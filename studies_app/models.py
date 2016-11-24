from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


"""

To add a new study type:

1) Add a lower case entry in _STUDY_TYPES (we'll call it "name" from now on)

2) Add a new model called NameCase(TypeCase) for the study's cases
    2.1) define the variables for Django
    2.2) create a validate(request) method inside

3) Add a new class NameForm(CaseForm) to forms.py
    (optional)
    3.1 Create and add a custom template to the form

4) Add the condition to get_form_from_case(case) in forms.py

(Optional)
5) Add the validation template as /validation/name.html

6) Add admin.site.register(NameCase) to admin.py

"""

_STUDY_TYPES = [
	("clips", "Clips Study"),
	("cancer", "Cancer Study"),
    ("observational", "Observational Study"),
    ("obsinternational", "International Observational Study"),
	]

_GROUPS = (
	(0, "Control group"),
	(1, "Treatment group")
	)

#MODEL choices

_SEX = (
	(1, "Male"),
	(2, "Female")
	)

_TRAMOS_EDAD = (
	(1, "< 60"),
	(2, "60-74"),
	(3, ">= 75")
	)

_ASA = (
	(1, "I"),
	(2, "II"),
	(3, "III"),
	(4, "IV")
	)

_NO_YES = (
	(0, "No"),
	(1, "Yes")
	)

_ASPIRIN = (
	(0, "No"),
	(1, "100mg cease"),
	(2, "300mg cease"),
	(3, "100mg during EMR"),
	(4, "300mg during EMR")
	)

_ANTICOAGULANT = (
	(0, "No"),
	(1, "Aspirin"),
	(2, "Clopidogrel"),
	(3, "Other antiagregant"),
	(4, "Warfarin"),
	(5, "NSAID"),
	(6, "2 NSAID including aspiring or not"),
	(7, "Aspirin+clopidogrel"),
	(8, "NACOs")
	)

_ANTIPLATELET = (
	(0, "No"),
	(1, "Antiplatelet"),
	(2, "Double antiplatelet"),
	(3, "Warfarin acenocumarol"),
	(4, "Dabigatran (new antic)")
	)

_PARIS = (
	(1, "0Is"),
	(2, "0IIa"),
	(3, "0IIa+0Is"),
	(4, "0Is+0IIa"),
	(5, "0IIb"),
	(6, "0IIc"),
	(7, "0IIa+0IIc"),
	(8, "0IIb+0IIc"),
	(9, "0IIb+0IIa")
	)

_MORPHOLOGY = (
	(1, "Granular homogeneous"),
	(2, "Focal nodular mixed type"),
	(3, "Whole nodular mixed type"),
	(4, "Flat elevated"),
	(5, "Psudodepressed")
	)

_LOCATION = (
	(1, "Rectum"),
	(2, "Left colon"),
	(3, "Splenic flexure"),
	(4, "Transverse"),
	(5, "Hepatic"),
	(6, "Ascendent"),
	(7, "Cecum")
	)

_HIGH_DEFINITION = (
	(1, "Conventional endoscope"),
	(2, "High definition"),
	(3, "Optic magnification")
	)

_NBI_SANO = (
	(1, "I"),
	(2, "II"),
	(3, "IIIA"),
	(4, "IIIB")
	)

_NBI_NICE = (
	(1, "Type 1"),
	(2, "Type 2"),
	(3, "Type 3")
	)

_KUDO = (
	(1, "I"),
	(2, "II"),
	(3, "IIIS"),
	(4, "IIIL"),
	(5, "IV"),
	(6, "V-I"),
	(7, "V-N")
	)

_PED_A = (
	(1, "Adenoma"),
	(2, "Serrated")
	)

_PED_B = (
	(1, "NodisplasiaToSuperficial submucosal carcinoma"),
	(2, "Deep submucosal carcinoma")
	)

_HISTOLOGY = (
	(1, "Adenoma"),
	(2, "HGD-intraepitelial carcinoma in adenoma"),
	(3, "Intramucosal carcinoma in adenoma"),
	(4, "Superficial submucosal carcinoma in adenoma"),
	(5, "Deep submucosal carcinoma in adenoma"),
	(6, "Hyperplastic"),
	(7, "Sesil Serrated polyp"),
	(8, "Traditional Serrated Adenoma"),
	(9, "Polyp Serrated Mixed or serrated polyp with dysplasia"),
	(10, "Intraepitelial carcinoma Any serrated"),
	(11, "Intramucosal carcinoma Any serrated"),
	(12, "Superficial submucosa carc. Any serrated"),
	(13, "Deep submucosa carc. Any serrated"),
	(14, "Carinoid")
	)

_HISTOLOGY_SIMP = (
	(1, "Adenoma"),
	(2, "HGD-Imucosal"),
	(3, "Invasive adenoma"),
	(4, "Serrated"),
	(5, "HGD-Imucosal serrated"),
	(6, "Invasive serrated"),
	(7, "Carcinoid")
	)

_DIFFICULTY = (
	(1, "Easy"),
	(2, "Medium"),
	(3, "Difficult")
	)

_RESECTION = (
	(1, "Piecemeal complete"),
	(2, "Piecemeal incomplete"),
	(3, "En bloc R0"),
	(4, "En bloq incomplete")
	)

_RESECTION_YN = (
	(1, "Piecemeal"),
	(2, "En bloc")
	)

_TECHNIQUE = (
	(1, "EMR"),
	(2, "Hybrid-EMR")
	)

_TECHNIQUE_TWO = (
	(1, "One-step"),
	(2, "Two-steps")
	)

_MARKS = (
	(0, "No marks"),
	(1, "APC marks")
	)

_INJECTION = (
	(0, "No"),
	(1, "Saline"),
	(2, "Glicerin"),
	(3, "Hyaluronic"),
	(4, "Hidrox-propil-cellulose: VOLUVEN(r)"),
	(5, "Gelafundin"),
	(6, "Others")
	)

_ENDOCUT = (
	(1, "Only cut current"),
	(2, "Only coagulation current"),
	(3, "Endocut/Blended")
	)

_POLYP_RETRIEVAL = (
	(1, "Roth net"),
	(2, "By aspiration"),
	(3, "Both methods"),
	(4, "By snare")
	)

_ARGON_PC = (
	(0, "No"),
	(1, "Yes: incomplete resection"),
	(2, "Yes: coagulation"),
	(3, "Yes: per protocol")
	)



_CLIPS_CONTROL = (
	(0, "No"),
	(1, "Punctual coagulation")
	)

_CLIPS_TREAT_GROUP = (
	(1, "Complete closure with complete mucosal apposition"),
	(2, "Complete closure without complete mucosal apposition"),
	(3, "Total failed closure"),
	(4, "Partial failed closure"),
	(5, "Closure not tried")
	)

_NOT_TRIED = (
	(1, "Big size"),
	(2, "Difficult location"),
	(3, "Both")
	)

_CLOSURE_TECHNIQUE = (
	(1, "Simple clipping"),
	(2, "Clip-Poly loop"),
	(3, "Clip Silk loop")
	)

_PERFORATIOM = (
	(0, "No"),
	(1, "Yes: endoscopic resolution"),
	(2, "Yes: surgical resolution")
	)

_SURGERY_BY_COMPLICATION = (
	(0, "No"),
	(1, "Yes: bleeding"),
	(2, "Yes: perforation")
	)

_BLEEDING = (
	(0, "No"),
	(1, "During no clinical impact-autol"),
	(2, "During exploration with clinical impact"),
	(3, "24h"),
	(4, "24-48h"),
	(5, "3-7 days"),
	(6, ">7 days")
	)

_IMMEDIATE_BLEEDING = (
	(0, "No"),
	(1, "Yes: during exploration with clinical impact"),
	(2, "Yes: during exploration without clinical impact")
	)

_BLEEDING_TREATMENT = (
	(0, "No"),
	(1, "Inyection"),
	(2, "Clipping"),
	(3, "ArgonPC"),
	(4, "Coagulation forceps"),
	(5, "2 methods")
	)

_FEVER = (
	(0, "No"),
	(1, "37-37.9"),
	(2, "38 or more")
	)

_SUCCESSFUL_TREATMENT = (
	(0, "No: surgical treatment"),
	(1, "Yes: in 1 session (includes one or two steps"),
	(2, "Yes, in 2 or more sessions (one session and treatment in controls")
	)

_SEDATION = (
	(0, "Without sedation"),
	(1, "By gastroenterologist other than Propofol"),
	(2, "By gastroenterologist based on Propofol"),
	(3, "By anesthesiologist")
	)

_RECURRENCE_THREE_SIX = (
	(0, "No"),
	(1, "Yes: positive biopsy: endoscopic treatment"),
	(2, "Yes: visible recurrence: endoscopic treatment"),
	(3, "Yes: surgical treatment needed")
	)

_RECURRENCE_ONE_YEAR = (
	(0, "No"),
	(1, "Yes: positive biopsy: endoscopic treatment"),
	(2, "Yes: visible recurrence: endoscopic treatment"),
	(3, "Yes: surgical treatment needed")
	)

_ENDOCUT_MODE = (
	(1, "1"),
	(2, "2"),
	(3, "3"),
	(4, "4")
	)

_COAGULATION = (
	(0, "Soft"),
	(1, "Force")
	)

#---------------------------



def int_or_none(string):
	try:
		return int(string)
	except:
		return None

class Hospital(models.Model):
    name = models.CharField(verbose_name = "Name", max_length = 100)

    def __str__(self):
        return self.name

# Create your models here.
class Study(models.Model):
    name = models.CharField(max_length=64)
    study_type = models.CharField(verbose_name="Study type", choices = _STUDY_TYPES, max_length=64)

    class Meta:
        verbose_name_plural = "Studies"

    def __str__(self):
        return self.name

    def get_cases(self):
        return getattr(self, "cases_" + self.study_type +"case" )

    def refresh_cases_ids(self):
        cases = self.get_cases().all()
        for case in cases:
            TypeCase.set_case_ids(case)


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="clips_userprofile")
	hospital = models.ForeignKey('Hospital', null=True)
	studies = models.ManyToManyField('Study')

	def __str__(self):
		return str(self.user)

class TypeCase(models.Model):
    study = models.ForeignKey(Study, verbose_name="Study", related_name='cases_%(class)s')
    doctor = models.ForeignKey('UserProfile', verbose_name = "Doctor", blank= True, null = True)
    #hospital = models.ForeignKey('Hospital', default = None , blank= True, null = True)
    group = models.IntegerField(verbose_name = "Group", choices = _GROUPS, blank= True, null = True)

    validate_template = ""

    id_for_hospital = models.IntegerField(verbose_name = "Id for hospital", blank= True, null = True)
    id_for_doctor = models.IntegerField(verbose_name = "Id for doctor", blank= True, null = True)

    def __str__(self):
        return str(self.pk) + " (D-"+str(self.id_for_doctor) +" H-"+str(self.id_for_hospital)+")"

    """
    validate function takes the request and returns:
        None: if validation failed
        case_pk: the new case's pk, if validation was successful
    """
    def validate(request):
        pass

    def get_case_ids(case):

        older_cases = case.study.get_cases().filter(pk__lt=case.pk)
        older_from_doctor = older_cases.filter(doctor= case.doctor)
        older_from_hospital = older_cases.filter(doctor__hospital = case.doctor.hospital)

        id_for_doctor = len(older_from_doctor)+1
        id_for_hospital = len(older_from_hospital)+1

        return (id_for_doctor, id_for_hospital)


    def set_case_ids(case):
        ids = TypeCase.get_case_ids(case)
        if case.id_for_doctor != ids[0] or case.id_for_hospital != ids[1]:
            case.id_for_doctor = ids[0]
            case.id_for_hospital = ids[1]
            case.save()

    class Meta:
        abstract = True



class ClipsCase(TypeCase):

    date = models.DateField(verbose_name = "Date", blank= True, null = True)
    age = models.IntegerField(verbose_name = "Age", validators = [MinValueValidator(0)], blank= True, null = True)
    age_interval = models.IntegerField(verbose_name = "Age interval", choices = _TRAMOS_EDAD, blank= True, null = True) #nombre en español?
    sex = models.IntegerField(verbose_name = "Sex", choices = _SEX, blank= True, null = True)
    asa = models.IntegerField(verbose_name = "ASA", choices = _ASA , blank= True, null = True)
    hypertension = models.IntegerField(verbose_name = "Hypertension", choices = _NO_YES, blank= True, null = True)
    hb = models.FloatField(verbose_name = "HB (g/dL)", blank= True, null = True)
    platelets = models.IntegerField(verbose_name = "Platelets (x10⁹/L)", blank= True, null = True)
    inr = models.FloatField(verbose_name = "INR", blank= True, null = True) #max-min ?
    pt = models.IntegerField(verbose_name = "PT (s)", blank= True, null = True)   #max-min ?
    aspirin = models.IntegerField(verbose_name = "Aspirin", choices = _ASPIRIN, blank= True, null = True)
    anticoagulants = models.IntegerField(verbose_name = "Anticoagulants", choices = _ANTICOAGULANT, blank= True, null = True)
    heparinbridgetherapy = models.IntegerField(verbose_name = "Heparin Bridge Therapy", choices = _NO_YES, blank= True, null = True)
    nombre_p_activo_antiagreg_anticoag = models.CharField(verbose_name = "Active ingredients anticoagulant/antiagregant", max_length=128, blank= True, null = True)
    day_of_reintroduction_antiagregant = models.IntegerField(verbose_name = "Day of reintroduction anticoagulant/antiagregant", blank= True, null = True)
    paris_calif = models.IntegerField(verbose_name = "Paris Clasif.", choices = _PARIS, blank= True, null = True)
    lst_yn = models.IntegerField(verbose_name = "LST yn", choices= _NO_YES, blank= True, null = True)
    lst_morphology = models.IntegerField(verbose_name = "LST Morphology", choices = _MORPHOLOGY, blank= True, null = True)
    large_nodule_one_cm = models.IntegerField(verbose_name = "Large nodule 1cm", choices = _NO_YES, blank= True, null = True)
    demacrated_depressed_area = models.IntegerField(verbose_name = "Demacrated depressed area", choices = _NO_YES, blank= True, null = True)
    sclerous_wall_change = models.IntegerField(verbose_name = "Sclerous wall change", choices = _NO_YES, blank= True, null = True)
    fold_convergency = models.IntegerField(verbose_name = "Fold convergency", choices = _NO_YES, blank= True, null = True)
    chicken_skin_mucosa_around = models.IntegerField(verbose_name = "Chicken skin mucosa around", choices = _NO_YES, blank= True, null = True)
    maximum_size_mm = models.IntegerField(verbose_name="Maximum size (mm)", blank= True, null = True)
    area_square_cm = models.IntegerField(verbose_name = "Area (cm2)", blank= True, null = True)
    location = models.IntegerField(verbose_name = "Location", choices = _LOCATION, blank= True, null = True)
    ileocecal_valve_involvement = models.IntegerField(verbose_name = "Ileocecal valve involvement", choices =_NO_YES, blank= True, null = True)
    high_definition = models.IntegerField(verbose_name = "High definition", choices = _HIGH_DEFINITION, blank= True, null = True)
    endoscopemodel = models.CharField(verbose_name = "Endoscope model", max_length = 50, blank= True, null = True)
    nbi = models.IntegerField(verbose_name = "NBI", choices = _NO_YES, blank= True, null = True)
    nbi_sano = models.IntegerField(verbose_name = "NBI sano", choices = _NBI_SANO, blank= True, null = True) #nombre en español?
    nbi_nice = models.IntegerField(verbose_name = "NBI NICE", choices = _NBI_NICE, blank= True, null = True) #NICE son siglas?
    cromoendoscopy = models.IntegerField(verbose_name = "Cromoendoscopy", choices = _NO_YES, blank= True, null = True)
    kudo = models.IntegerField(verbose_name = "Kudo", choices = _KUDO, blank= True, null = True)
    prepathologic_endoscopic_diagnostic_a = models.IntegerField(verbose_name = "Prepathologic endoscopic diagnost 1", choices = _PED_A , blank= True, null = True)
    prepathologic_endoscopic_diagnostic_b = models.IntegerField(verbose_name = "Prepathologic endoscopic diagnost 2", choices = _PED_B , blank= True, null = True)
    correct_dx_adenoma_serrated = models.IntegerField(verbose_name = "Correct Dx Adenoma Serrated", choices = _NO_YES, blank= True, null = True)
    correct_dx_invasion = models.IntegerField(verbose_name = "Correct Dx Invasion", choices = _NO_YES, blank= True, null = True)
    histology = models.IntegerField(verbose_name = "Histology", choices = _HISTOLOGY, blank= True, null = True)
    histol_simplified = models.IntegerField(verbose_name = "Histology simplified", choices = _HISTOLOGY_SIMP, blank= True, null = True)
    time_of_procedure_in_mins = models.IntegerField(verbose_name = "Time of procedure (m)", blank= True, null = True)
    difficulty_of_emr = models.IntegerField(verbose_name = "Dificutly of EMR", choices = _DIFFICULTY, blank= True, null = True)
    accesibility = models.IntegerField(verbose_name = "Accesibility", choices = _DIFFICULTY, blank= True, null = True)
    resection = models.IntegerField(verbose_name = "Resection", choices = _RESECTION, blank= True, null = True)
    previous_biopsy = models.IntegerField(verbose_name = "Previous biopsy", choices = _NO_YES, blank= True, null = True)
    previous_attempt = models.IntegerField(verbose_name = "Previous attempt", choices = _NO_YES, blank= True, null = True)
    non_lifting_sign = models.IntegerField(verbose_name = "Non lifting sign", choices = _NO_YES, blank= True, null = True)
    technique = models.IntegerField(verbose_name = "Technique", choices = _TECHNIQUE, blank= True, null = True)
    technique_two  = models.IntegerField(verbose_name =" Technique 2", choices = _TECHNIQUE_TWO, blank= True, null = True)
    limit_marks = models.IntegerField(verbose_name = "Limit marks", choices = _MARKS, blank= True, null = True)
    injection = models.IntegerField(verbose_name = "Injection", choices = _INJECTION, blank= True, null = True)
    adrenaline = models.IntegerField(verbose_name = "Adrenaline", choices = _NO_YES, blank= True, null = True)
    endocut = models.IntegerField(verbose_name = "Endocut/Blended", choices = _ENDOCUT, blank= True, null = True)
    electrosurgical_generator_model = models.CharField(verbose_name = "Electrosurgical generator model", max_length = 100, blank= True, null = True) #max_length?
    polyp_retrieval = models.IntegerField(verbose_name = "Polyp retrieval", choices = _POLYP_RETRIEVAL, blank= True, null = True)
    argon_PC = models.IntegerField(verbose_name = "Argon PC", choices = _ARGON_PC, blank= True, null = True)
    coagulation_forceps = models.IntegerField(verbose_name = "Coagulation forceps", choices = _NO_YES, blank= True, null = True)
    snare_tip_soft_coagulation = models.IntegerField(verbose_name = "Snare tip soft coagulation", choices = _NO_YES, blank= True, null = True)
    cs_cut_watts = models.IntegerField(verbose_name = "Cut (watts)", blank = True, null = True)
    cs_cut_mode = models.IntegerField(verbose_name = "Endocut mode", choices = _ENDOCUT_MODE, blank= True, null = True )
    cs_coagulation_watts = models.IntegerField(verbose_name = "Coagulation (watts)", blank = True, null = True)
    cs_coagulation_mode = models.IntegerField(verbose_name = "Coagulation mode", choices = _COAGULATION, blank= True, null = True )
    clips_control_group = models.IntegerField(verbose_name = "Clips control group", choices = _CLIPS_CONTROL, blank= True, null = True)
    clips_tratment_group = models.IntegerField(verbose_name = "Clips treatment group", choices = _CLIPS_TREAT_GROUP, blank= True, null = True)
    clips_n_lote = models.IntegerField(verbose_name = "Lot number", blank= True, null = True)
    clips_exp_date = models.DateField(verbose_name = "Expiration date", blank= True, null = True)
    not_tired_closure_by = models.IntegerField(verbose_name = "Closure not tried because of", choices = _NOT_TRIED, blank= True, null = True)
    closure_technique = models.IntegerField(verbose_name = "Closure technique", choices = _CLOSURE_TECHNIQUE, blank= True, null = True)
    number_clips_needed = models.IntegerField(verbose_name = "Number of clips needed", blank= True, null = True)
    perforation = models.IntegerField(verbose_name = "Perforation", choices = _PERFORATIOM, blank= True, null = True)
    surgery_from_endoscopy = models.IntegerField(verbose_name = "Surgery from endoscopy", choices = _NO_YES, blank= True, null = True) #Cadena?
    surgery_by_complication = models.IntegerField(verbose_name = "Surgery by complication", choices = _SURGERY_BY_COMPLICATION, blank= True, null = True)
    bleeding = models.IntegerField(verbose_name = "Bleeding", choices = _BLEEDING, blank= True, null = True)
    immediate_bleeding = models.IntegerField(verbose_name = "Immediate bleeding", choices = _IMMEDIATE_BLEEDING, blank= True, null = True)
    delayed_bleeding = models.IntegerField(verbose_name = "Delayed bleeding", choices = _NO_YES, blank= True, null = True)
    bleeding_treatment = models.IntegerField(verbose_name = "Bleeding treatment", choices = _BLEEDING_TREATMENT, blank= True, null = True)
    transfusion = models.IntegerField(verbose_name = "Transfusion", choices = _NO_YES, blank= True, null = True)
    pps = models.IntegerField(verbose_name = "Post polypectomy syndrome", choices = _NO_YES, blank= True, null = True) #PPS o Síndrome postpolipectomía?
    fever = models.IntegerField(verbose_name = "Fever", choices = _FEVER, blank= True, null = True)
    pain_requiring_medical_intervention = models.IntegerField(verbose_name = "Pain requiring medical intervantion", choices = _NO_YES, blank= True, null = True)
    hospital_stay_by_technique = models.IntegerField(verbose_name = "Hospital stay by technique", blank= True, null = True)
    hospital_stay_by_complication = models.IntegerField(verbose_name = "Hospital stay by complication", blank= True, null = True)
    follow_up_months = models.IntegerField(verbose_name = "Follow up months", blank= True, null = True)
    successful_treatment = models.IntegerField(verbose_name=" Successful treatment", choices = _SUCCESSFUL_TREATMENT, blank= True, null = True)
    sedation = models.IntegerField(verbose_name = "Sedation", choices = _SEDATION, blank= True, null = True)
    last_date_endoscopic_follow_up = models.DateField(verbose_name="Last date endoscopic follow up", blank= True, null = True)
    recurrence_three_six_months_control = models.IntegerField(verbose_name = "Recurrence 3-6 months control", choices = _RECURRENCE_THREE_SIX, blank= True, null = True)
    recurrenec_one_year_control = models.IntegerField(verbose_name = "Recurrence 1 year control", choices = _RECURRENCE_ONE_YEAR, blank= True, null = True)
    global_recurrence = models.IntegerField(verbose_name = "Global recurrence", choices = _NO_YES, blank= True, null = True)
    other_complications_comments = models.TextField(verbose_name = "Other complications comments", max_length = 500, blank = True, null = True)
    other_comments = models.TextField(verbose_name = "Other comments", max_length = 500, blank= True, null = True)



    def validate(request):
        user = UserProfile.objects.get(user = request.user)
        hospital = Hospital.objects.get(pk = user.hospital_id)
        study = Study.objects.get(pk = request.POST['study_id'])
        post = request.POST

        case = ClipsCase()
        case.study = study
        case.doctor = user
        case.hospital = hospital

        group = int_or_none(post['group'])
        age = int_or_none(post['age'])
        anticoagulants = int_or_none(post['anticoagulants'])
        asa = int_or_none(post['asa'])
        location = int_or_none(post['location'])
        size = int_or_none(post['maximum_size_mm'])
        study_id = int_or_none(post['study_id'])

        case.group = group
        case.age_interval = age
        case.location = location
        case.asa = asa
        case.anticoagulants = anticoagulants
        case.maximum_size_mm = size

        ids = TypeCase.get_case_ids(case)
        case.id_for_doctor = ids[0]
        case.id_for_hospital = ids[1]

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

        score = calculate_score(case)
        if score >= 4:
            case.save()
            return case.pk
        else:
            return None


#------------- EXTRA FOR Observational Study ---------

_COLONOSCOPY_INDICATION=(
    (1, 'Anemia/iron deficiency'),
    (2, 'CRC suspected'),
    (3, 'CRC screening program'),
    (4, 'Postpolypectomy surveillance'),
    (5, 'Relatives with CRC or polyposis'),
    (6, 'Polyposis'),
    (7, 'Other'),
    )

_COUNTRY = (
    (1, 'Spain'),
    (2, 'Japan'),
    (3, 'UK'),
    (4, 'USA'),
    (5, 'China'),
    )

_DEPTH = (
    (1, 'Mucosa'),
    (2, 'SM1'),
    (3, 'SM2'),
    (4, 'SM3'),
    (5, 'MP or deeper'),
    )

_BUDDING = (
    (0, 'No' ),
    (1, 'High grade'),
    )

_DEGREE_DIFFERENTIATION = (
    (1, 'Well'),
    (2, 'Moderate'),
    (3, 'Poorly'),
    )

_HISTOLOGICAL_VARIANTS = (
    (1,'Adenocarcinoma'),
    (2,'Mucinous'),
    (3,'Medullary'),
    (4,'Signet ring'),
    )

_FREE_MARGINS = (
    (1,'Nonassessable'),
    (2,'Free'),
    (3,'Affected')
    )

class ObservationalCase(TypeCase):

    date = models.DateField(verbose_name = "Date", blank= True, null = True)
    age = models.IntegerField(verbose_name = "Age", validators = [MinValueValidator(0)], blank= True, null = True)

    age_interval = models.IntegerField(verbose_name = "Age interval", choices = _TRAMOS_EDAD, blank= True, null = True) #nombre en español?
    sex = models.IntegerField(verbose_name = "Sex", choices = _SEX, blank= True, null = True)
    asa = models.IntegerField(verbose_name = "ASA", choices = _ASA , blank= True, null = True)
    hypertension = models.IntegerField(verbose_name = "Hypertension", choices = _NO_YES, blank= True, null = True)
    hb = models.FloatField(verbose_name = "HB (g/dL)", blank= True, null = True)
    platelets = models.IntegerField(verbose_name = "Platelets (x10⁹/L)", blank= True, null = True)
    inr = models.FloatField(verbose_name = "INR", blank= True, null = True) #max-min ?
    pt = models.IntegerField(verbose_name = "PT (s)", blank= True, null = True)   #max-min ?
    aspirin = models.IntegerField(verbose_name = "Aspirin", choices = _ASPIRIN, blank= True, null = True)
    anticoagulants = models.IntegerField(verbose_name = "Anticoagulants", choices = _ANTICOAGULANT, blank= True, null = True)
    heparinbridgetherapy = models.IntegerField(verbose_name = "Heparin Bridge Therapy", choices = _NO_YES, blank= True, null = True)
    nombre_p_activo_antiagreg_anticoag = models.CharField(verbose_name = "Active ingredients anticoagulant/antiagregant", max_length=128, blank= True, null = True)
    day_of_reintroduction_antiagregant = models.IntegerField(verbose_name = "Day of reintroduction anticoagulant/antiagregant", blank= True, null = True)
    paris_calif = models.IntegerField(verbose_name = "Paris Clasif.", choices = _PARIS, blank= True, null = True)
    lst_yn = models.IntegerField(verbose_name = "LST yn", choices= _NO_YES, blank= True, null = True)
    lst_morphology = models.IntegerField(verbose_name = "LST Morphology", choices = _MORPHOLOGY, blank= True, null = True)
    large_nodule_one_cm = models.IntegerField(verbose_name = "Large nodule 1cm", choices = _NO_YES, blank= True, null = True)
    demacrated_depressed_area = models.IntegerField(verbose_name = "Demacrated depressed area", choices = _NO_YES, blank= True, null = True)
    sclerous_wall_change = models.IntegerField(verbose_name = "Sclerous wall change", choices = _NO_YES, blank= True, null = True)
    fold_convergency = models.IntegerField(verbose_name = "Fold convergency", choices = _NO_YES, blank= True, null = True)
    chicken_skin_mucosa_around = models.IntegerField(verbose_name = "Chicken skin mucosa around", choices = _NO_YES, blank= True, null = True)
    maximum_size_mm = models.IntegerField(verbose_name="Maximum size (mm)", blank= True, null = True)
    area_square_cm = models.IntegerField(verbose_name = "Area (cm2)", blank= True, null = True)
    location = models.IntegerField(verbose_name = "Location", choices = _LOCATION, blank= True, null = True)
    ileocecal_valve_involvement = models.IntegerField(verbose_name = "Ileocecal valve involvement", choices =_NO_YES, blank= True, null = True)
    high_definition = models.IntegerField(verbose_name = "High definition", choices = _HIGH_DEFINITION, blank= True, null = True)
    endoscopemodel = models.CharField(verbose_name = "Endoscope model", max_length = 50, blank= True, null = True)
    nbi = models.IntegerField(verbose_name = "NBI", choices = _NO_YES, blank= True, null = True)
    nbi_sano = models.IntegerField(verbose_name = "NBI sano", choices = _NBI_SANO, blank= True, null = True) #nombre en español?
    nbi_nice = models.IntegerField(verbose_name = "NBI NICE", choices = _NBI_NICE, blank= True, null = True) #NICE son siglas?
    cromoendoscopy = models.IntegerField(verbose_name = "Cromoendoscopy", choices = _NO_YES, blank= True, null = True)
    kudo = models.IntegerField(verbose_name = "Kudo", choices = _KUDO, blank= True, null = True)
    prepathologic_endoscopic_diagnostic_a = models.IntegerField(verbose_name = "Prepathologic endoscopic diagnost 1", choices = _PED_A , blank= True, null = True)
    prepathologic_endoscopic_diagnostic_b = models.IntegerField(verbose_name = "Prepathologic endoscopic diagnost 2", choices = _PED_B , blank= True, null = True)
    correct_dx_adenoma_serrated = models.IntegerField(verbose_name = "Correct Dx Adenoma Serrated", choices = _NO_YES, blank= True, null = True)
    correct_dx_invasion = models.IntegerField(verbose_name = "Correct Dx Invasion", choices = _NO_YES, blank= True, null = True)
    histology = models.IntegerField(verbose_name = "Histology", choices = _HISTOLOGY, blank= True, null = True)
    histol_simplified = models.IntegerField(verbose_name = "Histology simplified", choices = _HISTOLOGY_SIMP, blank= True, null = True)
    time_of_procedure_in_mins = models.IntegerField(verbose_name = "Time of procedure (m)", blank= True, null = True)
    difficulty_of_emr = models.IntegerField(verbose_name = "Dificutly of EMR", choices = _DIFFICULTY, blank= True, null = True)
    accesibility = models.IntegerField(verbose_name = "Accesibility", choices = _DIFFICULTY, blank= True, null = True)
    resection = models.IntegerField(verbose_name = "Resection", choices = _RESECTION, blank= True, null = True)
    previous_biopsy = models.IntegerField(verbose_name = "Previous biopsy", choices = _NO_YES, blank= True, null = True)
    previous_attempt = models.IntegerField(verbose_name = "Previous attempt", choices = _NO_YES, blank= True, null = True)
    non_lifting_sign = models.IntegerField(verbose_name = "Non lifting sign", choices = _NO_YES, blank= True, null = True)
    technique = models.IntegerField(verbose_name = "Technique", choices = _TECHNIQUE, blank= True, null = True)
    technique_two  = models.IntegerField(verbose_name =" Technique 2", choices = _TECHNIQUE_TWO, blank= True, null = True)
    limit_marks = models.IntegerField(verbose_name = "Limit marks", choices = _MARKS, blank= True, null = True)
    injection = models.IntegerField(verbose_name = "Injection", choices = _INJECTION, blank= True, null = True)
    adrenaline = models.IntegerField(verbose_name = "Adrenaline", choices = _NO_YES, blank= True, null = True)
    endocut = models.IntegerField(verbose_name = "Endocut/Blended", choices = _ENDOCUT, blank= True, null = True)
    electrosurgical_generator_model = models.CharField(verbose_name = "Electrosurgical generator model", max_length = 100, blank= True, null = True) #max_length?
    polyp_retrieval = models.IntegerField(verbose_name = "Polyp retrieval", choices = _POLYP_RETRIEVAL, blank= True, null = True)
    argon_PC = models.IntegerField(verbose_name = "Argon PC", choices = _ARGON_PC, blank= True, null = True)
    coagulation_forceps = models.IntegerField(verbose_name = "Coagulation forceps", choices = _NO_YES, blank= True, null = True)
    snare_tip_soft_coagulation = models.IntegerField(verbose_name = "Snare tip soft coagulation", choices = _NO_YES, blank= True, null = True)
    cs_cut_watts = models.IntegerField(verbose_name = "Cut (watts)", blank = True, null = True)
    cs_cut_mode = models.IntegerField(verbose_name = "Endocut mode", choices = _ENDOCUT_MODE, blank= True, null = True )
    cs_coagulation_watts = models.IntegerField(verbose_name = "Coagulation (watts)", blank = True, null = True)
    cs_coagulation_mode = models.IntegerField(verbose_name = "Coagulation mode", choices = _COAGULATION, blank= True, null = True )
    clips_control_group = models.IntegerField(verbose_name = "Clips control group", choices = _CLIPS_CONTROL, blank= True, null = True)
    clips_tratment_group = models.IntegerField(verbose_name = "Clips treatment group", choices = _CLIPS_TREAT_GROUP, blank= True, null = True)
    clips_n_lote = models.IntegerField(verbose_name = "Lot number", blank= True, null = True)
    clips_exp_date = models.DateField(verbose_name = "Expiration date", blank= True, null = True)
    not_tired_closure_by = models.IntegerField(verbose_name = "Closure not tried because of", choices = _NOT_TRIED, blank= True, null = True)
    closure_technique = models.IntegerField(verbose_name = "Closure technique", choices = _CLOSURE_TECHNIQUE, blank= True, null = True)
    number_clips_needed = models.IntegerField(verbose_name = "Number of clips needed", blank= True, null = True)
    perforation = models.IntegerField(verbose_name = "Perforation", choices = _PERFORATIOM, blank= True, null = True)
    surgery_from_endoscopy = models.IntegerField(verbose_name = "Surgery from endoscopy", choices = _NO_YES, blank= True, null = True) #Cadena?
    surgery_by_complication = models.IntegerField(verbose_name = "Surgery by complication", choices = _SURGERY_BY_COMPLICATION, blank= True, null = True)
    bleeding = models.IntegerField(verbose_name = "Bleeding", choices = _BLEEDING, blank= True, null = True)
    immediate_bleeding = models.IntegerField(verbose_name = "Immediate bleeding", choices = _IMMEDIATE_BLEEDING, blank= True, null = True)
    delayed_bleeding = models.IntegerField(verbose_name = "Delayed bleeding", choices = _NO_YES, blank= True, null = True)
    bleeding_treatment = models.IntegerField(verbose_name = "Bleeding treatment", choices = _BLEEDING_TREATMENT, blank= True, null = True)
    transfusion = models.IntegerField(verbose_name = "Transfusion", choices = _NO_YES, blank= True, null = True)
    pps = models.IntegerField(verbose_name = "Post polypectomy syndrome", choices = _NO_YES, blank= True, null = True) #PPS o Síndrome postpolipectomía?
    fever = models.IntegerField(verbose_name = "Fever", choices = _FEVER, blank= True, null = True)
    pain_requiring_medical_intervention = models.IntegerField(verbose_name = "Pain requiring medical intervantion", choices = _NO_YES, blank= True, null = True)
    hospital_stay_by_technique = models.IntegerField(verbose_name = "Hospital stay by technique", blank= True, null = True)
    hospital_stay_by_complication = models.IntegerField(verbose_name = "Hospital stay by complication", blank= True, null = True)
    follow_up_months = models.IntegerField(verbose_name = "Follow up months", blank= True, null = True)
    successful_treatment = models.IntegerField(verbose_name=" Successful treatment", choices = _SUCCESSFUL_TREATMENT, blank= True, null = True)
    sedation = models.IntegerField(verbose_name = "Sedation", choices = _SEDATION, blank= True, null = True)
    last_date_endoscopic_follow_up = models.DateField(verbose_name="Last date endoscopic follow up", blank= True, null = True)
    recurrence_three_six_months_control = models.IntegerField(verbose_name = "Recurrence 3-6 months control", choices = _RECURRENCE_THREE_SIX, blank= True, null = True)
    recurrenec_one_year_control = models.IntegerField(verbose_name = "Recurrence 1 year control", choices = _RECURRENCE_ONE_YEAR, blank= True, null = True)
    global_recurrence = models.IntegerField(verbose_name = "Global recurrence", choices = _NO_YES, blank= True, null = True)
    other_complications_comments = models.TextField(verbose_name = "Other complications comments", max_length = 500, blank = True, null = True)
    other_comments = models.TextField(verbose_name = "Other comments", max_length = 500, blank= True, null = True)

    #variables specifics to observatory
    colonoscopy_indication = models.IntegerField(verbose_name = "Colonoscopy indication", choices = _COLONOSCOPY_INDICATION , blank= True, null = True)
    country = models.IntegerField(verbose_name = "Country", choices = _COUNTRY , blank= True, null = True)
    depth = models.IntegerField(verbose_name = "Depth", choices = _DEPTH , blank= True, null = True)
    depth_sm_invasion = models.FloatField(verbose_name="Depth (Sm invasion: µ)", blank=True, null=True)
    lymphatic_invasion = models.IntegerField(verbose_name="Lymphatic invasion", choices = _NO_YES, blank=True, null=True)
    vascular_invasion = models.IntegerField(verbose_name="Vascular invasion", choices = _NO_YES, blank=True, null=True)
    perineural_invasion = models.IntegerField(verbose_name="Perineural invasion", choices = _NO_YES, blank=True, null=True)
    budding = models.IntegerField(verbose_name="Budding", choices= _BUDDING, blank=True, null=True)
    degree_differentiation = models.IntegerField(verbose_name="Degree differentiation", choices= _DEGREE_DIFFERENTIATION, blank=True, null=True)
    histological_variants = models.IntegerField(verbose_name="Histological variants", choices= _HISTOLOGICAL_VARIANTS, blank=True, null=True)
    free_vertical_margins =  models.IntegerField(verbose_name="Free vertical margins (>1mm)", choices= _FREE_MARGINS, blank=True, null=True)
    free_horizontal_margins =  models.IntegerField(verbose_name="Free horizontal margin (>1mm)", choices= _FREE_MARGINS, blank=True, null=True)

    def validate(request):
        user = UserProfile.objects.get(user = request.user)
        hospital = Hospital.objects.get(pk = user.hospital_id)

        post = request.POST
        study = Study.objects.get(pk = post['study_id'])
        group = int_or_none(post['group'])

        case = ObservationalCase()
        case.study = study
        case.hospital = hospital
        case.doctor = user
        case.group = group

        ids = TypeCase.get_case_ids(case)
        case.id_for_doctor = ids[0]
        case.id_for_hospital = ids[1]
        try:
            case.save()
            return case.pk
        except:
            return None


class ObsinternationalCase(TypeCase):

    date = models.DateField(verbose_name = "Date", blank= True, null = True)
    age = models.IntegerField(verbose_name = "Age", validators = [MinValueValidator(0)], blank= True, null = True)

    age_interval = models.IntegerField(verbose_name = "Age interval", choices = _TRAMOS_EDAD, blank= True, null = True) #nombre en español?
    sex = models.IntegerField(verbose_name = "Sex", choices = _SEX, blank= True, null = True)
    asa = models.IntegerField(verbose_name = "ASA", choices = _ASA , blank= True, null = True)
    hypertension = models.IntegerField(verbose_name = "Hypertension", choices = _NO_YES, blank= True, null = True)
    hb = models.FloatField(verbose_name = "HB (g/dL)", blank= True, null = True)
    platelets = models.IntegerField(verbose_name = "Platelets (x10⁹/L)", blank= True, null = True)
    inr = models.FloatField(verbose_name = "INR", blank= True, null = True) #max-min ?
    pt = models.IntegerField(verbose_name = "PT (s)", blank= True, null = True)   #max-min ?
    aspirin = models.IntegerField(verbose_name = "Aspirin", choices = _ASPIRIN, blank= True, null = True)
    anticoagulants = models.IntegerField(verbose_name = "Anticoagulants", choices = _ANTICOAGULANT, blank= True, null = True)
    heparinbridgetherapy = models.IntegerField(verbose_name = "Heparin Bridge Therapy", choices = _NO_YES, blank= True, null = True)
    nombre_p_activo_antiagreg_anticoag = models.CharField(verbose_name = "Active ingredients anticoagulant/antiagregant", max_length=128, blank= True, null = True)
    day_of_reintroduction_antiagregant = models.IntegerField(verbose_name = "Day of reintroduction anticoagulant/antiagregant", blank= True, null = True)
    paris_calif = models.IntegerField(verbose_name = "Paris Clasif.", choices = _PARIS, blank= True, null = True)
    lst_yn = models.IntegerField(verbose_name = "LST yn", choices= _NO_YES, blank= True, null = True)
    lst_morphology = models.IntegerField(verbose_name = "LST Morphology", choices = _MORPHOLOGY, blank= True, null = True)
    large_nodule_one_cm = models.IntegerField(verbose_name = "Large nodule 1cm", choices = _NO_YES, blank= True, null = True)
    demacrated_depressed_area = models.IntegerField(verbose_name = "Demacrated depressed area", choices = _NO_YES, blank= True, null = True)
    sclerous_wall_change = models.IntegerField(verbose_name = "Sclerous wall change", choices = _NO_YES, blank= True, null = True)
    fold_convergency = models.IntegerField(verbose_name = "Fold convergency", choices = _NO_YES, blank= True, null = True)
    chicken_skin_mucosa_around = models.IntegerField(verbose_name = "Chicken skin mucosa around", choices = _NO_YES, blank= True, null = True)
    maximum_size_mm = models.IntegerField(verbose_name="Maximum size (mm)", blank= True, null = True)
    area_square_cm = models.IntegerField(verbose_name = "Area (cm2)", blank= True, null = True)
    location = models.IntegerField(verbose_name = "Location", choices = _LOCATION, blank= True, null = True)
    ileocecal_valve_involvement = models.IntegerField(verbose_name = "Ileocecal valve involvement", choices =_NO_YES, blank= True, null = True)
    high_definition = models.IntegerField(verbose_name = "High definition", choices = _HIGH_DEFINITION, blank= True, null = True)
    endoscopemodel = models.CharField(verbose_name = "Endoscope model", max_length = 50, blank= True, null = True)
    nbi = models.IntegerField(verbose_name = "NBI", choices = _NO_YES, blank= True, null = True)
    nbi_sano = models.IntegerField(verbose_name = "NBI sano", choices = _NBI_SANO, blank= True, null = True) #nombre en español?
    nbi_nice = models.IntegerField(verbose_name = "NBI NICE", choices = _NBI_NICE, blank= True, null = True) #NICE son siglas?
    cromoendoscopy = models.IntegerField(verbose_name = "Cromoendoscopy", choices = _NO_YES, blank= True, null = True)
    kudo = models.IntegerField(verbose_name = "Kudo", choices = _KUDO, blank= True, null = True)
    prepathologic_endoscopic_diagnostic_a = models.IntegerField(verbose_name = "Prepathologic endoscopic diagnost 1", choices = _PED_A , blank= True, null = True)
    prepathologic_endoscopic_diagnostic_b = models.IntegerField(verbose_name = "Prepathologic endoscopic diagnost 2", choices = _PED_B , blank= True, null = True)
    correct_dx_adenoma_serrated = models.IntegerField(verbose_name = "Correct Dx Adenoma Serrated", choices = _NO_YES, blank= True, null = True)
    correct_dx_invasion = models.IntegerField(verbose_name = "Correct Dx Invasion", choices = _NO_YES, blank= True, null = True)
    histology = models.IntegerField(verbose_name = "Histology", choices = _HISTOLOGY, blank= True, null = True)
    histol_simplified = models.IntegerField(verbose_name = "Histology simplified", choices = _HISTOLOGY_SIMP, blank= True, null = True)
    time_of_procedure_in_mins = models.IntegerField(verbose_name = "Time of procedure (m)", blank= True, null = True)
    difficulty_of_emr = models.IntegerField(verbose_name = "Dificutly of EMR", choices = _DIFFICULTY, blank= True, null = True)
    accesibility = models.IntegerField(verbose_name = "Accesibility", choices = _DIFFICULTY, blank= True, null = True)
    resection = models.IntegerField(verbose_name = "Resection", choices = _RESECTION, blank= True, null = True)
    previous_biopsy = models.IntegerField(verbose_name = "Previous biopsy", choices = _NO_YES, blank= True, null = True)
    previous_attempt = models.IntegerField(verbose_name = "Previous attempt", choices = _NO_YES, blank= True, null = True)
    non_lifting_sign = models.IntegerField(verbose_name = "Non lifting sign", choices = _NO_YES, blank= True, null = True)
    technique = models.IntegerField(verbose_name = "Technique", choices = _TECHNIQUE, blank= True, null = True)
    technique_two  = models.IntegerField(verbose_name =" Technique 2", choices = _TECHNIQUE_TWO, blank= True, null = True)
    limit_marks = models.IntegerField(verbose_name = "Limit marks", choices = _MARKS, blank= True, null = True)
    injection = models.IntegerField(verbose_name = "Injection", choices = _INJECTION, blank= True, null = True)
    adrenaline = models.IntegerField(verbose_name = "Adrenaline", choices = _NO_YES, blank= True, null = True)
    endocut = models.IntegerField(verbose_name = "Endocut/Blended", choices = _ENDOCUT, blank= True, null = True)
    electrosurgical_generator_model = models.CharField(verbose_name = "Electrosurgical generator model", max_length = 100, blank= True, null = True) #max_length?
    polyp_retrieval = models.IntegerField(verbose_name = "Polyp retrieval", choices = _POLYP_RETRIEVAL, blank= True, null = True)
    argon_PC = models.IntegerField(verbose_name = "Argon PC", choices = _ARGON_PC, blank= True, null = True)
    coagulation_forceps = models.IntegerField(verbose_name = "Coagulation forceps", choices = _NO_YES, blank= True, null = True)
    snare_tip_soft_coagulation = models.IntegerField(verbose_name = "Snare tip soft coagulation", choices = _NO_YES, blank= True, null = True)
    cs_cut_watts = models.IntegerField(verbose_name = "Cut (watts)", blank = True, null = True)
    cs_cut_mode = models.IntegerField(verbose_name = "Endocut mode", choices = _ENDOCUT_MODE, blank= True, null = True )
    cs_coagulation_watts = models.IntegerField(verbose_name = "Coagulation (watts)", blank = True, null = True)
    cs_coagulation_mode = models.IntegerField(verbose_name = "Coagulation mode", choices = _COAGULATION, blank= True, null = True )
    clips_control_group = models.IntegerField(verbose_name = "Clips control group", choices = _CLIPS_CONTROL, blank= True, null = True)
    clips_tratment_group = models.IntegerField(verbose_name = "Clips treatment group", choices = _CLIPS_TREAT_GROUP, blank= True, null = True)
    clips_n_lote = models.IntegerField(verbose_name = "Lot number", blank= True, null = True)
    clips_exp_date = models.DateField(verbose_name = "Expiration date", blank= True, null = True)
    not_tired_closure_by = models.IntegerField(verbose_name = "Closure not tried because of", choices = _NOT_TRIED, blank= True, null = True)
    closure_technique = models.IntegerField(verbose_name = "Closure technique", choices = _CLOSURE_TECHNIQUE, blank= True, null = True)
    number_clips_needed = models.IntegerField(verbose_name = "Number of clips needed", blank= True, null = True)
    perforation = models.IntegerField(verbose_name = "Perforation", choices = _PERFORATIOM, blank= True, null = True)
    surgery_from_endoscopy = models.IntegerField(verbose_name = "Surgery from endoscopy", choices = _NO_YES, blank= True, null = True) #Cadena?
    surgery_by_complication = models.IntegerField(verbose_name = "Surgery by complication", choices = _SURGERY_BY_COMPLICATION, blank= True, null = True)
    bleeding = models.IntegerField(verbose_name = "Bleeding", choices = _BLEEDING, blank= True, null = True)
    immediate_bleeding = models.IntegerField(verbose_name = "Immediate bleeding", choices = _IMMEDIATE_BLEEDING, blank= True, null = True)
    delayed_bleeding = models.IntegerField(verbose_name = "Delayed bleeding", choices = _NO_YES, blank= True, null = True)
    bleeding_treatment = models.IntegerField(verbose_name = "Bleeding treatment", choices = _BLEEDING_TREATMENT, blank= True, null = True)
    transfusion = models.IntegerField(verbose_name = "Transfusion", choices = _NO_YES, blank= True, null = True)
    pps = models.IntegerField(verbose_name = "Post polypectomy syndrome", choices = _NO_YES, blank= True, null = True) #PPS o Síndrome postpolipectomía?
    fever = models.IntegerField(verbose_name = "Fever", choices = _FEVER, blank= True, null = True)
    pain_requiring_medical_intervention = models.IntegerField(verbose_name = "Pain requiring medical intervantion", choices = _NO_YES, blank= True, null = True)
    hospital_stay_by_technique = models.IntegerField(verbose_name = "Hospital stay by technique", blank= True, null = True)
    hospital_stay_by_complication = models.IntegerField(verbose_name = "Hospital stay by complication", blank= True, null = True)
    follow_up_months = models.IntegerField(verbose_name = "Follow up months", blank= True, null = True)
    successful_treatment = models.IntegerField(verbose_name=" Successful treatment", choices = _SUCCESSFUL_TREATMENT, blank= True, null = True)
    sedation = models.IntegerField(verbose_name = "Sedation", choices = _SEDATION, blank= True, null = True)
    last_date_endoscopic_follow_up = models.DateField(verbose_name="Last date endoscopic follow up", blank= True, null = True)
    recurrence_three_six_months_control = models.IntegerField(verbose_name = "Recurrence 3-6 months control", choices = _RECURRENCE_THREE_SIX, blank= True, null = True)
    recurrenec_one_year_control = models.IntegerField(verbose_name = "Recurrence 1 year control", choices = _RECURRENCE_ONE_YEAR, blank= True, null = True)
    global_recurrence = models.IntegerField(verbose_name = "Global recurrence", choices = _NO_YES, blank= True, null = True)
    other_complications_comments = models.TextField(verbose_name = "Other complications comments", max_length = 500, blank = True, null = True)
    other_comments = models.TextField(verbose_name = "Other comments", max_length = 500, blank= True, null = True)

    #variables specifics to observatory
    colonoscopy_indication = models.IntegerField(verbose_name = "Colonoscopy indication", choices = _COLONOSCOPY_INDICATION , blank= True, null = True)
    country = models.IntegerField(verbose_name = "Country", choices = _COUNTRY , blank= True, null = True)
    depth = models.IntegerField(verbose_name = "Depth", choices = _DEPTH , blank= True, null = True)
    depth_sm_invasion = models.FloatField(verbose_name="Depth (Sm invasion: µ)", blank=True, null=True)
    lymphatic_invasion = models.IntegerField(verbose_name="Lymphatic invasion", choices = _NO_YES, blank=True, null=True)
    vascular_invasion = models.IntegerField(verbose_name="Vascular invasion", choices = _NO_YES, blank=True, null=True)
    perineural_invasion = models.IntegerField(verbose_name="Perineural invasion", choices = _NO_YES, blank=True, null=True)
    budding = models.IntegerField(verbose_name="Budding", choices= _BUDDING, blank=True, null=True)
    degree_differentiation = models.IntegerField(verbose_name="Degree differentiation", choices= _DEGREE_DIFFERENTIATION, blank=True, null=True)
    histological_variants = models.IntegerField(verbose_name="Histological variants", choices= _HISTOLOGICAL_VARIANTS, blank=True, null=True)
    free_vertical_margins =  models.IntegerField(verbose_name="Free vertical margins (>1mm)", choices= _FREE_MARGINS, blank=True, null=True)
    free_horizontal_margins =  models.IntegerField(verbose_name="Free horizontal margin (>1mm)", choices= _FREE_MARGINS, blank=True, null=True)

    def validate(request):
        user = UserProfile.objects.get(user = request.user)
        hospital = Hospital.objects.get(pk = user.hospital_id)

        post = request.POST
        study = Study.objects.get(pk = post['study_id'])
        group = int_or_none(post['group'])

        case = ObsinternationalCase()
        case.study = study
        case.hospital = hospital
        case.doctor = user
        case.group = group

        ids = TypeCase.get_case_ids(case)
        case.id_for_doctor = ids[0]
        case.id_for_hospital = ids[1]
        try:
            case.save()
            return case.pk
        except:
            return None

#Example of a simple case type
class CancerCase(TypeCase):
    organ = models.CharField(max_length=16)

    def validate(request):
        user = UserProfile.objects.get(user = request.user)
        hospital = Hospital.objects.get(pk = user.hospital_id)

        post = request.POST
        study = Study.objects.get(pk = post['study_id'])
        group = int_or_none(post['group'])

        case = CancerCase()
        case.study = study
        case.hospital = hospital
        case.doctor = user
        case.group = group

        ids = TypeCase.get_case_ids(case)
        case.id_for_doctor = ids[0]
        case.id_for_hospital = ids[1]
        try:
            case.save()
            return case.pk
        except:
            return None
