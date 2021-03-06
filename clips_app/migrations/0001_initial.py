# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('doctor', models.IntegerField(null=True, blank=True, verbose_name='Doctor')),
                ('date', models.DateField(null=True, blank=True, verbose_name='Date')),
                ('name', models.CharField(null=True, max_length=2, blank=True, verbose_name='Name')),
                ('id_number', models.CharField(null=True, max_length=10, blank=True, verbose_name='ID Number')),
                ('age', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], blank=True, verbose_name='Age')),
                ('age_interval', models.IntegerField(null=True, max_length=2, blank=True, choices=[(1, '<= 60'), (2, '67-74'), (3, '>= 75')], verbose_name='Age interval')),
                ('sex', models.IntegerField(null=True, max_length=1, blank=True, choices=[(1, 'Male'), (2, 'Female')], verbose_name='Sex')),
                ('asa', models.IntegerField(null=True, blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], verbose_name='ASA')),
                ('hypertension', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Hypertension')),
                ('hb', models.IntegerField(null=True, blank=True, verbose_name='HB')),
                ('platelets', models.IntegerField(null=True, blank=True, verbose_name='Platelets')),
                ('inr', models.IntegerField(null=True, blank=True, verbose_name='INR')),
                ('pt', models.IntegerField(null=True, blank=True, verbose_name='PT')),
                ('aspirin', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')], verbose_name='Aspirin')),
                ('anticoagulants', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiagregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], verbose_name='Anticoagulants')),
                ('antiplatelet_anticoagulant', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Antiplatelet'), (2, 'Double antiplatelet'), (3, 'Warfarin acenocumarol'), (4, 'Dabigatran (new antic)')], verbose_name='Antiplatelet anticoagulant/antiagregant')),
                ('heparinbridgetherapy', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Heparin Bridge Therapy')),
                ('nombre_p_activo_antiagreg_anticoag', models.IntegerField(null=True, blank=True, verbose_name='Active ingredient anticoagulant/antiagregant')),
                ('day_of_reintroduction_antiagregant', models.IntegerField(null=True, blank=True, verbose_name='Day of reintroduction anticoagulant/antiagregant')),
                ('paris_calif', models.IntegerField(null=True, blank=True, choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], verbose_name='Paris Clasif.')),
                ('lst_yn', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='LST yn')),
                ('lst_morphology', models.IntegerField(null=True, blank=True, choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], verbose_name='LST Morphology')),
                ('large_nodule_one_cm', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Large nodule 1cm')),
                ('demacrated_depressed_area', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Demacrated depressed area')),
                ('sclerous_wall_change', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Sclerous wall change')),
                ('fold_convergency', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Fold convergency')),
                ('chicken_skin_mucosa_around', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Chicken skin mucosa around')),
                ('maximum_size_mm', models.IntegerField(null=True, blank=True, verbose_name='Maximum size (mm)')),
                ('area_square_cm', models.IntegerField(null=True, blank=True, verbose_name='Area (cm2)')),
                ('location', models.IntegerField(null=True, blank=True, choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic'), (6, 'Ascendent'), (7, 'Cecum')], verbose_name='Location')),
                ('ileocecal_valve_involvement', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Ileocecal valve involvement')),
                ('high_definition', models.IntegerField(null=True, blank=True, choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')], verbose_name='High definition')),
                ('endoscopemodel', models.CharField(null=True, max_length=50, blank=True, verbose_name='Endoscope model')),
                ('nbi', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='NBI')),
                ('nbi_sano', models.IntegerField(null=True, blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], verbose_name='NBI sano')),
                ('nbi_nice', models.IntegerField(null=True, blank=True, choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], verbose_name='NBI NICE')),
                ('cromoendoscopy', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Cromoendoscopy')),
                ('kudo', models.IntegerField(null=True, blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')], verbose_name='Kudo')),
                ('prepathologic_endoscopic_diagnostic_a', models.IntegerField(null=True, blank=True, choices=[(1, 'Adenoma'), (2, 'Serrated')], verbose_name='Prepathologic endoscopic diagnost 1')),
                ('prepathologic_endoscopic_diagnostic_b', models.IntegerField(null=True, blank=True, choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], verbose_name='Prepathologic endoscopic diagnost 2')),
                ('correct_dx_adenoma_serrated', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Adenoma Serrated')),
                ('correct_dx_invasion', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Invasion')),
                ('histology', models.IntegerField(null=True, blank=True, choices=[(1, 'Adenoma'), (2, 'HGD-intraepitelial carcinoma in adenoma'), (3, 'Intramucosal carcinoma in adenoma'), (4, 'Superficial submucosal carcinoma in adenoma'), (5, 'Deep submucosal carcinoma in adenoma'), (6, 'Hyperplastic'), (7, 'Sesil Serrated polyp'), (8, 'Traditional Serrated Adenoma'), (9, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (10, 'Intraepitelial carcinoma Any serrated'), (11, 'Intramucosal carcinoma Any serrated'), (12, 'Superficial submucosa carc. Any serrated'), (13, 'Deep submucosa carc. Any serrated'), (14, 'Carinoid')], verbose_name='Histology')),
                ('histol_simplified', models.IntegerField(null=True, blank=True, choices=[(1, 'Adenoma'), (2, 'HGD-Imucosal'), (3, 'Invasive adenoma'), (4, 'Serrated'), (5, 'HGD-Imucosal serrated'), (6, 'Invasive serrated'), (7, 'Carcinoid')], verbose_name='Histology simplified')),
                ('time_of_procedure_in_mins', models.IntegerField(null=True, blank=True, verbose_name='Time of procedure (s)')),
                ('difficulty_of_emr', models.IntegerField(null=True, blank=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Dificutly of EMR')),
                ('accesibility', models.IntegerField(null=True, blank=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Accesibility')),
                ('resection', models.IntegerField(null=True, blank=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloq incomplete')], verbose_name='Resection')),
                ('resection_yn', models.IntegerField(null=True, blank=True, choices=[(1, 'Piecemeal'), (2, 'En bloc')], verbose_name='Resection YN')),
                ('previous_biopsy', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous biopsy')),
                ('previous_attempt', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous attempt')),
                ('non_lifting_sign', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Non lifting sign')),
                ('technique', models.IntegerField(null=True, blank=True, choices=[(1, 'EMR'), (2, 'Hybrid-EMR')], verbose_name='Technique')),
                ('technique_two', models.IntegerField(null=True, blank=True, choices=[(1, 'One-step'), (2, 'Two-steps')], verbose_name=' Technique 2')),
                ('limit_marks', models.IntegerField(null=True, blank=True, choices=[(0, 'No marks'), (1, 'PAC marks')], verbose_name='Limit marks')),
                ('injection', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Saline'), (2, 'Glicerin'), (3, 'Hyaluronic'), (4, 'Hidrox-propil-cellulose: VOLUVEN(r)'), (5, 'Gelafundin'), (6, 'Others')], verbose_name='Injection')),
                ('adrenaline', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Adrenaline')),
                ('endocut', models.IntegerField(null=True, blank=True, choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut')], verbose_name='Endocut')),
                ('electrosurgical_generator_model', models.CharField(null=True, max_length=100, blank=True, verbose_name='Electrosurgical generator model')),
                ('polyp_retrieval', models.IntegerField(null=True, blank=True, choices=[(1, 'Roth net'), (2, 'By aspiration'), (3, 'Both methods'), (4, 'By snare')], verbose_name='Polyp retrieval')),
                ('argon_PC', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')], verbose_name='Argon PC')),
                ('argon_coagulacion', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Argón Coagulación')),
                ('coagulation_forceps', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Coagulation forceps')),
                ('cs_cut_watts', models.IntegerField(null=True, blank=True, verbose_name='Cut (watts)')),
                ('cs_cut_mode', models.IntegerField(null=True, blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], verbose_name='Endocut mode')),
                ('cs_coagulation_watts', models.IntegerField(null=True, blank=True, verbose_name='Coagulation (watts)')),
                ('cs_coagulation_mode', models.IntegerField(null=True, blank=True, choices=[(0, 'Soft'), (1, 'Force')], verbose_name='Coagulation mode')),
                ('clips', models.IntegerField(null=True, blank=True, choices=[(0, 'Control group'), (1, 'Treatment group')], verbose_name='Clips')),
                ('clips_control_group', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Punctual coagulation')], verbose_name='Clips control group')),
                ('clips_tratment_group', models.IntegerField(null=True, blank=True, choices=[(1, 'Complete closure with complete mucosal apposition'), (2, 'Complee closure without complete mucosal apposition'), (3, 'Total failed closure'), (4, 'Partial failed closure'), (5, 'Not tried closure')], verbose_name='Clips treatment group')),
                ('not_tired_closure_by', models.IntegerField(null=True, blank=True, choices=[(1, 'Big size'), (2, 'Difficult location'), (3, 'Both')], verbose_name='Not tried closure by')),
                ('closure_technique', models.IntegerField(null=True, blank=True, choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')], verbose_name='Closure technique')),
                ('number_clips_needed', models.IntegerField(null=True, blank=True, verbose_name='Number of clips needed')),
                ('perforation', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')], verbose_name='Perforation')),
                ('surgery_from_endoscopy', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Surgery from endoscopy')),
                ('surgery_by_complication', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes: bleeding'), (2, 'Yes: perforation')], verbose_name='Surgery by complication')),
                ('bleeding', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'During exploration with clinical impact'), (2, '24h'), (3, '24-48h'), (4, '3-7 days'), (5, '>7 days'), (6, 'During no clinical impact-autol')], verbose_name='Bleeding')),
                ('immediate_bleeding', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes: during expliration with clinical impact')], verbose_name='Immediate bleeding')),
                ('delayed_bleeding', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Delayed bleeding')),
                ('bleeding_treatment', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Inyection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods')], verbose_name='Bleeding treatment')),
                ('transfusion', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Transfusion')),
                ('pps', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='PPS')),
                ('fever', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')], verbose_name='Fever')),
                ('pain_requiring_medical_intervention', models.IntegerField(null=True, blank=True, verbose_name='Pain requiring medical intervantion')),
                ('hospital_stay_by_technique', models.IntegerField(null=True, blank=True, verbose_name='Hospital stay by technique')),
                ('hospital_stay_by_complication', models.IntegerField(null=True, blank=True, verbose_name='Hospital stay by complication')),
                ('follow_up_months', models.IntegerField(null=True, blank=True, verbose_name='Follow up months')),
                ('successful_treatment', models.IntegerField(null=True, blank=True, choices=[(0, 'No: surgical treatment'), (1, 'Yes: in 1 session (includes one or two steps'), (2, 'Yes, in 2 or more sessions (one session and treatment in controls')], verbose_name=' Successful treatment')),
                ('sedation', models.IntegerField(null=True, blank=True, choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], verbose_name='Sedation')),
                ('last_date_endoscopic_follow_up', models.DateField(null=True, blank=True, verbose_name='Last date endoscopic follow up')),
                ('recurrence_three_six_months_control', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], verbose_name='Recurrence 3-6 months control')),
                ('recurrenec_one_year_control', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes: endoscopic treatment'), (2, 'Yes: surgical treatment needed'), (3, 'Lost'), (4, 'Pendiente control'), (5, 'Rechaza / No seguimiento')], verbose_name='Recurrence 1 year control')),
                ('global_recurrence', models.IntegerField(null=True, blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Global recurrence')),
                ('other_complications_comments', models.TextField(null=True, max_length=500, blank=True, verbose_name='Other complications comments')),
                ('other_comments', models.TextField(null=True, max_length=500, blank=True, verbose_name='Other comments')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=200)),
                ('description', models.CharField(verbose_name='Description', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Studies',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('hospital', models.ForeignKey(to='clips_app.Hospital')),
                ('studies', models.ManyToManyField(to='clips_app.Study')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='hospital',
            field=models.ForeignKey(null=True, to='clips_app.Hospital', default=None, blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='study',
            field=models.ForeignKey(null=True, to='clips_app.Study', default=None, blank=True),
        ),
    ]
