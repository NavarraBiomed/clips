from django import forms
from material import *
from .models import *
import studies_app
from django.views.generic import *
from django.views.generic.edit import FormView


def get_form_from_case(case, **kwargs ):
    #import pdb; pdb.set_trace()
    post = kwargs.get('post', None)
    study_type = case.study.study_type

    if study_type == "clips":
        return ClipsForm(post,instance = case)
    elif study_type == "cancer":
        return CancerForm(post, instance = case)
    elif study_type == "observational":
        return ObservationalForm(post, instance = case)

class CaseForm(forms.ModelForm):

    class Meta:
        abstract = True
        model = TypeCase
        exclude = ()

    layout = None
    template = 'studies_app/edit/default.html'


class CancerForm(CaseForm):
	#, LayoutMixin, View
    #CancerCase = apps.get_model('studies_app', 'CancerCase')
    class Meta:
        model = CancerCase
        exclude = ('id_for_doctor', 'id_for_hospital')
        #fields = ('name', 'clips', 'id_number', 'sex', 'study', 'doctor', 'date')

    layout = Layout(
        Row('study', 'group'),
        Row('doctor'),
        Row('organ',),
    )

class ObservationalForm(CaseForm):
    class Meta:
        model = ObservationalCase
        exclude = ('id_for_doctor', 'id_for_hospital')

    layout = Layout(
            Row('study', 'group'),
            Row('doctor'),
            Fieldset('Patient info',
                     Row('sex', 'age', 'age_interval'),
                     Row('date', 'country'),
                     Row('asa', 'hypertension', 'hb'),
                     Row('platelets',),
                    Row('inr',),
                    Row('pt',),
                    Row('aspirin', 'anticoagulants'),
                    Row('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
                    Row('day_of_reintroduction_antiagregant',),
                    Row('colonoscopy_indication'),
            ),
            Fieldset('Polyp characteristics',
                Row('paris_calif',),
                Row('lst_yn','lst_morphology'),
                Row('large_nodule_one_cm',),
                Row('demacrated_depressed_area',),
                Row('sclerous_wall_change',),
                Row('fold_convergency',),
                Row('chicken_skin_mucosa_around',),
                Row('maximum_size_mm', 'area_square_cm'),
                Row('location',),
                Row('ileocecal_valve_involvement',),
            ),
            Fieldset('Technical considerations',
                Row('high_definition',),
                Row('endoscopemodel',),
                Row('nbi', 'nbi_sano', 'nbi_nice'),
                Row('sedation',),
                Row('cromoendoscopy',),
                Row('kudo',),
                Row('time_of_procedure_in_mins',),
                Row('difficulty_of_emr',),
                Row('accesibility', 'resection'),
                Row('previous_biopsy', 'previous_attempt'),
                Row('non_lifting_sign',),
                Row('technique','technique_two'),
                Row('limit_marks',),
                Row('injection', 'adrenaline'),
                Row('polyp_retrieval'),

            ),
            Fieldset('Morphology and Histology',
                Row('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
                Row('correct_dx_adenoma_serrated','correct_dx_invasion'),
                Row('histology', 'histol_simplified'),
                Row('depth', 'depth_sm_invasion'),
                Row('lymphatic_invasion', 'vascular_invasion', 'perineural_invasion'),
                Row('budding', 'degree_differentiation'),
                Row('histological_variants',),
                Row('free_vertical_margins','free_horizontal_margins'),
            ),
            Fieldset('Cautering settings',
                Row('endocut','electrosurgical_generator_model'),
                Row('cs_cut_watts', 'cs_cut_mode'),
                Row('cs_coagulation_watts', 'cs_coagulation_mode' )
            ),
            Fieldset('Profilactic measures',
                Row('argon_PC'),
                Row('snare_tip_soft_coagulation', 'coagulation_forceps'),
                Row('clips_control_group', 'clips_tratment_group'),
                Row('not_tired_closure_by', 'closure_technique'),
                Row('number_clips_needed',),
                Row('clips_n_lote', 'clips_exp_date')
            ),
            Fieldset('Complications',
                Row('perforation',),
                Row('surgery_from_endoscopy', 'surgery_by_complication'),
                Row('bleeding', 'immediate_bleeding'),
                Row('delayed_bleeding', 'bleeding_treatment'),
                Row('transfusion',),
                Row('pps',),
                Row('fever',),
                Row('pain_requiring_medical_intervention',),
                Row('hospital_stay_by_technique', 'hospital_stay_by_complication'),
            ),
            Fieldset('Follow up',
                Row('follow_up_months',),
                Row('successful_treatment',),
                Row('last_date_endoscopic_follow_up',),
                Row('recurrence_three_six_months_control', 'recurrenec_one_year_control', 'global_recurrence'),
            ),
            Fieldset('Aditional info',
                Row('other_complications_comments',),
                Row('other_comments',),
            )
    )

class ClipsForm(CaseForm):
	#, LayoutMixin, View
    #ClipsCase = apps.get_model('studies_app', 'ClipsCase')
    class Meta:
        model = ClipsCase
        exclude = ('id_for_doctor', 'id_for_hospital')
        #fields = ('name', 'clips', 'id_number', 'sex', 'study', 'doctor', 'date')

    layout = Layout(
    				Row('study', 'group'),
    				Row('doctor'),
                    Fieldset('Patient info',
                             Row('sex', 'age', 'age_interval'),
                             Row('date',),
                             Row('asa', 'hypertension', 'hb'),
                             Row('platelets',),
							Row('inr',),
							Row('pt',),
							Row('aspirin', 'anticoagulants'),
							Row('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
							Row('day_of_reintroduction_antiagregant',),
                    ),
                    Fieldset('Polyp characteristics',
                    	Row('paris_calif',),
						Row('lst_yn','lst_morphology'),
						Row('large_nodule_one_cm',),
						Row('demacrated_depressed_area',),
						Row('sclerous_wall_change',),
						Row('fold_convergency',),
						Row('chicken_skin_mucosa_around',),
						Row('maximum_size_mm', 'area_square_cm'),
						Row('location',),
						Row('ileocecal_valve_involvement',),
                   	),
                   	Fieldset('Technical considerations',
                   	    Row('high_definition',),
						Row('endoscopemodel',),
						Row('nbi', 'nbi_sano', 'nbi_nice'),
						Row('sedation',),
						Row('cromoendoscopy',),
						Row('kudo',),
						Row('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
						Row('correct_dx_adenoma_serrated','correct_dx_invasion'),
						Row('histology', 'histol_simplified'),
						Row('time_of_procedure_in_mins',),
						Row('difficulty_of_emr',),
						Row('accesibility', 'resection'),
						Row('previous_biopsy', 'previous_attempt'),
						Row('non_lifting_sign',),
						Row('technique','technique_two'),
						Row('limit_marks',),
						Row('injection', 'adrenaline'),
						Row('polyp_retrieval'),

                   	),
                   	Fieldset('Cautering settings',
                   		Row('endocut','electrosurgical_generator_model'),
                   		Row('cs_cut_watts', 'cs_cut_mode'),
						Row('cs_coagulation_watts', 'cs_coagulation_mode' )
                   	),
                   	Fieldset('Profilactic measures',
                   		Row('argon_PC'),
						Row('snare_tip_soft_coagulation', 'coagulation_forceps'),
                   		Row('clips_control_group', 'clips_tratment_group'),
						Row('not_tired_closure_by', 'closure_technique'),
						Row('number_clips_needed',),
						Row('clips_n_lote', 'clips_exp_date')
                   	),
                   	Fieldset('Complications',
                   		Row('perforation',),
						Row('surgery_from_endoscopy', 'surgery_by_complication'),
						Row('bleeding', 'immediate_bleeding'),
						Row('delayed_bleeding', 'bleeding_treatment'),
						Row('transfusion',),
						Row('pps',),
						Row('fever',),
						Row('pain_requiring_medical_intervention',),
						Row('hospital_stay_by_technique', 'hospital_stay_by_complication'),
                   	),
                   	Fieldset('Follow up',
                   		Row('follow_up_months',),
						Row('successful_treatment',),
						Row('last_date_endoscopic_follow_up',),
						Row('recurrence_three_six_months_control', 'recurrenec_one_year_control', 'global_recurrence'),
                   	),
                   	Fieldset('Aditional info',
                   		Row('other_complications_comments',),
						Row('other_comments',),
                   	)
            )
