from django.core.management.base import BaseCommand, CommandError
from clips_app.models import *
from studies_app.models import *
import json


class Command(BaseCommand):

    def handle(self, *args, **options):

        clip_cases = Case.objects.all()

        clips_study = Study.objects.all()[0]

        for case in clip_cases:
            new_case = ClipsCase()
            fields = case._meta.get_fields()
            for field in fields:

                #import pdb; pdb.set_trace()
                if field.name == "study":
                    new_case.study = clips_study

                elif field.name == "clips":
                    setattr(new_case, 'group', getattr(case,field.name) )

                elif field.name == "hospital":
                    continue

                else:
                    try:
                        setattr(new_case, field.name, getattr(case,field.name) )
                    except:
                        print("ERROR: " + str(new_case) )
                        

            print("Case saved: " + str(new_case) )
            new_case.save()
