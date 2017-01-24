from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django import template
from django.template.loader import get_template, TemplateDoesNotExist
from django.conf import settings

from .models import *
from .forms import *
import sys
import random, json
import os

# Create your views here.

def generate_breadcrumbs(**kwargs):
	#Home > Study > Case / Info / New
	study = kwargs.get('study', None)
	case = kwargs.get('case', None)
	new = kwargs.get('new', None)
	info = kwargs.get('info', None)

	breadcrumbs = [{'name':'Home','link':'/'},]

	if study:
		breadcrumbs.append({'name':study.name, 'link':'/study/'+str(study.pk)})

		if new:
			breadcrumbs.append({'name':'New case', 'link':'/study/'+str(study.pk)+'/new'})

		if case:
			breadcrumbs.append({'name':case.short_name(), 'link':'/study/'+str(study.pk)+'/case/'+str(case.pk)+'/edit'})

		if info:
			breadcrumbs.append({'name':'Info', 'link':'/study/'+str(study.pk)+'/info'})



	return breadcrumbs

def test(request):
    	return render(request, 'studies_app/test.html', {
    		'user_prof':user,
    		})


@login_required
def study_list(request):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	breadcrumbs = generate_breadcrumbs()
	return render(request, 'studies_app/study_list.html', {
		'user_prof':user,
		'breadcrumbs':breadcrumbs
		})

@login_required
def study_details(request, study_id):

	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	study = Study.objects.get(pk = study_id)
	user = UserProfile.objects.get(user = request.user)
	cases = study.get_cases().filter(study = study, doctor = user)

	breadcrumbs = generate_breadcrumbs(study = study)

	if study in user.studies.all():
		return render(request, 'studies_app/study_details.html', {
			'study': study,
			'study_id':study.pk,
			'cases': cases,
			'user_prof':user,
			'breadcrumbs': breadcrumbs
			})
	else:
		return HttpResponseForbidden()


@login_required
def tutorial(request, study_id):
    study = Study.objects.get(pk = study_id)
    full_path = study.tutorial.url
    rel_path = full_path.split('/')[:-1]
    name = full_path.split('/')[-1]
    #path = os.path.join(settings.MEDIA_ROOT, rel_path, name)
    pdf = open(study.tutorial.url, 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + name
    return response


def case_edit(request, study_pk, case_pk):
	#Redirect to admin site if needed
    if request.user.is_superuser:
        return HttpResponseRedirect("/admin")

    user = UserProfile.objects.get(user = request.user)
    study = Study.objects.get(pk = study_pk)
    case = study.get_cases().get(pk = case_pk)
    hospital = user.hospital

	#case = get_object_or_404(TypeCase, pk=pk)

    breadcrumbs = generate_breadcrumbs(study = study, case = case)

    if request.method == "POST":

        form = get_form_from_case(case, post=request.POST, hidden_fields=['clips_tratment_group'])
        #form = CancerForm(request.POST, instance = case)
        if form.is_valid():
            case.save()
            return redirect('/study/'+str(study.pk)+'/')
        else:
            return render(request, form.template, {
                'user_prof':user,
                'hospital':hospital,
                'group': case.group,
                'study':study,
                'form': form,
                'case':case,
                'new': False,
                'breadcrumbs':breadcrumbs
                })

            #raise Exception("Form isn't valid. Form type: {}".format( type(form) ))
    else:
        form = get_form_from_case(case, hidden_fields=['clips_tratment_group'])
        return render(request, form.template, {
            'user_prof':user,
            'hospital':hospital,
            'group': case.group,
            'study':study,
            'form': form,
            'case':case,
            'new': True,
            'breadcrumbs':breadcrumbs
            })

@login_required
def new_case(request, study_id):
    #Redirect to admin site if needed
    if request.user.is_superuser:
        return HttpResponseRedirect("/admin")

    user = UserProfile.objects.get(user = request.user)
    study = Study.objects.get(pk = study_id)
    group = random.choice([0,1])

    breadcrumbs = generate_breadcrumbs(study = study, new = True)

    #get the corresponding template or the default one
    template_name = "studies_app/validation/"+study.study_type+".html"
    try:
        get_template(template_name)
    except TemplateDoesNotExist:
        template_name = "studies_app/validation/default.html"

    #template_name = "studies_app/"+study.study_type+"_validation.html"

    return render(request, template_name, {
    	'user_prof':user,
    	'study_id':study_id,
    	'group':group,
    	'breadcrumbs': breadcrumbs
    	})

@login_required
def validate_case(request, study_id):
    study = Study.objects.get(pk = study_id)
    #get the calss that corresponds to the study type
    case_class = getattr(sys.modules[__name__], study.study_type.title()+"Case")

    if request.method == "POST":
        new_case_pk = case_class.validate(request)
        if new_case_pk is not None:
            return redirect("/study/"+str(study.pk)+"/case/"+str(new_case_pk)+"/edit") #redirect('/case/'+str(case.pk)+'/edit')
        else:
            return redirect('/study/'+str(study.pk))
    else:
        return redirect('/study/'+str(study.pk))

@login_required
def study_info(request, study_id):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	study = Study.objects.get(pk = study_id)

	breadcrumbs = generate_breadcrumbs(study = study, info = True)

	return render(request, 'studies_app/study_info.html', {
		'user_prof':user,
		'study_id':study.pk,
		'breadcrumbs':breadcrumbs
		})

@login_required
def study_json(request, study_id):
    data = []
    cases = Study.objects.get(pk=study_id).get_cases().all()
    for case in cases:
        try:
            new_case = {'clips':case.group, 'hospital': str(case.doctor.hospital),  'doctor': case.doctor.user.first_name + " " + case.doctor.user.last_name}
        except:
            raise KeyError('No user in case: ' + str(case))
        data.append(new_case)

    return HttpResponse(json.dumps(data), content_type='application/json')
