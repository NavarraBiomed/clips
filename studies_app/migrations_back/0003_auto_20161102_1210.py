# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0002_auto_20161102_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obsinternationalcase',
            name='observationalcase_ptr',
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='accesibility',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Accesibility', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='adrenaline',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Adrenaline', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='age',
            field=models.IntegerField(verbose_name='Age', validators=[django.core.validators.MinValueValidator(0)], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], max_length=2, blank=True, null=True, verbose_name='Age interval'),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='anticoagulants',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiagregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], verbose_name='Anticoagulants', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='area_square_cm',
            field=models.IntegerField(verbose_name='Area (cm2)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='argon_PC',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')], verbose_name='Argon PC', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='asa',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], verbose_name='ASA', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='aspirin',
            field=models.IntegerField(choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')], verbose_name='Aspirin', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'During no clinical impact-autol'), (2, 'During exploration with clinical impact'), (3, '24h'), (4, '24-48h'), (5, '3-7 days'), (6, '>7 days')], verbose_name='Bleeding', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='bleeding_treatment',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Inyection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods')], verbose_name='Bleeding treatment', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='budding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'High grade')], verbose_name='Budding', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Chicken skin mucosa around', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='clips_control_group',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Punctual coagulation')], verbose_name='Clips control group', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='clips_exp_date',
            field=models.DateField(verbose_name='Expiration date', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='clips_n_lote',
            field=models.IntegerField(verbose_name='Lot number', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='clips_tratment_group',
            field=models.IntegerField(choices=[(1, 'Complete closure with complete mucosal apposition'), (2, 'Complete closure without complete mucosal apposition'), (3, 'Total failed closure'), (4, 'Partial failed closure'), (5, 'Closure not tried')], verbose_name='Clips treatment group', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='closure_technique',
            field=models.IntegerField(choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')], verbose_name='Closure technique', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='coagulation_forceps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Coagulation forceps', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(choices=[(1, 'Anemia/iron deficiency'), (2, 'CRC suspected'), (3, 'CRC screening program'), (4, 'Postpolypectomy surveillance'), (5, 'Relatives with CRC or polyposis'), (6, 'Polyposis'), (7, 'Other')], verbose_name='Colonoscopy indication', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Adenoma Serrated', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='correct_dx_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Invasion', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='country',
            field=models.IntegerField(choices=[(1, 'Spain'), (2, 'Japan'), (3, 'UK'), (4, 'USA'), (5, 'China')], verbose_name='Country', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='cromoendoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Cromoendoscopy', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='cs_coagulation_mode',
            field=models.IntegerField(choices=[(0, 'Soft'), (1, 'Force')], verbose_name='Coagulation mode', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='cs_coagulation_watts',
            field=models.IntegerField(verbose_name='Coagulation (watts)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='cs_cut_mode',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], verbose_name='Endocut mode', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='cs_cut_watts',
            field=models.IntegerField(verbose_name='Cut (watts)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='date',
            field=models.DateField(verbose_name='Date', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='day_of_reintroduction_antiagregant',
            field=models.IntegerField(verbose_name='Day of reintroduction anticoagulant/antiagregant', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='degree_differentiation',
            field=models.IntegerField(choices=[(1, 'Well'), (2, 'Moderate'), (3, 'Poorly')], verbose_name='Degree differentiation', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='delayed_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Delayed bleeding', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='demacrated_depressed_area',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Demacrated depressed area', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='depth',
            field=models.IntegerField(choices=[(1, 'Mucosa'), (2, 'SM1'), (3, 'SM2'), (4, 'SM3'), (5, 'MP or deeper')], verbose_name='Depth', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='depth_sm_invasion',
            field=models.FloatField(verbose_name='Depth (Sm invasion: µ)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='difficulty_of_emr',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Dificutly of EMR', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='doctor',
            field=models.ForeignKey(null=True, verbose_name='Doctor', to='studies_app.UserProfile', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='electrosurgical_generator_model',
            field=models.CharField(max_length=100, verbose_name='Electrosurgical generator model', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='endocut',
            field=models.IntegerField(choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut/Blended')], verbose_name='Endocut/Blended', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='endoscopemodel',
            field=models.CharField(max_length=50, verbose_name='Endoscope model', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='fever',
            field=models.IntegerField(choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')], verbose_name='Fever', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='fold_convergency',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Fold convergency', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='follow_up_months',
            field=models.IntegerField(verbose_name='Follow up months', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='free_horizontal_margins',
            field=models.IntegerField(choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], verbose_name='Free horizontal margin (>1mm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='free_vertical_margins',
            field=models.IntegerField(choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], verbose_name='Free vertical margins (>1mm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='global_recurrence',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Global recurrence', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='group',
            field=models.IntegerField(choices=[(0, 'Control group'), (1, 'Treatment group')], verbose_name='Group', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hb',
            field=models.FloatField(verbose_name='HB (g/dL)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='heparinbridgetherapy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Heparin Bridge Therapy', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='high_definition',
            field=models.IntegerField(choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')], verbose_name='High definition', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='histol_simplified',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-Imucosal'), (3, 'Invasive adenoma'), (4, 'Serrated'), (5, 'HGD-Imucosal serrated'), (6, 'Invasive serrated'), (7, 'Carcinoid')], verbose_name='Histology simplified', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='histological_variants',
            field=models.IntegerField(choices=[(1, 'Adenocarcinoma'), (2, 'Mucinous'), (3, 'Medullary'), (4, 'Signet ring')], verbose_name='Histological variants', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='histology',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-intraepitelial carcinoma in adenoma'), (3, 'Intramucosal carcinoma in adenoma'), (4, 'Superficial submucosal carcinoma in adenoma'), (5, 'Deep submucosal carcinoma in adenoma'), (6, 'Hyperplastic'), (7, 'Sesil Serrated polyp'), (8, 'Traditional Serrated Adenoma'), (9, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (10, 'Intraepitelial carcinoma Any serrated'), (11, 'Intramucosal carcinoma Any serrated'), (12, 'Superficial submucosa carc. Any serrated'), (13, 'Deep submucosa carc. Any serrated'), (14, 'Carinoid')], verbose_name='Histology', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(verbose_name='Hospital stay by complication', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(verbose_name='Hospital stay by technique', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hypertension',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Hypertension', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id',
            field=models.AutoField(verbose_name='ID', default=0, serialize=False, primary_key=True, auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id_for_doctor',
            field=models.IntegerField(verbose_name='Id for doctor', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id_for_hospital',
            field=models.IntegerField(verbose_name='Id for hospital', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='ileocecal_valve_involvement',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Ileocecal valve involvement', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='immediate_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact'), (2, 'Yes: during exploration without clinical impact')], verbose_name='Immediate bleeding', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='injection',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Saline'), (2, 'Glicerin'), (3, 'Hyaluronic'), (4, 'Hidrox-propil-cellulose: VOLUVEN(r)'), (5, 'Gelafundin'), (6, 'Others')], verbose_name='Injection', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='inr',
            field=models.FloatField(verbose_name='INR', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='kudo',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')], verbose_name='Kudo', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='large_nodule_one_cm',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Large nodule 1cm', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(verbose_name='Last date endoscopic follow up', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='limit_marks',
            field=models.IntegerField(choices=[(0, 'No marks'), (1, 'APC marks')], verbose_name='Limit marks', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='location',
            field=models.IntegerField(choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic'), (6, 'Ascendent'), (7, 'Cecum')], verbose_name='Location', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='lst_morphology',
            field=models.IntegerField(choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], verbose_name='LST Morphology', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='lst_yn',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='LST yn', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='lymphatic_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Lymphatic invasion', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='maximum_size_mm',
            field=models.IntegerField(verbose_name='Maximum size (mm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nbi',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='NBI', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nbi_nice',
            field=models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], verbose_name='NBI NICE', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nbi_sano',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], verbose_name='NBI sano', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.IntegerField(verbose_name='Active ingredients anticoagulant/antiagregant', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='non_lifting_sign',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Non lifting sign', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='not_tired_closure_by',
            field=models.IntegerField(choices=[(1, 'Big size'), (2, 'Difficult location'), (3, 'Both')], verbose_name='Closure not tried because of', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='number_clips_needed',
            field=models.IntegerField(verbose_name='Number of clips needed', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='other_comments',
            field=models.TextField(max_length=500, verbose_name='Other comments', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='other_complications_comments',
            field=models.TextField(max_length=500, verbose_name='Other complications comments', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Pain requiring medical intervantion', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='paris_calif',
            field=models.IntegerField(choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], verbose_name='Paris Clasif.', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='perforation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')], verbose_name='Perforation', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='perineural_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Perineural invasion', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='platelets',
            field=models.IntegerField(verbose_name='Platelets (x10⁹/L)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='polyp_retrieval',
            field=models.IntegerField(choices=[(1, 'Roth net'), (2, 'By aspiration'), (3, 'Both methods'), (4, 'By snare')], verbose_name='Polyp retrieval', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='pps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Post polypectomy syndrome', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'Serrated')], verbose_name='Prepathologic endoscopic diagnost 1', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], verbose_name='Prepathologic endoscopic diagnost 2', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='previous_attempt',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous attempt', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='previous_biopsy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous biopsy', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='pt',
            field=models.IntegerField(verbose_name='PT (s)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], verbose_name='Recurrence 3-6 months control', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='recurrenec_one_year_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], verbose_name='Recurrence 1 year control', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='resection',
            field=models.IntegerField(choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloq incomplete')], verbose_name='Resection', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='sclerous_wall_change',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Sclerous wall change', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='sedation',
            field=models.IntegerField(choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], verbose_name='Sedation', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], max_length=1, blank=True, null=True, verbose_name='Sex'),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='snare_tip_soft_coagulation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Snare tip soft coagulation', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='study',
            field=models.ForeignKey(default=0, verbose_name='Study', to='studies_app.Study', related_name='cases_obsinternationalcase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='successful_treatment',
            field=models.IntegerField(choices=[(0, 'No: surgical treatment'), (1, 'Yes: in 1 session (includes one or two steps'), (2, 'Yes, in 2 or more sessions (one session and treatment in controls')], verbose_name=' Successful treatment', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='surgery_by_complication',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: bleeding'), (2, 'Yes: perforation')], verbose_name='Surgery by complication', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='surgery_from_endoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Surgery from endoscopy', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='technique',
            field=models.IntegerField(choices=[(1, 'EMR'), (2, 'Hybrid-EMR')], verbose_name='Technique', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='technique_two',
            field=models.IntegerField(choices=[(1, 'One-step'), (2, 'Two-steps')], verbose_name=' Technique 2', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(verbose_name='Time of procedure (m)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='transfusion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Transfusion', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='vascular_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Vascular invasion', blank=True, null=True),
        ),
    ]
