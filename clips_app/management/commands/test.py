from django.core.management.base import BaseCommand, CommandError
from clips_app.models import Study
import django


import csv

def parse_num(value):
    if value.isdigit():
        return int(value)
    else:
        return None;

def parse_date(value):
    pieces = value.split("/")
    try:
        return (pieces[2]+"-"+pieces[0]+"-"+pieces[1])
    except IndexError:
        return None;

class Command(BaseCommand):
    help = 'Command test'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type = str)

    

    def handle(self, *args, **options):
        input_file =  options['file'][0]
        print("Reading data from " + input_file)

        model_to_row = {
                'doctor' : 'Medicoresponsable',
                'date' : 'Date',
                'name' : 'Name',
                'id_number' : 'IDnumber',
                'age' : 'Age',
                'age_interval' : 'Tramos_edad',
                'sex' : 'Sex',
                'asa' : 'ASA' , 
                #'hypertension' : '', 
                'hb' : 'HB',
                'platelets' : 'Platelets',
                'inr' : 'INR',
                'pt' : 'PT',
                'aspirin' : 'Aspirin',
                'anticoagulants' : 'Anticoagulants',
                'antiplatelet_anticoagulant' : 'Antiplatelet_anticoagulant',
                #'heparinbridgetherapy' : '', 
                 #'nombre_p_activo_antiagreg_anticoag' : '', 
                 #'day_of_reintroduction_antiagregant' : '', 
                'paris_calif' : 'ParisClasif',
                'lst_yn' : 'LSTyn',
                #'lst_morphology' : '', 
                'large_nodule_one_cm' : 'LargeNodule1cm',
                'demacrated_depressed_area' : 'DemarcatedDepressedArea',
                'sclerous_wall_change' : 'SclerousWallChange',
                'fold_convergency' : 'FoldConvergency',
                'chicken_skin_mucosa_around' : 'ChickenSkinMucosaAround',
                'maximum_size_mm' : 'Size.mm', #?
                'area_square_cm' : 'Areacm2',
                'location' : 'Location',
                'ileocecal_valve_involvement' : 'Ileocecalvalveinvolvement',
                'high_definition' : 'HighDefinition',
                #'histologyigh_definition' : '', 
                'endoscopemodel' : 'Endoscopemodel',
                'nbi' : 'NBI',
                'nbi_sano' : 'NBI.Sano',
                'nbi_nice' : 'NBI.NICE',
                'cromoendoscopy' : 'cromoendoscopy',
                'kudo' : 'Kudo',
                'prepathologic_endoscopic_diagnostic_a' : 'PrepathologicEndoscopicDiagnosticA',
                'prepathologic_endoscopic_diagnostic_b' : 'PrepathologicEndoscopicDiagnosticB',
                'correct_dx_adenoma_serrated': 'CorrectDxAdenomaSerrado',
                'correct_dx_invasion' : 'CorrectDxInvasiónprofunda',
                'histology' : 'Histology',
                'histol_simplified' : 'Histol_simplified',
                'time_of_procedure_in_mins' : 'Timeofprocedureinmins',
                'difficulty_of_emr' : 'DifficultyofEMR',
                'accesibility' : 'Accessibility',
                'resection' : 'Resection',
                'resection_yn' : 'ResectionYN',
                'previous_biopsy' : 'Previous.biopsy',
                'previous_attempt' : 'Previous.attempt',
                'non_lifting_sign' : 'Nonliftingsign',
                'technique' : 'Technique',
                'technique_two' : 'Technique2',
                'limit_marks' : 'LimitMarks',
                'injection' : 'Injection',
                'adrenaline' : 'Adrenaline',
                'endocut' : 'Endocut',
                'electrosurgical_generator_model' : 'Electrosurgicalgeneratormodel',
                'polyp_retrieval' : 'PolypRetrieval',
                'argon_PC' : 'ArgonPC',
                'argon_coagulacion' : 'argón_coagulación',
                'coagulation_forceps' : 'Coagulationforceps',
                'clips' : 'Clipping', #?
                #'clips_control_group' : '', 
                #'clips_tratment_group' : '', 
                #'not_tired_closure_by' : '', 
                #'closure_technique' : '', 
                'number_clips_needed' : 'ClipsNeeded',
                'perforation' : 'Perforation',
                'surgery_from_endoscopy' : 'Surgeryfromendoscopy',
                'surgery_by_complication' : 'Surgerybycomplication',
                'bleeding' : 'Bleeding',
                #'immediate_bleeding' : '', 
                'delayed_bleeding' : 'Delayedbleeding',
                'bleeding_treatment' : 'BleedingTreatment',
                'transfusion' : 'Trasfusion',
                'pps' : 'SPP', #?
                #'fever' : '', 
                #'pain_requiring_medical_intervention' : '', 
                'hospital_stay_by_technique' : 'HospitalStayByTechniche',
                'hospital_stay_by_complication' : 'HospitalStayByComplication',
                'follow_up_months' : 'FollowUpInMonths',
                'successful_treatment' : 'Successfultreatment',
                'sedation' : 'Sedation',
                'last_date_endoscopic_follow_up' : 'LastDateEndoscopicFollowUp',
                'recurrence_three_six_months_control' : 'Recurrence3monthscontrol',
                'recurrenec_one_year_control' : 'Recurrence1yearcontrol',
                'global_recurrence' : 'Globalrecurrence',
                'other_complications_comments' : 'OtherComplicationsComments',
                'other_comments' : 'OtherComments'
            }

        with open(input_file, 'rt') as f:
            reader = csv.DictReader(f)
            #reader_list = list(reader)
            #print(reader_list[0].keys())
            for index, row in enumerate(reader):
                #row = reader_list[0]
                print("-------- Study #"+ str(index)+" ----------")
                for field in Study._meta.get_fields():
                    if type(field) is django.db.models.fields.IntegerField:
                        try:
                            row[model_to_row[field.name]] =  parse_num(row[model_to_row[field.name]])
                        except KeyError:
                            print("KeyError: "+field.name)

                    elif type(field) is django.db.models.fields.DateField:
                        try:
                            row[model_to_row[field.name]] = parse_date(row[model_to_row[field.name]])
                        except:
                            print("Date format error in :"+model_to_row[field.name]+ " -> "+row[model_to_row[field.name]])
                
                Study.objects.create(
                    doctor = row['Medicoresponsable'],
                    date = row['Date'],
                    name = row['Name'],
                    id_number = row['IDnumber'],
                    age = row['Age'],
                    age_interval = row['Tramos_edad'],
                    sex = row['Sex'],
                    asa = row['ASA'] , 
                    #hypertension = row[],
                    hb = row['HB'],
                    platelets = row['Platelets'],
                    inr = row['INR'],
                    pt = row['PT'],
                    aspirin = row['Aspirin'],
                    anticoagulants = row['Anticoagulants'],
                    antiplatelet_anticoagulant = row['Antiplatelet_anticoagulant'],
                    #heparinbridgetherapy = row[''],
                    # nombre_p_activo_antiagreg_anticoag = row[''],
                    # day_of_reintroduction_antiagregant = row[''],
                    paris_calif = row['ParisClasif'],
                    lst_yn = row['LSTyn'],
                    #lst_morphology = row[''],
                    large_nodule_one_cm = row['LargeNodule1cm'],
                    demacrated_depressed_area = row['DemarcatedDepressedArea'],
                    sclerous_wall_change = row['SclerousWallChange'],
                    fold_convergency = row['FoldConvergency'],
                    chicken_skin_mucosa_around = row['ChickenSkinMucosaAround'],
                    maximum_size_mm = row['Size.mm'], #?
                    area_square_cm = row['Areacm2'],
                    location = row['Location'],
                    ileocecal_valve_involvement = row['Ileocecalvalveinvolvement'],
                    high_definition = row['HighDefinition'],
                    #histologyigh_definition = row[''],
                    endoscopemodel = row['Endoscopemodel'],
                    nbi = row['NBI'],
                    nbi_sano = row['NBI.Sano'],
                    nbi_nice = row['NBI.NICE'],
                    cromoendoscopy = row['cromoendoscopy'],
                    kudo = row['Kudo'],
                    prepathologic_endoscopic_diagnostic_a = row['PrepathologicEndoscopicDiagnosticA'],
                    prepathologic_endoscopic_diagnostic_b = row['PrepathologicEndoscopicDiagnosticB'],
                    correct_dx_adenoma_serrated= row['CorrectDxAdenomaSerrado'],
                    correct_dx_invasion = row['CorrectDxInvasiónprofunda'],
                    histology = row['Histology'],
                    histol_simplified = row['Histol_simplified'],
                    time_of_procedure_in_mins = row['Timeofprocedureinmins'],
                    difficulty_of_emr = row['DifficultyofEMR'],
                    accesibility = row['Accessibility'],
                    resection = row['Resection'],
                    resection_yn = row['ResectionYN'],
                    previous_biopsy = row['Previous.biopsy'],
                    previous_attempt = row['Previous.attempt'],
                    non_lifting_sign = row['Nonliftingsign'],
                    technique = row['Technique'],
                    technique_two = row['Technique2'],
                    limit_marks = row['LimitMarks'],
                    injection = row['Injection'],
                    adrenaline = row['Adrenaline'],
                    endocut = row['Endocut'],
                    electrosurgical_generator_model = row['Electrosurgicalgeneratormodel'],
                    polyp_retrieval = row['PolypRetrieval'],
                    argon_PC = row['ArgonPC'],
                    argon_coagulacion = row['argón_coagulación'],
                    coagulation_forceps = row['Coagulationforceps'],
                    clips = row['Clipping'], #?
                    #clips_control_group = row[''],
                    #clips_tratment_group = row[''],
                    #not_tired_closure_by = row[''],
                    #closure_technique = row[''],
                    number_clips_needed = row['ClipsNeeded'],
                    perforation = row['Perforation'],
                    surgery_from_endoscopy = row['Surgeryfromendoscopy'],
                    surgery_by_complication = row['Surgerybycomplication'],
                    bleeding = row['Bleeding'],
                    #immediate_bleeding = row[''],
                    delayed_bleeding = row['Delayedbleeding'],
                    bleeding_treatment = row['BleedingTreatment'],
                    transfusion = row['Trasfusion'],
                    pps = row['SPP'], #?
                    #fever = row[''],
                    #pain_requiring_medical_intervention = row[''],
                    hospital_stay_by_technique = row['HospitalStayByTechniche'],
                    hospital_stay_by_complication = row['HospitalStayByComplication'],
                    follow_up_months = row['FollowUpInMonths'],
                    successful_treatment = row['Successfultreatment'],
                    sedation = row['Sedation'],
                    last_date_endoscopic_follow_up = row['LastDateEndoscopicFollowUp'],
                    recurrence_three_six_months_control = row['Recurrence3monthscontrol'],
                    recurrenec_one_year_control = row['Recurrence1yearcontrol'],
                    global_recurrence = row['Globalrecurrence'],
                    other_complications_comments = row['OtherComplicationsComments'],
                    other_comments = row['OtherComments']
               )