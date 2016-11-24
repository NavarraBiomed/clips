from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from studies_app.models import *
import json


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('study_pk')

    def handle(self, *args, **options):
        study_pk = options['study_pk']
        study = Study.objects.get( pk=study_pk )

        users = User.objects.all()
        for user in users:
            print(user)
            print("-----------")
            cases = study.get_cases().filter(doctor__user = user)
            for case in cases:
                print(case)
            print("")
