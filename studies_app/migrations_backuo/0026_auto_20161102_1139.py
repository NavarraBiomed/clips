# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0025_auto_20161102_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observationalinternationalcase',
            name='observationalcase_ptr',
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='accesibility',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True, null=True, verbose_name='Accesibility'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='adrenaline',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Adrenaline'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], blank=True, null=True, max_length=2, verbose_name='Age interval'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='anticoagulants',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiagregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], blank=True, null=True, verbose_name='Anticoagulants'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='area_square_cm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Area (cm2)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='argon_PC',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')], blank=True, null=True, verbose_name='Argon PC'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='asa',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], blank=True, null=True, verbose_name='ASA'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='aspirin',
            field=models.IntegerField(choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')], blank=True, null=True, verbose_name='Aspirin'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'During no clinical impact-autol'), (2, 'During exploration with clinical impact'), (3, '24h'), (4, '24-48h'), (5, '3-7 days'), (6, '>7 days')], blank=True, null=True, verbose_name='Bleeding'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='bleeding_treatment',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Inyection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods')], blank=True, null=True, verbose_name='Bleeding treatment'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='budding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'High grade')], blank=True, null=True, verbose_name='Budding'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Chicken skin mucosa around'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='clips_control_group',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Punctual coagulation')], blank=True, null=True, verbose_name='Clips control group'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='clips_exp_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expiration date'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='clips_n_lote',
            field=models.IntegerField(blank=True, null=True, verbose_name='Lot number'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='clips_tratment_group',
            field=models.IntegerField(choices=[(1, 'Complete closure with complete mucosal apposition'), (2, 'Complete closure without complete mucosal apposition'), (3, 'Total failed closure'), (4, 'Partial failed closure'), (5, 'Closure not tried')], blank=True, null=True, verbose_name='Clips treatment group'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='closure_technique',
            field=models.IntegerField(choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')], blank=True, null=True, verbose_name='Closure technique'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='coagulation_forceps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Coagulation forceps'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(choices=[(1, 'Anemia/iron deficiency'), (2, 'CRC suspected'), (3, 'CRC screening program'), (4, 'Postpolypectomy surveillance'), (5, 'Relatives with CRC or polyposis'), (6, 'Polyposis'), (7, 'Other')], blank=True, null=True, verbose_name='Colonoscopy indication'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Correct Dx Adenoma Serrated'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='correct_dx_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Correct Dx Invasion'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='country',
            field=models.IntegerField(choices=[(1, 'Spain'), (2, 'Japan'), (3, 'UK'), (4, 'USA'), (5, 'China')], blank=True, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='cromoendoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Cromoendoscopy'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='cs_coagulation_mode',
            field=models.IntegerField(choices=[(0, 'Soft'), (1, 'Force')], blank=True, null=True, verbose_name='Coagulation mode'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='cs_coagulation_watts',
            field=models.IntegerField(blank=True, null=True, verbose_name='Coagulation (watts)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='cs_cut_mode',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], blank=True, null=True, verbose_name='Endocut mode'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='cs_cut_watts',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cut (watts)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='day_of_reintroduction_antiagregant',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of reintroduction anticoagulant/antiagregant'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='degree_differentiation',
            field=models.IntegerField(choices=[(1, 'Well'), (2, 'Moderate'), (3, 'Poorly')], blank=True, null=True, verbose_name='Degree differentiation'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='delayed_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Delayed bleeding'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='demacrated_depressed_area',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Demacrated depressed area'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='depth',
            field=models.IntegerField(choices=[(1, 'Mucosa'), (2, 'SM1'), (3, 'SM2'), (4, 'SM3'), (5, 'MP or deeper')], blank=True, null=True, verbose_name='Depth'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='depth_sm_invasion',
            field=models.FloatField(blank=True, null=True, verbose_name='Depth (Sm invasion: µ)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='difficulty_of_emr',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True, null=True, verbose_name='Dificutly of EMR'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='doctor',
            field=models.ForeignKey(blank=True, to='studies_app.UserProfile', null=True, verbose_name='Doctor'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='electrosurgical_generator_model',
            field=models.CharField(blank=True, null=True, max_length=100, verbose_name='Electrosurgical generator model'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='endocut',
            field=models.IntegerField(choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut/Blended')], blank=True, null=True, verbose_name='Endocut/Blended'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='endoscopemodel',
            field=models.CharField(blank=True, null=True, max_length=50, verbose_name='Endoscope model'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='fever',
            field=models.IntegerField(choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')], blank=True, null=True, verbose_name='Fever'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='fold_convergency',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Fold convergency'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='follow_up_months',
            field=models.IntegerField(blank=True, null=True, verbose_name='Follow up months'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='free_horizontal_margins',
            field=models.IntegerField(choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], blank=True, null=True, verbose_name='Free horizontal margin (>1mm)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='free_vertical_margins',
            field=models.IntegerField(choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], blank=True, null=True, verbose_name='Free vertical margins (>1mm)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='global_recurrence',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Global recurrence'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='group',
            field=models.IntegerField(choices=[(0, 'Control group'), (1, 'Treatment group')], blank=True, null=True, verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='hb',
            field=models.FloatField(blank=True, null=True, verbose_name='HB (g/dL)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='heparinbridgetherapy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Heparin Bridge Therapy'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='high_definition',
            field=models.IntegerField(choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')], blank=True, null=True, verbose_name='High definition'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='histol_simplified',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-Imucosal'), (3, 'Invasive adenoma'), (4, 'Serrated'), (5, 'HGD-Imucosal serrated'), (6, 'Invasive serrated'), (7, 'Carcinoid')], blank=True, null=True, verbose_name='Histology simplified'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='histological_variants',
            field=models.IntegerField(choices=[(1, 'Adenocarcinoma'), (2, 'Mucinous'), (3, 'Medullary'), (4, 'Signet ring')], blank=True, null=True, verbose_name='Histological variants'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='histology',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-intraepitelial carcinoma in adenoma'), (3, 'Intramucosal carcinoma in adenoma'), (4, 'Superficial submucosal carcinoma in adenoma'), (5, 'Deep submucosal carcinoma in adenoma'), (6, 'Hyperplastic'), (7, 'Sesil Serrated polyp'), (8, 'Traditional Serrated Adenoma'), (9, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (10, 'Intraepitelial carcinoma Any serrated'), (11, 'Intramucosal carcinoma Any serrated'), (12, 'Superficial submucosa carc. Any serrated'), (13, 'Deep submucosa carc. Any serrated'), (14, 'Carinoid')], blank=True, null=True, verbose_name='Histology'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by complication'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by technique'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='hypertension',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Hypertension'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='id',
            field=models.AutoField(default=0, auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='id_for_doctor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Id for doctor'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='id_for_hospital',
            field=models.IntegerField(blank=True, null=True, verbose_name='Id for hospital'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='ileocecal_valve_involvement',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Ileocecal valve involvement'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='immediate_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact'), (2, 'Yes: during exploration without clinical impact')], blank=True, null=True, verbose_name='Immediate bleeding'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='injection',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Saline'), (2, 'Glicerin'), (3, 'Hyaluronic'), (4, 'Hidrox-propil-cellulose: VOLUVEN(r)'), (5, 'Gelafundin'), (6, 'Others')], blank=True, null=True, verbose_name='Injection'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='inr',
            field=models.FloatField(blank=True, null=True, verbose_name='INR'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='kudo',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')], blank=True, null=True, verbose_name='Kudo'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='large_nodule_one_cm',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Large nodule 1cm'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(blank=True, null=True, verbose_name='Last date endoscopic follow up'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='limit_marks',
            field=models.IntegerField(choices=[(0, 'No marks'), (1, 'APC marks')], blank=True, null=True, verbose_name='Limit marks'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='location',
            field=models.IntegerField(choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic'), (6, 'Ascendent'), (7, 'Cecum')], blank=True, null=True, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='lst_morphology',
            field=models.IntegerField(choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], blank=True, null=True, verbose_name='LST Morphology'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='lst_yn',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='LST yn'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='lymphatic_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Lymphatic invasion'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='maximum_size_mm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Maximum size (mm)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='nbi',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='NBI'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='nbi_nice',
            field=models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], blank=True, null=True, verbose_name='NBI NICE'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='nbi_sano',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], blank=True, null=True, verbose_name='NBI sano'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.IntegerField(blank=True, null=True, verbose_name='Active ingredients anticoagulant/antiagregant'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='non_lifting_sign',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Non lifting sign'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='not_tired_closure_by',
            field=models.IntegerField(choices=[(1, 'Big size'), (2, 'Difficult location'), (3, 'Both')], blank=True, null=True, verbose_name='Closure not tried because of'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='number_clips_needed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of clips needed'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='other_comments',
            field=models.TextField(blank=True, null=True, max_length=500, verbose_name='Other comments'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='other_complications_comments',
            field=models.TextField(blank=True, null=True, max_length=500, verbose_name='Other complications comments'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Pain requiring medical intervantion'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='paris_calif',
            field=models.IntegerField(choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], blank=True, null=True, verbose_name='Paris Clasif.'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='perforation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')], blank=True, null=True, verbose_name='Perforation'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='perineural_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Perineural invasion'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='platelets',
            field=models.IntegerField(blank=True, null=True, verbose_name='Platelets (x10⁹/L)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='polyp_retrieval',
            field=models.IntegerField(choices=[(1, 'Roth net'), (2, 'By aspiration'), (3, 'Both methods'), (4, 'By snare')], blank=True, null=True, verbose_name='Polyp retrieval'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='pps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Post polypectomy syndrome'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'Serrated')], blank=True, null=True, verbose_name='Prepathologic endoscopic diagnost 1'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], blank=True, null=True, verbose_name='Prepathologic endoscopic diagnost 2'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='previous_attempt',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Previous attempt'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='previous_biopsy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Previous biopsy'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='pt',
            field=models.IntegerField(blank=True, null=True, verbose_name='PT (s)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], blank=True, null=True, verbose_name='Recurrence 3-6 months control'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='recurrenec_one_year_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], blank=True, null=True, verbose_name='Recurrence 1 year control'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='resection',
            field=models.IntegerField(choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloq incomplete')], blank=True, null=True, verbose_name='Resection'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='sclerous_wall_change',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Sclerous wall change'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='sedation',
            field=models.IntegerField(choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], blank=True, null=True, verbose_name='Sedation'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], blank=True, null=True, max_length=1, verbose_name='Sex'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='snare_tip_soft_coagulation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Snare tip soft coagulation'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='study',
            field=models.ForeignKey(default=0, to='studies_app.Study', related_name='cases_observationalinternationalcase', verbose_name='Study'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='successful_treatment',
            field=models.IntegerField(choices=[(0, 'No: surgical treatment'), (1, 'Yes: in 1 session (includes one or two steps'), (2, 'Yes, in 2 or more sessions (one session and treatment in controls')], blank=True, null=True, verbose_name=' Successful treatment'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='surgery_by_complication',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: bleeding'), (2, 'Yes: perforation')], blank=True, null=True, verbose_name='Surgery by complication'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='surgery_from_endoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Surgery from endoscopy'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='technique',
            field=models.IntegerField(choices=[(1, 'EMR'), (2, 'Hybrid-EMR')], blank=True, null=True, verbose_name='Technique'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='technique_two',
            field=models.IntegerField(choices=[(1, 'One-step'), (2, 'Two-steps')], blank=True, null=True, verbose_name=' Technique 2'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(blank=True, null=True, verbose_name='Time of procedure (m)'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='transfusion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Transfusion'),
        ),
        migrations.AddField(
            model_name='observationalinternationalcase',
            name='vascular_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Vascular invasion'),
        ),
    ]
