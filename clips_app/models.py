from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



_SEX = (
	(1, "Man"),
	(2, "Woman")
	)

_TRAMOS_EDAD = (
	(1, "<= 60"),
	(2, "67-74"),
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
	(4, "Debigatran (new antic)")
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
	(1, "Conventinoal endoscope"),
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
	(1, "adenoma"),
	(2, "HGD-Imucosal"),
	(3, "Invasive"),
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
	(1, "PAC marks")
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
	(3, "Endocut")
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

_CLIPS = (
	(0, "Control group"),
	(1, "Yes")
	)
 
_CLIPS_CONTROL = (
	(0, "No"),
	(1, "Punctual coagulation")
	)

_CLIPS_TREAT_GROUP = (
	(1, "Complete closure with complete mucosal apposition"),
	(2, "Complee closure without complete mucosal apposition"),
	(3, "Total failed closure"),
	(4, "Partial failed closure"),
	(5, "Not tired closure")
	)

_NO_TIRED = (
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
	(1, "During exploration with clinical impact"),
	(2, "24h"),
	(3, "24-48h"),
	(4, "3-7 days"),
	(5, ">7 days"),
	(6, "During no clinical impact-autol")
	)

_IMMEDIATE_BLEEDING = (
	(0, "No"),
	(1, "Yes: during expliration with clinical impact")
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
	(1, "Yes: endoscopic treatment"),
	(2, "Yes: surgical treatment needed"),
	(3, "Lost"),
	(4, "Pendiente control"),
	(5, "Rechaza / No seguimiento")
	)

class Hospital(models.Model):
	name = models.CharField(verbose_name = "Name", max_length = 100)

	def __str__(self):
		return self.name

class Study(models.Model):
	class Meta:
		verbose_name_plural = "Studies"

	hospital = models.ForeignKey('Hospital', default = None , blank= True, null = True)
	doctor = models.IntegerField(verbose_name = "Doctor", blank= True, null = True)
	date = models.DateField(verbose_name = "Date", blank= True, null = True)
	name = models.CharField(verbose_name = "Name", max_length = 2, blank= True, null = True)
	id_number = models.CharField(verbose_name = "ID Number", max_length = 10, blank= True, null = True) #length?
	age = models.IntegerField(verbose_name = "Age", validators = [MinValueValidator(0)], blank= True, null = True)
	age_interval = models.CharField(verbose_name = "Age interval", choices = _TRAMOS_EDAD, max_length = 2, blank= True, null = True) #nombre en español?
	sex = models.CharField(verbose_name = "Sex", choices = _SEX, max_length = 1, blank= True, null = True)
	asa = models.IntegerField(verbose_name = "ASA", choices = _ASA , blank= True, null = True)
	hypertension = models.IntegerField(verbose_name = "Hypertension", choices = _NO_YES, blank= True, null = True) 
	hb = models.IntegerField(verbose_name = "HB", blank= True, null = True)
	platelets = models.IntegerField(verbose_name = "Platelets", blank= True, null = True)
	inr = models.IntegerField(verbose_name = "INR", blank= True, null = True) #max-min ?
	pt = models.IntegerField(verbose_name = "PT", blank= True, null = True)   #max-min ?
	aspirin = models.IntegerField(verbose_name = "Aspirin", choices = _ASPIRIN, blank= True, null = True)
	anticoagulants = models.IntegerField(verbose_name = "Anticoagulants", choices = _ANTICOAGULANT, blank= True, null = True)
	antiplatelet_anticoagulant = models.IntegerField(verbose_name = "Antiplatelet anticoagulant", choices = _ANTIPLATELET, blank= True, null = True)
	heparinbridgetherapy = models.IntegerField(verbose_name = "Heparin Bridge Therapy", choices = _NO_YES, blank= True, null = True)
	nombre_p_activo_antiagreg_anticoag = models.IntegerField(verbose_name = "Nombre p. activo antiagregante...", blank= True, null = True) #nombre en español, está cotado
	day_of_reintroduction_antiagregant = models.IntegerField(verbose_name = "Day of reintroduction antiagregant", blank= True, null = True) #nombre?
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
	time_of_procedure_in_mins = models.IntegerField(verbose_name = "Time of procedure (s, blank= True, null = True)", blank= True, null = True)
	difficulty_of_emr = models.IntegerField(verbose_name = "Dificutly of EMR", choices = _DIFFICULTY, blank= True, null = True)
	accesibility = models.IntegerField(verbose_name = "Accesibility", choices = _DIFFICULTY, blank= True, null = True)
	resection = models.IntegerField(verbose_name = "Resection", choices = _RESECTION, blank= True, null = True)
	resection_yn = models.IntegerField(verbose_name = "Resection YN", choices = _RESECTION_YN, blank= True, null = True)
	previous_biopsy = models.IntegerField(verbose_name = "Previous biopsy", choices = _NO_YES, blank= True, null = True)
	previous_attempt = models.IntegerField(verbose_name = "Previous attempt", choices = _NO_YES, blank= True, null = True)
	non_lifting_sign = models.IntegerField(verbose_name = "Non lifting sign", choices = _NO_YES, blank= True, null = True)
	technique = models.IntegerField(verbose_name = "Technique", choices = _TECHNIQUE, blank= True, null = True)
	technique_two  = models.IntegerField(verbose_name =" Technique 2", choices = _TECHNIQUE_TWO, blank= True, null = True)
	limit_marks = models.IntegerField(verbose_name = "Limit marks", choices = _MARKS, blank= True, null = True)
	injection = models.IntegerField(verbose_name = "Injection", choices = _INJECTION, blank= True, null = True)
	adrenaline = models.IntegerField(verbose_name = "Adrenaline", choices = _NO_YES, blank= True, null = True)
	endocut = models.IntegerField(verbose_name = "Endocut", choices = _ENDOCUT, blank= True, null = True)
	electrosurgical_generator_model = models.CharField(verbose_name = "Electrosurgical generator model", max_length = 100, blank= True, null = True) #max_length?
	polyp_retrieval = models.IntegerField(verbose_name = "Polyp retrieval", choices = _POLYP_RETRIEVAL, blank= True, null = True)
	argon_PC = models.IntegerField(verbose_name = "Argon PC", choices = _ARGON_PC, blank= True, null = True)
	argon_coagulacion = models.IntegerField(verbose_name = "Argón Coagulación", choices = _NO_YES, blank= True, null = True) #nombre en español?
	coagulation_forceps = models.IntegerField(verbose_name = "Coagulation forceps", choices = _NO_YES, blank= True, null = True)
	clips = models.IntegerField(verbose_name = "Clips", choices = _CLIPS, blank= True, null = True)
	clips_control_group = models.IntegerField(verbose_name = "Clips control group", choices = _CLIPS_CONTROL, blank= True, null = True)
	clips_tratment_group = models.IntegerField(verbose_name = "Clips treatment group", choices = _CLIPS_TREAT_GROUP, blank= True, null = True)
	not_tired_closure_by = models.IntegerField(verbose_name = "Not tired closure by", choices = _NO_TIRED, blank= True, null = True)
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
	pps = models.IntegerField(verbose_name = "PPS", choices = _NO_YES, blank= True, null = True) #PPS o Síndrome postpolipectomía?
	fever = models.IntegerField(verbose_name = "Fever", choices = _FEVER, blank= True, null = True)
	pain_requiring_medical_intervention = models.IntegerField(verbose_name = "Pain requiring medical intervantion", blank= True, null = True)
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