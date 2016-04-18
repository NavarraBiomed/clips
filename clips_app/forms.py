from django import forms
from material import *
from .models import *
import clips_app
from django.views.generic import *
from django.views.generic.edit import FormView

class CaseForm(forms.ModelForm): 
	#, LayoutMixin, View

    class Meta:
        model = Case
        exclude = ('id_for_doctor', 'id_for_hospital')
        #fields = ('name', 'clips', 'id_number', 'sex', 'study', 'doctor', 'date')
    
    layout = Layout(
    				Row('study', 'clips'),
    				Row('hospital', 'doctor'),
                    Fieldset('Patient info',
                             Row('sex', 'age', 'age_interval'),
                             'date',
                             Row('asa', 'hypertension', 'hb'),
                             'platelets',
							'inr',
							'pt',
							Row('aspirin', 'anticoagulants', 'antiplatelet_anticoagulant'),
							Row('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
							'day_of_reintroduction_antiagregant',
                    ),
                    Fieldset('Polyp characteristics',
                    	'paris_calif',
						Row('lst_yn','lst_morphology'),
						'large_nodule_one_cm',
						'demacrated_depressed_area',
						'sclerous_wall_change',
						'fold_convergency',
						'chicken_skin_mucosa_around',	
						Row('maximum_size_mm', 'area_square_cm'),	
						'location',
						'ileocecal_valve_involvement',
                   	),
                   	Fieldset('Technical considerations',
                   		'high_definition',
						'endoscopemodel',
						Row('nbi', 'nbi_sano', 'nbi_nice'),
						'sedation',
						'cromoendoscopy',
						'kudo',
						Row('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
						Row('correct_dx_adenoma_serrated','correct_dx_invasion'),
						Row('histology', 'histol_simplified'),
						'time_of_procedure_in_mins',
						'difficulty_of_emr',
						Row('accesibility', 'resection', 'resection_yn'),
						Row('previous_biopsy', 'previous_attempt'),
						'non_lifting_sign',
						Row('technique','technique_two'),
						'limit_marks',
						Row('injection', 'adrenaline'),
						'endocut',
						'electrosurgical_generator_model',
						'polyp_retrieval',
						Row('argon_PC', 'argon_coagulacion'),
						Row('snare_tip_soft_coagulation', 'coagulation_forceps' )
                   	),
                   	Fieldset('Cautering settings',
                   		Row('cs_cut_watts', 'cs_cut_mode'),
						Row('cs_coagulation_watts', 'cs_coagulation_mode' )
                   	),
                   	Fieldset('Profilactic measures',
                   		Row('clips_control_group', 'clips_tratment_group'),
						Row('not_tired_closure_by', 'closure_technique'),
						'number_clips_needed',
						Row('clips_n_lote', 'clips_exp_date')
                   	),
                   	Fieldset('Complications',
                   		'perforation',
						Row('surgery_from_endoscopy', 'surgery_by_complication'),
						Row('bleeding', 'immediate_bleeding'),
						Row('delayed_bleeding', 'bleeding_treatment'),
						'transfusion',
						'pps',
						'fever',
						'pain_requiring_medical_intervention',
						Row('hospital_stay_by_technique', 'hospital_stay_by_complication'),
                   	),
                   	Fieldset('Follow up',
                   		'follow_up_months',
						'successful_treatment',			
						'last_date_endoscopic_follow_up',
						Row('recurrence_three_six_months_control', 'recurrenec_one_year_control', 'global_recurrence'),						
                   	),
                   	Fieldset('Aditional info',
                   		'other_complications_comments',
						'other_comments',
                   	)
            )
	

class RegistrationForm(forms.Form):

	username = forms.CharField()
	email = forms.EmailField(label="Email Address")
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
	receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
	agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

	"""
	fields = Case._meta.fields

	for field in fields:
		exec("%s=%s" % (field.name, field))
	"""

	

	layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Patient',
                             Row('first_name', 'first_name'),
                             'first_name', 'first_name', 'first_name'))