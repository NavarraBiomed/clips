from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Hospital, Study, UserProfile, Case
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from .forms import CaseForm

import random, json


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
			breadcrumbs.append({'name':case, 'link':'/case/'+str(case.pk)+'/edit'})

		if info:
			breadcrumbs.append({'name':'Info', 'link':'/study/'+str(study.pk)+'/info'})



	return breadcrumbs

# Create your views here.

@login_required
def study_list(request):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")
	
	user = UserProfile.objects.get(user = request.user)
	breadcrumbs = generate_breadcrumbs
	return render(request, 'clips_app/study_list.html', {
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
	cases = Case.objects.filter(study = study, doctor = user)

	breadcrumbs = generate_breadcrumbs(study = study)

	if study in user.studies.all():
		return render(request, 'clips_app/study_details.html', {
			'study': study,
			'study_id':study.pk,
			'cases': cases,
			'user_prof':user,
			'breadcrumbs': breadcrumbs
			})
	else:
		return HttpResponseForbidden()


def calculate_score(case):
	score = 0
	if case.age_interval == 3: #>=75
		score += 1

	if case.asa != None and case.asa > 2:
		score +=1

	if case.maximum_size_mm != None and case.maximum_size_mm >= 40:
		score += 1


	if case.anticoagulants != None and case.anticoagulants > 0:
		score +=2

	if case.location !=None and case.location >= 4:
		score +=3

	if score == None:
		return -1

	return score


@login_required
def new_case(request, study_id):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	study = Study.objects.get(pk = study_id)
	clips = random.choice([0,1])

	breadcrumbs = generate_breadcrumbs(study = study, new = True)

	return render(request, 'clips_app/case_score.html', {
		'user_prof':user,
		'study_id':study_id,
		'clips':clips,
		'breadcrumbs': breadcrumbs
		})

def int_or_none(string):
	try:
		return int(string)
	except:
		return None

@login_required
def validate_score(request):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	hospital = Hospital.objects.get(pk = user.hospital_id)
	study = Study.objects.get(pk = request.POST['study_id'])

	if request.method == "POST":
		post = request.POST
		
		clips = int_or_none(post['clips'])
		age = int_or_none(post['age'])
		anticoagulants = int_or_none(post['anticoagulants'])
		asa = int_or_none(post['asa'])
		location = int_or_none(post['location'])
		size = int_or_none(post['maximum_size_mm'])
		study_id = int_or_none(post['study_id'])

		case = Case()
		study = Study.objects.get(pk = study_id)
		case.study = study
		case.doctor = user
		case.hospital = hospital
		case.clips = clips
		case.age_interval = age
		case.location = location
		case.asa = asa
		case.anticoagulants = anticoagulants
		case.maximum_size_mm = size
		#Calculate case ids
		try:
			last_id_for_doctor = Case.objects.filter(study = study, doctor = user).latest('id_for_doctor').id_for_doctor
		except:
			last_id_for_doctor = None
		try:
			last_id_for_hospital = Case.objects.filter(study = study, hospital = hospital).latest('id_for_hospital').id_for_hospital
		except:
			last_id_for_hospital = None

		if last_id_for_doctor == None:
			last_id_for_doctor = 0

		if last_id_for_hospital == None:
			last_id_for_hospital = 0


		case.id_for_doctor = last_id_for_doctor+1
		case.id_for_hospital = last_id_for_hospital+1

		score = calculate_score(case)

		if score >= 4:
			case.save()
			return redirect('/case/'+str(case.pk)+'/edit')

		return redirect('/POST/score:'+str(score)+"____location:_"+str(location))
	else:
		return redirect('/study/'+str(study.pk)+'/')

@login_required
def case_edit(request, pk):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	case = get_object_or_404(Case, pk=pk)

	if case.doctor != user:
		return HttpResponseForbidden()

	study = Study.objects.get(pk = case.study_id)
	hospital = Hospital.objects.get(pk = user.hospital_id)

	breadcrumbs = generate_breadcrumbs(study = study, case = case)

	if request.method == "POST":
	    form = CaseForm(request.POST, instance=case)
	    if form.is_valid():
	        case.save()
	        return redirect('/study/'+str(study.pk)+'/')
	else:
	    form = CaseForm(instance=case)
	return render(request, 'clips_app/case_edit.html', {
		'user_prof':user,
		'clips': case.clips,'study':study,
		'hospital':hospital,
		'form': form,
		'new': False,
		'breadcrumbs':breadcrumbs
		})


@login_required
def study_info(request, study_id):
	#Redirect to admin site if needed
	if request.user.is_superuser:
		return HttpResponseRedirect("/admin")

	user = UserProfile.objects.get(user = request.user)
	study = Study.objects.get(pk = study_id)

	breadcrumbs = generate_breadcrumbs(study = study, info = True)

	return render(request, 'clips_app/study_info.html', {
		'user_prof':user,
		'study_id':study.pk,
		'breadcrumbs':breadcrumbs
		})


@login_required
def message(request):
	return render(request, 'clips_app/message.html', {'user_prof':user, 'study':study})

@login_required
def study_json(request, study_id):
	data = []
	cases = Case.objects.filter(study_id = study_id)
	for case in cases:
		new_case = {'clips':case.clips, 'hospital': str(case.hospital),  'doctor':case.doctor.user.username}
		data.append(new_case)

	return HttpResponse(json.dumps(data), content_type='application/json')
