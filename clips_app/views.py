from django.shortcuts import render
from .models import Hospital, Study, UserProfile, Case
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import random



# Create your views here.

@login_required
def study_list(request):
	user = UserProfile.objects.get(user = request.user)
	return render(request, 'clips_app/study_list.html', {'user_prof':user})


@login_required
def study_details(request, study_id):
	study = Study.objects.get(pk = study_id)
	user = UserProfile.objects.get(user = request.user)
	cases = Case.objects.filter(study = study, doctor = user)
	if study in user.studies.all():
		return render(request, 'clips_app/study_details.html', {'study': study, 'cases': cases, 'user':user})
	else:
		return HttpResponseForbidden()


@login_required
def new_case(request, study_id):
	study = Study.objects.get(pk = study_id)
	control = random.choice([0, 1])
	return render(request, 'clips_app/new_case.html', {'study':study, 'control': control})