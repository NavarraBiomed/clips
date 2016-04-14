from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Hospital, Study, UserProfile, Case
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from .forms import CaseForm

import random, json



# Create your views here.

@login_required
def study_list(request):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")
	
	user = UserProfile.objects.get(user = request.user)
	return render(request, 'clips_app/study_list.html', {'user_prof':user})


@login_required
def study_details(request, study_id):

	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	study = Study.objects.get(pk = study_id)
	user = UserProfile.objects.get(user = request.user)
	cases = Case.objects.filter(study = study, doctor = user)
	if study in user.studies.all():
		return render(request, 'clips_app/study_details.html', {'study': study, 'cases': cases, 'user_prof':user})
	else:
		return HttpResponseForbidden()


@login_required
def new_case(request, study_id):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	study = Study.objects.get(pk = study_id)
	hospital = Hospital.objects.get(pk = user.hospital_id)
	clips = random.choice([0,1])

	if request.method == "POST":		
		form = CaseForm(request.POST)
		if form.is_valid():			
			case = form.save()
			return redirect('/study/'+str(study_id)+'/')
		else:
			return redirect('/invalid_form/')
	else:
		form = CaseForm()
	return render(request, 'clips_app/case_edit.html', {'user_prof':user, 'clips': clips, 'study':study, 'hospital':hospital, 'form': form,  'new': True})


@login_required
def case_edit(request, pk):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	case = get_object_or_404(Case, pk=pk)
	study = Study.objects.get(pk = case.study_id)
	hospital = Hospital.objects.get(pk = user.hospital_id)
	if request.method == "POST":
	    form = CaseForm(request.POST, instance=case)
	    if form.is_valid():
	        case.save()
	        return redirect('/study/'+str(study.pk)+'/')
	else:
	    form = CaseForm(instance=case)
	return render(request, 'clips_app/case_edit.html', {'user_prof':user, 'clips': case.clips,'study':study, 'hospital':hospital, 'form': form, 'new': False})

@login_required
def study_info(request, study_id):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	study = Study.objects.get(pk = study_id)

	return render(request, 'clips_app/study_info.html', {'user_prof':user, 'study':study})


@login_required
def study_json(request, study_id):
	data = []
	cases = Case.objects.filter(study_id = study_id)
	for case in cases:
		new_case = {'clips':case.clips, 'hospital': str(case.hospital),  'doctor':case.doctor.user.username}
		data.append(new_case)

	return HttpResponse(json.dumps(data), content_type='application/json')