from django.core.management.base import BaseCommand, CommandError
from studies_app.models import *
import json


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('study_pk')

    def handle(self, *args, **options):
        study_pk = options['study_pk']
        study = Study.objects.get( pk=study_pk )

        study.refresh_cases_ids()
