from django.core.management.base import BaseCommand, CommandError
from clips_app.models import *
from studies_app.models import *
import json

class Command(BaseCommand):

    def handle(self, *args, **options):


        user_studies = UserProfileStudies.objects.all()
        for user_studies in user_studies:

            user_prof = UserProfile()
            user_prof.user = user_studies.user
            user_prof.save()
