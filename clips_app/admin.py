from django.contrib import admin
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


from .models import Case, Study, Hospital, UserProfile

class CaseAdmin(admin.ModelAdmin):
	
	formfield_overrides = {
		models.IntegerField: {'widget': forms.NumberInput},
    }


    
	fieldsets = (
		('Hospital info', {
		'fields': (
			('study',),
			('clips',),
			('hospital',),
			('doctor',),
			('id_for_hospital', 'id_for_doctor')
			)
		}),
		('Patient info', {
		'fields': (
			('sex', 'age', 'age_interval'),
			'date',
			('asa', 'hypertension', 'hb'),
			'platelets',
			'inr',
			'pt',
			('aspirin', 'anticoagulants'),
			('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
			'day_of_reintroduction_antiagregant',
			)
		}),
		('Polyp characteristics', {
		'classes': ('suit-tab', 'suit-tab-general',),
		'fields': (			
			'paris_calif',
			('lst_yn','lst_morphology'),
			'large_nodule_one_cm',
			'demacrated_depressed_area',
			'sclerous_wall_change',
			'fold_convergency',
			'chicken_skin_mucosa_around',	
			('maximum_size_mm', 'area_square_cm'),	
			'location',
			'ileocecal_valve_involvement',
			)

		}),
		('Technical considerations', {
		'fields': (			
			'high_definition',
			'endoscopemodel',
			('nbi', 'nbi_sano', 'nbi_nice'),
			'sedation',
			'cromoendoscopy',
			'kudo',
			('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
			('correct_dx_adenoma_serrated','correct_dx_invasion'),
			('histology', 'histol_simplified'),
			'time_of_procedure_in_mins',
			'difficulty_of_emr',
			('accesibility', 'resection'),
			('previous_biopsy', 'previous_attempt'),
			'non_lifting_sign',
			('technique','technique_two'),
			'limit_marks',
			('injection', 'adrenaline'),
			'endocut',
			'electrosurgical_generator_model',
			'polyp_retrieval',
			('argon_PC'),
			('snare_tip_soft_coagulation', 'coagulation_forceps' )
			)
		}),
		('Cautering settings', {
		'fields': (
			('cs_cut_watts', 'cs_cut_mode'),
			('cs_coagulation_watts', 'cs_coagulation_mode' )
			)
		}),
		('Profilactic measures', {
		'fields': (
			('clips_control_group', 'clips_tratment_group'),
			('not_tired_closure_by', 'closure_technique'),
			'number_clips_needed',
			('clips_n_lote', 'clips_exp_date')
			)
		}),
		('Complications', {
		'fields': (
			'perforation',
			('surgery_from_endoscopy', 'surgery_by_complication'),
			('bleeding', 'immediate_bleeding', 'delayed_bleeding', 'bleeding_treatment'),
			'transfusion',
			'pps',
			'fever',
			'pain_requiring_medical_intervention',
			('hospital_stay_by_technique', 'hospital_stay_by_complication'),
			)
		}),
		('Follow up', {
		'fields': (
			'follow_up_months',
			'successful_treatment',			
			'last_date_endoscopic_follow_up',
			('recurrence_three_six_months_control', 'recurrenec_one_year_control', 'global_recurrence'),

			)
		}),
		('Additional info', {
		'fields': (
			'other_complications_comments',
			'other_comments',
			)
		}),                 	
	)

	suit_form_tabs = (
		('general', 'General'),
		('treatment', 'Treatment'),
		('follow_up', 'Follow up')
                 )
admin.site.register(Hospital)
admin.site.register(Study)
admin.site.register(Case, CaseAdmin)

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.register(User, UserProfileAdmin)
