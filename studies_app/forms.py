from django import forms
from material import *
from .models import *
import studies_app
from django.views.generic import *
from django.views.generic.edit import FormView


def get_form_from_case(case, **kwargs ):
    post = kwargs.get('post', None)
    hidden_fields = kwargs.get('hidden_fields', [])
    study_type = case.study.study_type

    if study_type == "clips":
        return ClipsForm(post,instance = case, hidden_fields=hidden_fields)
    elif study_type == "cancer":
        return CancerForm(post, instance = case, hidden_fields=hidden_fields)
    elif study_type == "observational":
        return ObservationalForm(post, instance = case, hidden_fields=hidden_fields)
    elif study_type == "obsinternational":
        return ObsinternationalForm(post, instance = case, hidden_fields=hidden_fields)

class CaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        hidden_fields = kwargs.pop('hidden_fields', [])
        super(CaseForm, self).__init__(*args, **kwargs)


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
        exclude = ('id_for_doctor', 'id_for_hospital', 'group')

    template = 'studies_app/edit/observational.html'
    layout = Layout(
            Row('study'),
            Row('doctor'),
            Row('endoscopist', 'country' ),
            Row('id_number','case_number'),
            Fieldset('Patient info',
                    Row('sex', 'date'),
                    Row('age', 'age_interval'),
                    Row('asa', 'hypertension'),
                    Row('aspirin', 'anticoagulants'),
                    Row('platelets','other_coagulopathies'),
                    Row('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
                    Row('day_of_reintroduction_antiaggregant',),
                    Row('colonoscopy_indication'),
            ),
            Fieldset('Polyp characteristics',
                Row('paris_calif',),
                Row('lst_yn','lst_morphology'),
                Row('large_nodule_one_cm',),
                Row('demarcated_depressed_area',),
                Row('sclerous_wall_change',),
                Row('fold_convergency',),
                Row('chicken_skin_mucosa_around',),
                Row('maximum_size_mm', 'area_square_cm'),
                Row('location',),
                Row('difficult_locations',),
            ),
            Fieldset('Technical considerations',
                Row('high_definition',),
                Row('endoscopemodel',),
                Row('nbi', 'nbi_sano', 'jnet', 'nbi_nice'),
                Row('chromoendoscopy',),
                Row('kudo',),
                Row('sedation',),
                Row('time_of_procedure_in_mins',),
                Row('difficulty_of_emr',),
                Row('accesibility'),
                Row('previous_biopsy', 'previous_attempt'),
                Row('non_lifting_sign',),
                Row('visible_scar'),
                Row('endoscopic_technique','resection'),
                Row('treatment_of_residual_polyp', 'limit_marks',),
                Row('injection', 'dye_submucosal_injection'),
                Row('adrenaline'),
                Row('laxative','laxative_schedule'),
                Row('boston_right', 'boston_transverse', 'boston_left'),
                Row('boston'),
                Row('caps_accessories'),
                Row('sydney', 'mucosal_defect_vessels', 'mucosal_defect_hematoma')

            ),
            Fieldset('Morphology and Histology',
                Row('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
                Row('correct_dx_adenoma_serrated','correct_dx_invasion'),
                Row('histology'),
                Row('depth', 'depth_sm_invasion'),
                Row('lymphatic_invasion', 'vascular_invasion', 'perineural_invasion'),
                Row('budding', 'degree_differentiation'),
                Row('histological_variants',),
                Row('free_vertical_margins','free_horizontal_margins'),
            ),
            Fieldset('Cautering settings',
                Row('endocut','electrosurgical_generator_model'),

            ),
            Fieldset('Profilactic measures',
                Row('argon_PC'),
                Row('snare_tip_soft_coagulation', 'coagulation_forceps'),
                Row('clipping', 'closure_technique'),
                Row('number_clips_needed',),
            ),
            Fieldset('Surgery/Complications',
                Row('surgery'),
                Row('perforation',),
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
                Row('number_of_sessions'),
            ),
            Fieldset('Aditional info',
                Row('other_complications_comments',),
                Row('other_comments',),
            )
    )

class ObsinternationalForm(CaseForm):

    class Meta:
        model = ObsinternationalCase
        exclude = ('id_for_doctor', 'id_for_hospital', 'group')

    template = 'studies_app/edit/observational.html'
    layout = Layout(
            Row('study'),
            Row('doctor'),
            Row('endoscopist', 'country' ),
            Row('id_number','case_number'),
            Fieldset('Patient info',
                    Row('sex', 'date'),
                    Row('age', 'age_interval', 'ethnicity'),
                    Row('asa', 'hypertension'),
                    Row('aspirin', 'anticoagulants'),
                    Row('platelets','other_coagulopathies'),
                    Row('heparinbridgetherapy', 'nombre_p_activo_antiagreg_anticoag'),
                    Row('day_of_reintroduction_antiaggregant',),
                    Row('colonoscopy_indication'),
            ),
            Fieldset('Polyp characteristics',
                Row('paris_calif',),
                Row('lst_yn','lst_morphology'),
                Row('large_nodule_one_cm',),
                Row('demarcated_depressed_area',),
                Row('sclerous_wall_change',),
                Row('fold_convergency',),
                Row('chicken_skin_mucosa_around',),
                Row('maximum_size_mm', 'area_square_cm'),
                Row('location',),
                Row('difficult_locations',),
            ),
            Fieldset('Technical considerations',
                Row('high_definition',),
                Row('endoscopemodel',),
                Row('nbi', 'nbi_sano', 'jnet', 'nbi_nice'),
                Row('chromoendoscopy',),
                Row('kudo',),
                Row('sedation',),
                Row('time_of_procedure_in_mins',),
                Row('difficulty_of_emr',),
                Row('accesibility'),
                Row('previous_biopsy', 'previous_attempt'),
                Row('non_lifting_sign',),
                Row('visible_scar'),
                Row('endoscopic_technique','resection'),
                Row('treatment_of_residual_polyp', 'limit_marks',),
                Row('injection', 'dye_submucosal_injection'),
                Row('adrenaline'),
                Row('laxative','laxative_schedule'),
                Row('boston_right', 'boston_transverse', 'boston_left'),
                Row('boston'),
                Row('caps_accessories'),
                Row('sydney', 'mucosal_defect_vessels', 'mucosal_defect_hematoma')

            ),
            Fieldset('Morphology and Histology',
                Row('prepathologic_endoscopic_diagnostic_a','prepathologic_endoscopic_diagnostic_b'),
                Row('correct_dx_adenoma_serrated','correct_dx_invasion'),
                Row('histology'),
                Row('depth', 'depth_sm_invasion'),
                Row('lymphatic_invasion', 'vascular_invasion', 'perineural_invasion'),
                Row('budding', 'degree_differentiation'),
                Row('histological_variants',),
                Row('free_vertical_margins','free_horizontal_margins'),
            ),
            Fieldset('Cautering settings',
                Row('endocut','electrosurgical_generator_model'),

            ),
            Fieldset('Profilactic measures',
                Row('argon_PC'),
                Row('snare_tip_soft_coagulation', 'coagulation_forceps'),
                Row('clipping', 'closure_technique'),
                Row('number_clips_needed',),
            ),
            Fieldset('Surgery/Complications',
                Row('surgery'),
                Row('perforation',),
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
                Row('number_of_sessions'),
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
							Row('day_of_reintroduction_antiaggregant',),
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
						Row('cromoendoscopy',),
						Row('kudo',),
                        Row('sedation',),
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
