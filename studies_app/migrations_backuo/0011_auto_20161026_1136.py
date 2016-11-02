# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0010_auto_20161026_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='clipscase',
            name='accesibility',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True, verbose_name='Accesibility', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='adrenaline',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Adrenaline', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], blank=True, verbose_name='Age', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='age_interval',
            field=models.IntegerField(max_length=2, choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], verbose_name='Age interval', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='anticoagulants',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiagregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], blank=True, verbose_name='Anticoagulants', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='area_square_cm',
            field=models.IntegerField(blank=True, verbose_name='Area (cm2)', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='argon_PC',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')], blank=True, verbose_name='Argon PC', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='asa',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], blank=True, verbose_name='ASA', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='aspirin',
            field=models.IntegerField(choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')], blank=True, verbose_name='Aspirin', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'During no clinical impact-autol'), (2, 'During exploration with clinical impact'), (3, '24h'), (4, '24-48h'), (5, '3-7 days'), (6, '>7 days')], blank=True, verbose_name='Bleeding', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='bleeding_treatment',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Inyection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods')], blank=True, verbose_name='Bleeding treatment', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Chicken skin mucosa around', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='clips',
            field=models.IntegerField(choices=[(0, 'Control group'), (1, 'Treatment group')], blank=True, verbose_name='Clips', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='clips_control_group',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Punctual coagulation')], blank=True, verbose_name='Clips control group', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='clips_exp_date',
            field=models.DateField(blank=True, verbose_name='Expiration date', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='clips_n_lote',
            field=models.IntegerField(blank=True, verbose_name='Lot number', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='clips_tratment_group',
            field=models.IntegerField(choices=[(1, 'Complete closure with complete mucosal apposition'), (2, 'Complete closure without complete mucosal apposition'), (3, 'Total failed closure'), (4, 'Partial failed closure'), (5, 'Closure not tried')], blank=True, verbose_name='Clips treatment group', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='closure_technique',
            field=models.IntegerField(choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')], blank=True, verbose_name='Closure technique', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='coagulation_forceps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Coagulation forceps', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Correct Dx Adenoma Serrated', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='correct_dx_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Correct Dx Invasion', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='cromoendoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Cromoendoscopy', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='cs_coagulation_mode',
            field=models.IntegerField(choices=[(0, 'Soft'), (1, 'Force')], blank=True, verbose_name='Coagulation mode', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='cs_coagulation_watts',
            field=models.IntegerField(blank=True, verbose_name='Coagulation (watts)', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='cs_cut_mode',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], blank=True, verbose_name='Endocut mode', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='cs_cut_watts',
            field=models.IntegerField(blank=True, verbose_name='Cut (watts)', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='date',
            field=models.DateField(blank=True, verbose_name='Date', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='day_of_reintroduction_antiagregant',
            field=models.IntegerField(blank=True, verbose_name='Day of reintroduction anticoagulant/antiagregant', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='delayed_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Delayed bleeding', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='demacrated_depressed_area',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Demacrated depressed area', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='difficulty_of_emr',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True, verbose_name='Dificutly of EMR', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='electrosurgical_generator_model',
            field=models.CharField(max_length=100, blank=True, verbose_name='Electrosurgical generator model', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='endocut',
            field=models.IntegerField(choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut/Blended')], blank=True, verbose_name='Endocut/Blended', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='endoscopemodel',
            field=models.CharField(max_length=50, blank=True, verbose_name='Endoscope model', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='fever',
            field=models.IntegerField(choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')], blank=True, verbose_name='Fever', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='fold_convergency',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Fold convergency', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='follow_up_months',
            field=models.IntegerField(blank=True, verbose_name='Follow up months', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='global_recurrence',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Global recurrence', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='hb',
            field=models.IntegerField(blank=True, verbose_name='HB', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='heparinbridgetherapy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Heparin Bridge Therapy', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='high_definition',
            field=models.IntegerField(choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')], blank=True, verbose_name='High definition', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='histol_simplified',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-Imucosal'), (3, 'Invasive adenoma'), (4, 'Serrated'), (5, 'HGD-Imucosal serrated'), (6, 'Invasive serrated'), (7, 'Carcinoid')], blank=True, verbose_name='Histology simplified', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='histology',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-intraepitelial carcinoma in adenoma'), (3, 'Intramucosal carcinoma in adenoma'), (4, 'Superficial submucosal carcinoma in adenoma'), (5, 'Deep submucosal carcinoma in adenoma'), (6, 'Hyperplastic'), (7, 'Sesil Serrated polyp'), (8, 'Traditional Serrated Adenoma'), (9, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (10, 'Intraepitelial carcinoma Any serrated'), (11, 'Intramucosal carcinoma Any serrated'), (12, 'Superficial submucosa carc. Any serrated'), (13, 'Deep submucosa carc. Any serrated'), (14, 'Carinoid')], blank=True, verbose_name='Histology', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(blank=True, verbose_name='Hospital stay by complication', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(blank=True, verbose_name='Hospital stay by technique', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='hypertension',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Hypertension', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='id_for_doctor',
            field=models.IntegerField(blank=True, verbose_name='Id for doctor', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='id_for_hospital',
            field=models.IntegerField(blank=True, verbose_name='Id for hospital', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='ileocecal_valve_involvement',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Ileocecal valve involvement', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='immediate_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact'), (2, 'Yes: during exploration without clinical impact')], blank=True, verbose_name='Immediate bleeding', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='injection',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Saline'), (2, 'Glicerin'), (3, 'Hyaluronic'), (4, 'Hidrox-propil-cellulose: VOLUVEN(r)'), (5, 'Gelafundin'), (6, 'Others')], blank=True, verbose_name='Injection', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='inr',
            field=models.FloatField(blank=True, verbose_name='INR', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='kudo',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')], blank=True, verbose_name='Kudo', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='large_nodule_one_cm',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Large nodule 1cm', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(blank=True, verbose_name='Last date endoscopic follow up', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='limit_marks',
            field=models.IntegerField(choices=[(0, 'No marks'), (1, 'APC marks')], blank=True, verbose_name='Limit marks', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='location',
            field=models.IntegerField(choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic'), (6, 'Ascendent'), (7, 'Cecum')], blank=True, verbose_name='Location', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='lst_morphology',
            field=models.IntegerField(choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], blank=True, verbose_name='LST Morphology', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='lst_yn',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='LST yn', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='maximum_size_mm',
            field=models.IntegerField(blank=True, verbose_name='Maximum size (mm)', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='nbi',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='NBI', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='nbi_nice',
            field=models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], blank=True, verbose_name='NBI NICE', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='nbi_sano',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], blank=True, verbose_name='NBI sano', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.IntegerField(blank=True, verbose_name='Active ingredients anticoagulant/antiagregant', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='non_lifting_sign',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Non lifting sign', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='not_tired_closure_by',
            field=models.IntegerField(choices=[(1, 'Big size'), (2, 'Difficult location'), (3, 'Both')], blank=True, verbose_name='Closure not tried because of', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='number_clips_needed',
            field=models.IntegerField(blank=True, verbose_name='Number of clips needed', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='other_comments',
            field=models.TextField(max_length=500, blank=True, verbose_name='Other comments', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='other_complications_comments',
            field=models.TextField(max_length=500, blank=True, verbose_name='Other complications comments', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Pain requiring medical intervantion', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='paris_calif',
            field=models.IntegerField(choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], blank=True, verbose_name='Paris Clasif.', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='perforation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')], blank=True, verbose_name='Perforation', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='platelets',
            field=models.IntegerField(blank=True, verbose_name='Platelets', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='polyp_retrieval',
            field=models.IntegerField(choices=[(1, 'Roth net'), (2, 'By aspiration'), (3, 'Both methods'), (4, 'By snare')], blank=True, verbose_name='Polyp retrieval', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='pps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Post polypectomy syndrome', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'Serrated')], blank=True, verbose_name='Prepathologic endoscopic diagnost 1', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], blank=True, verbose_name='Prepathologic endoscopic diagnost 2', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='previous_attempt',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Previous attempt', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='previous_biopsy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Previous biopsy', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='pt',
            field=models.IntegerField(blank=True, verbose_name='PT', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], blank=True, verbose_name='Recurrence 3-6 months control', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='recurrenec_one_year_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], blank=True, verbose_name='Recurrence 1 year control', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='resection',
            field=models.IntegerField(choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloq incomplete')], blank=True, verbose_name='Resection', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='sclerous_wall_change',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Sclerous wall change', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='sedation',
            field=models.IntegerField(choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], blank=True, verbose_name='Sedation', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='sex',
            field=models.IntegerField(max_length=1, choices=[(1, 'Male'), (2, 'Female')], verbose_name='Sex', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='snare_tip_soft_coagulation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Snare tip soft coagulation', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='successful_treatment',
            field=models.IntegerField(choices=[(0, 'No: surgical treatment'), (1, 'Yes: in 1 session (includes one or two steps'), (2, 'Yes, in 2 or more sessions (one session and treatment in controls')], blank=True, verbose_name=' Successful treatment', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='surgery_by_complication',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: bleeding'), (2, 'Yes: perforation')], blank=True, verbose_name='Surgery by complication', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='surgery_from_endoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Surgery from endoscopy', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='technique',
            field=models.IntegerField(choices=[(1, 'EMR'), (2, 'Hybrid-EMR')], blank=True, verbose_name='Technique', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='technique_two',
            field=models.IntegerField(choices=[(1, 'One-step'), (2, 'Two-steps')], blank=True, verbose_name=' Technique 2', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(blank=True, verbose_name='Time of procedure (m)', null=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='transfusion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, verbose_name='Transfusion', null=True),
        ),
    ]
