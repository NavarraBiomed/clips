from django.core.management.base import BaseCommand
from studies_app.models import Study
import csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('study_pk')

    def handle(self, *args, **options):
        study_pk = options['study_pk']
        study = Study.objects.get(pk=study_pk)
        cases = study.get_cases().all()

        with open('output.csv', 'w', newline="\n") as outputfile:
            writer = csv.writer(outputfile)

            # Write headers
            first_case = cases[0]
            header = []
            for field in first_case._meta.get_fields():
                header.append(field.name)

            writer.writerow(header)

            for case in cases:
                fields = case._meta.get_fields()
                row_data = []
                for field in fields:
                    value = getattr(case, field.name, None)
                    if value is None:
                        value = ''
                    if type(value) is int and field.choices:
                        try:
                            value = find_value_in_tuples(field.choices, value)
                        except Exception as e:
                            pass
                    if type(value) is str:
                        value = value.replace('\r', '')
                        value = value.replace('\n', ' ')
                        value = value.strip()
                    row_data.append(value)
                writer.writerow(row_data)
