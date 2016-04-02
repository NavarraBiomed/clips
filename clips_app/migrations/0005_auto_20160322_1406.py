# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0004_auto_20160322_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='accesibility',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True, null=True, verbose_name='Accesibility'),
        ),
        migrations.AlterField(
            model_name='study',
            name='adrenaline',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Adrenaline'),
        ),
        migrations.AlterField(
            model_name='study',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='study',
            name='age_interval',
            field=models.CharField(choices=[(1, '<= 60'), (2, '67-74'), (3, '>= 75')], blank=True, max_length=2, null=True, verbose_name='Age interval'),
        ),
        migrations.AlterField(
            model_name='study',
            name='anticoagulants',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiagregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], blank=True, null=True, verbose_name='Anticoagulants'),
        ),
        migrations.AlterField(
            model_name='study',
            name='antiplatelet_anticoagulant',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Antiplatelet'), (2, 'Double antiplatelet'), (3, 'Warfarin acenocumarol'), (4, 'Debigatran (new antic)')], blank=True, null=True, verbose_name='Antiplatelet anticoagulant'),
        ),
        migrations.AlterField(
            model_name='study',
            name='area_square_cm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Area (cm2, blank= True, null = True)'),
        ),
        migrations.AlterField(
            model_name='study',
            name='argon_PC',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')], blank=True, null=True, verbose_name='Argon PC'),
        ),
        migrations.AlterField(
            model_name='study',
            name='argon_coagulacion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Argón Coagulación'),
        ),
        migrations.AlterField(
            model_name='study',
            name='asa',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], blank=True, null=True, verbose_name='ASA'),
        ),
        migrations.AlterField(
            model_name='study',
            name='aspirin',
            field=models.IntegerField(choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')], blank=True, null=True, verbose_name='Aspirin'),
        ),
        migrations.AlterField(
            model_name='study',
            name='bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'During exploration with clinical impact'), (2, '24h'), (3, '24-48h'), (4, '3-7 days'), (5, '>7 days'), (6, 'During no clinical impact-autol')], blank=True, null=True, verbose_name='Bleeding'),
        ),
        migrations.AlterField(
            model_name='study',
            name='bleeding_treatment',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Inyection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods')], blank=True, null=True, verbose_name='Bleeding treatment'),
        ),
        migrations.AlterField(
            model_name='study',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Chicken skin mucosa around'),
        ),
        migrations.AlterField(
            model_name='study',
            name='clips',
            field=models.IntegerField(choices=[(0, 'Control group'), (1, 'Yes')], blank=True, null=True, verbose_name='Clips'),
        ),
        migrations.AlterField(
            model_name='study',
            name='clips_control_group',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Punctual coagulation')], blank=True, null=True, verbose_name='Clips control group'),
        ),
        migrations.AlterField(
            model_name='study',
            name='clips_tratment_group',
            field=models.IntegerField(choices=[(1, 'Complete closure with complete mucosal apposition'), (2, 'Complee closure without complete mucosal apposition'), (3, 'Total failed closure'), (4, 'Partial failed closure'), (5, 'Not tired closure')], blank=True, null=True, verbose_name='Clips treatment group'),
        ),
        migrations.AlterField(
            model_name='study',
            name='closure_technique',
            field=models.IntegerField(choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')], blank=True, null=True, verbose_name='Closure technique'),
        ),
        migrations.AlterField(
            model_name='study',
            name='coagulation_forceps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Coagulation forceps'),
        ),
        migrations.AlterField(
            model_name='study',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Correct Dx Adenoma Serrated'),
        ),
        migrations.AlterField(
            model_name='study',
            name='correct_dx_invasion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Correct Dx Invasion'),
        ),
        migrations.AlterField(
            model_name='study',
            name='cromoendoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Cromoendoscopy'),
        ),
        migrations.AlterField(
            model_name='study',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='study',
            name='day_of_reintroduction_antiagregant',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of reintroduction antiagregant'),
        ),
        migrations.AlterField(
            model_name='study',
            name='delayed_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Delayed bleeding'),
        ),
        migrations.AlterField(
            model_name='study',
            name='demacrated_depressed_area',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Demacrated depressed area'),
        ),
        migrations.AlterField(
            model_name='study',
            name='difficulty_of_emr',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True, null=True, verbose_name='Dificutly of EMR'),
        ),
        migrations.AlterField(
            model_name='study',
            name='doctor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Doctor'),
        ),
        migrations.AlterField(
            model_name='study',
            name='electrosurgical_generator_model',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Electrosurgical generator model'),
        ),
        migrations.AlterField(
            model_name='study',
            name='endocut',
            field=models.IntegerField(choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut')], blank=True, null=True, verbose_name='Endocut'),
        ),
        migrations.AlterField(
            model_name='study',
            name='endoscopemodel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Endoscope model'),
        ),
        migrations.AlterField(
            model_name='study',
            name='fever',
            field=models.IntegerField(choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')], blank=True, null=True, verbose_name='Fever'),
        ),
        migrations.AlterField(
            model_name='study',
            name='fold_convergency',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Fold convergency'),
        ),
        migrations.AlterField(
            model_name='study',
            name='follow_up_months',
            field=models.IntegerField(blank=True, null=True, verbose_name='Follow up months'),
        ),
        migrations.AlterField(
            model_name='study',
            name='global_recurrence',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Global recurrence'),
        ),
        migrations.AlterField(
            model_name='study',
            name='hb',
            field=models.IntegerField(blank=True, null=True, verbose_name='HB'),
        ),
        migrations.AlterField(
            model_name='study',
            name='heparinbridgetherapy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Heparin Bridge Therapy'),
        ),
        migrations.AlterField(
            model_name='study',
            name='high_definition',
            field=models.IntegerField(choices=[(1, 'Conventinoal endoscope'), (2, 'High definition'), (3, 'Optic magnification')], blank=True, null=True, verbose_name='High definition'),
        ),
        migrations.AlterField(
            model_name='study',
            name='histol_simplified',
            field=models.IntegerField(choices=[(1, 'adenoma'), (2, 'HGD-Imucosal'), (3, 'Invasive'), (4, 'Serrated'), (5, 'HGD-Imucosal serrated'), (6, 'Invasive serrated'), (7, 'Carcinoid')], blank=True, null=True, verbose_name='Histology simplified'),
        ),
        migrations.AlterField(
            model_name='study',
            name='histology',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'HGD-intraepitelial carcinoma in adenoma'), (3, 'Intramucosal carcinoma in adenoma'), (4, 'Superficial submucosal carcinoma in adenoma'), (5, 'Deep submucosal carcinoma in adenoma'), (6, 'Hyperplastic'), (7, 'Sesil Serrated polyp'), (8, 'Traditional Serrated Adenoma'), (9, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (10, 'Intraepitelial carcinoma Any serrated'), (11, 'Intramucosal carcinoma Any serrated'), (12, 'Superficial submucosa carc. Any serrated'), (13, 'Deep submucosa carc. Any serrated'), (14, 'Carinoid')], blank=True, null=True, verbose_name='Histology'),
        ),
        migrations.AlterField(
            model_name='study',
            name='hospital',
            field=models.ForeignKey(to='clips_app.Hospital', null=True, blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='study',
            name='hospital_stay_by_complication',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by complication'),
        ),
        migrations.AlterField(
            model_name='study',
            name='hospital_stay_by_technique',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by technique'),
        ),
        migrations.AlterField(
            model_name='study',
            name='hypertension',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Hypertension'),
        ),
        migrations.AlterField(
            model_name='study',
            name='id_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ID Number'),
        ),
        migrations.AlterField(
            model_name='study',
            name='ileocecal_valve_involvement',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Ileocecal valve involvement'),
        ),
        migrations.AlterField(
            model_name='study',
            name='immediate_bleeding',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: during expliration with clinical impact')], blank=True, null=True, verbose_name='Immediate bleeding'),
        ),
        migrations.AlterField(
            model_name='study',
            name='injection',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Saline'), (2, 'Glicerin'), (3, 'Hyaluronic'), (4, 'Hidrox-propil-cellulose: VOLUVEN(r)'), (5, 'Gelafundin'), (6, 'Others')], blank=True, null=True, verbose_name='Injection'),
        ),
        migrations.AlterField(
            model_name='study',
            name='inr',
            field=models.IntegerField(blank=True, null=True, verbose_name='INR'),
        ),
        migrations.AlterField(
            model_name='study',
            name='kudo',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')], blank=True, null=True, verbose_name='Kudo'),
        ),
        migrations.AlterField(
            model_name='study',
            name='large_nodule_one_cm',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Large nodule 1cm'),
        ),
        migrations.AlterField(
            model_name='study',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(blank=True, null=True, verbose_name='Last date endoscopic follow up'),
        ),
        migrations.AlterField(
            model_name='study',
            name='limit_marks',
            field=models.IntegerField(choices=[(0, 'No marks'), (1, 'PAC marks')], blank=True, null=True, verbose_name='Limit marks'),
        ),
        migrations.AlterField(
            model_name='study',
            name='location',
            field=models.IntegerField(choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic'), (6, 'Ascendent'), (7, 'Cecum')], blank=True, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='study',
            name='lst_morphology',
            field=models.IntegerField(choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], blank=True, null=True, verbose_name='LST Morphology'),
        ),
        migrations.AlterField(
            model_name='study',
            name='lst_yn',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='LST yn'),
        ),
        migrations.AlterField(
            model_name='study',
            name='maximum_size_mm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Maximum size (mm, blank= True, null = True)'),
        ),
        migrations.AlterField(
            model_name='study',
            name='name',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='study',
            name='nbi',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='NBI'),
        ),
        migrations.AlterField(
            model_name='study',
            name='nbi_nice',
            field=models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], blank=True, null=True, verbose_name='NBI NICE'),
        ),
        migrations.AlterField(
            model_name='study',
            name='nbi_sano',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], blank=True, null=True, verbose_name='NBI sano'),
        ),
        migrations.AlterField(
            model_name='study',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nombre p. activo antiagregante...'),
        ),
        migrations.AlterField(
            model_name='study',
            name='non_lifting_sign',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Non lifting sign'),
        ),
        migrations.AlterField(
            model_name='study',
            name='not_tired_closure_by',
            field=models.IntegerField(choices=[(1, 'Big size'), (2, 'Difficult location'), (3, 'Both')], blank=True, null=True, verbose_name='Not tired closure by'),
        ),
        migrations.AlterField(
            model_name='study',
            name='number_clips_needed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of clips needed'),
        ),
        migrations.AlterField(
            model_name='study',
            name='other_comments',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Other comments'),
        ),
        migrations.AlterField(
            model_name='study',
            name='other_complications_comments',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Other complications comments'),
        ),
        migrations.AlterField(
            model_name='study',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(blank=True, null=True, verbose_name='Pain requiring medical intervantion'),
        ),
        migrations.AlterField(
            model_name='study',
            name='paris_calif',
            field=models.IntegerField(choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], blank=True, null=True, verbose_name='Paris Clasif.'),
        ),
        migrations.AlterField(
            model_name='study',
            name='perforation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')], blank=True, null=True, verbose_name='Perforation'),
        ),
        migrations.AlterField(
            model_name='study',
            name='platelets',
            field=models.IntegerField(blank=True, null=True, verbose_name='Platelets'),
        ),
        migrations.AlterField(
            model_name='study',
            name='polyp_retrieval',
            field=models.IntegerField(choices=[(1, 'Roth net'), (2, 'By aspiration'), (3, 'Both methods'), (4, 'By snare')], blank=True, null=True, verbose_name='Polyp retrieval'),
        ),
        migrations.AlterField(
            model_name='study',
            name='pps',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='PPS'),
        ),
        migrations.AlterField(
            model_name='study',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(choices=[(1, 'Adenoma'), (2, 'Serrated')], blank=True, null=True, verbose_name='Prepathologic endoscopic diagnost 1'),
        ),
        migrations.AlterField(
            model_name='study',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], blank=True, null=True, verbose_name='Prepathologic endoscopic diagnost 2'),
        ),
        migrations.AlterField(
            model_name='study',
            name='previous_attempt',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Previous attempt'),
        ),
        migrations.AlterField(
            model_name='study',
            name='previous_biopsy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Previous biopsy'),
        ),
        migrations.AlterField(
            model_name='study',
            name='pt',
            field=models.IntegerField(blank=True, null=True, verbose_name='PT'),
        ),
        migrations.AlterField(
            model_name='study',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], blank=True, null=True, verbose_name='Recurrence 3-6 months control'),
        ),
        migrations.AlterField(
            model_name='study',
            name='recurrenec_one_year_control',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: endoscopic treatment'), (2, 'Yes: surgical treatment needed'), (3, 'Lost'), (4, 'Pendiente control'), (5, 'Rechaza / No seguimiento')], blank=True, null=True, verbose_name='Recurrence 1 year control'),
        ),
        migrations.AlterField(
            model_name='study',
            name='resection',
            field=models.IntegerField(choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloq incomplete')], blank=True, null=True, verbose_name='Resection'),
        ),
        migrations.AlterField(
            model_name='study',
            name='resection_yn',
            field=models.IntegerField(choices=[(1, 'Piecemeal'), (2, 'En bloc')], blank=True, null=True, verbose_name='Resection YN'),
        ),
        migrations.AlterField(
            model_name='study',
            name='sclerous_wall_change',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Sclerous wall change'),
        ),
        migrations.AlterField(
            model_name='study',
            name='sedation',
            field=models.IntegerField(choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], blank=True, null=True, verbose_name='Sedation'),
        ),
        migrations.AlterField(
            model_name='study',
            name='sex',
            field=models.CharField(choices=[(1, 'Man'), (2, 'Woman')], blank=True, max_length=1, null=True, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='study',
            name='successful_treatment',
            field=models.IntegerField(choices=[(0, 'No: surgical treatment'), (1, 'Yes: in 1 session (includes one or two steps'), (2, 'Yes, in 2 or more sessions (one session and treatment in controls')], blank=True, null=True, verbose_name=' Successful treatment'),
        ),
        migrations.AlterField(
            model_name='study',
            name='surgery_by_complication',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes: bleeding'), (2, 'Yes: perforation')], blank=True, null=True, verbose_name='Surgery by complication'),
        ),
        migrations.AlterField(
            model_name='study',
            name='surgery_from_endoscopy',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Surgery from endoscopy'),
        ),
        migrations.AlterField(
            model_name='study',
            name='technique',
            field=models.IntegerField(choices=[(1, 'EMR'), (2, 'Hybrid-EMR')], blank=True, null=True, verbose_name='Technique'),
        ),
        migrations.AlterField(
            model_name='study',
            name='technique_two',
            field=models.IntegerField(choices=[(1, 'One-step'), (2, 'Two-steps')], blank=True, null=True, verbose_name=' Technique 2'),
        ),
        migrations.AlterField(
            model_name='study',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(blank=True, null=True, verbose_name='Time of procedure (s, blank= True, null = True)'),
        ),
        migrations.AlterField(
            model_name='study',
            name='transfusion',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], blank=True, null=True, verbose_name='Transfusion'),
        ),
    ]
