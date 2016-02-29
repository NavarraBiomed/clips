from django.contrib import admin
from django import forms
from django.db import models
# Register your models here.

from .models import Study, Hospital

class StudyAdmin(admin.ModelAdmin):
	
	formfield_overrides = {
		models.IntegerField: {'widget': forms.NumberInput},
    }
    
	fieldsets = (
		('Hospital info', {
		'fields': (
			'hospital',
			'doctor'
			)
		}),
		('Patient info', {
		'fields': (
			('name', 'id_number'),
			('sex', 'age', 'age_interval'),
			)
		}),
		('Group 1', {
		'classes': ('suit-tab', 'suit-tab-general',),
		'fields': (
			'date',
			('asa', 'hypertension', 'hb'),
			'platelets',
			'inr',
			'pt',
			('aspirin', 'anticoagulants', 'antiplatelet_anticoagulant'),
			('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
			'day_of_reintroduction_antiagregant',
			'paris_calif',
			('lst_yn','lst_morphology'),
			'large_nodule_one_cm',
			'demacrated_depressed_area',
			'sclerous_wall_change',
			'fold_convergency',
			'chicken_skin_mucosa_around',	
			)

		}),
		('Group 2', {
		'fields': (
			('maximum_size_mm', 'area_square_cm'),	
			'location',
			'ileocecal_valve_involvement',
			'high_definition',
			'endoscopemodel',
			('nbi', 'nbi_sano', 'nbi_nice'),
			'cromoendoscopy',
			'kudo',
			('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
			('correct_dx_adenoma_serrated','correct_dx_invasion'),
			)
		}),
		('Group 3', {
		'fields': (
			('histology', 'histol_simplified'),
			'time_of_procedure_in_mins',
			'difficulty_of_emr',
			('accesibility', 'resection', 'resection_yn'),
			('previous_biopsy', 'previous_attempt'),
			'non_lifting_sign',
			('technique','technique_two'),
			'limit_marks',
			('injection', 'adrenaline'),
			'endocut',
			'electrosurgical_generator_model',
			'polyp_retrieval',
			('argon_PC', 'argon_coagulacion', 'coagulation_forceps' ),
			)
		}),
		('Group 4', {
		'fields': (
			('clips', 'clips_control_group', 'clips_tratment_group'),
			('not_tired_closure_by', 'closure_technique'),
			'number_clips_needed',
			)
		}),
		('Group 5', {
		'fields': (
			'perforation',
			('surgery_from_endoscopy', 'surgery_by_complication'),
			('bleeding', 'immediate_bleeding', 'delayed_bleeding', 'bleeding_treatment'),
			'transfusion'
			)
		}),
		('Group 6', {
		'fields': (
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
			'sedation',
			'last_date_endoscopic_follow_up',
			('recurrence_three_six_months_control', 'recurrenec_one_year_control', 'global_recurrence'),

			)
		}),
		('Additional Info', {
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
admin.site.register(Study, StudyAdmin)