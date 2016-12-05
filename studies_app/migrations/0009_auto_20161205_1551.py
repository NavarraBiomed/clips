# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0008_auto_20161205_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obsinternationalcase',
            name='observationalcase_ptr',
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='accesibility',
            field=models.IntegerField(null=True, verbose_name='Accesibility', blank=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='adrenaline',
            field=models.IntegerField(null=True, verbose_name='Adrenaline', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], null=True, verbose_name='Age', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='age_interval',
            field=models.IntegerField(null=True, verbose_name='Age interval', blank=True, choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='anticoagulants',
            field=models.IntegerField(null=True, verbose_name='Anticoagulants', blank=True, choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiagregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='area_square_cm',
            field=models.IntegerField(null=True, verbose_name='Area (cm2)', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='argon_PC',
            field=models.IntegerField(null=True, verbose_name='Argon PC', blank=True, choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='asa',
            field=models.IntegerField(null=True, verbose_name='ASA', blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='aspirin',
            field=models.IntegerField(null=True, verbose_name='Aspirin', blank=True, choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='bleeding',
            field=models.IntegerField(null=True, verbose_name='Bleeding', blank=True, choices=[(0, 'No'), (1, 'During no clinical impact-autol'), (2, 'During exploration with clinical impact'), (3, '24h'), (4, '24-48h'), (5, '3-7 days'), (6, '>7 days')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='bleeding_treatment',
            field=models.IntegerField(null=True, verbose_name='Bleeding treatment', blank=True, choices=[(0, 'No'), (1, 'Injection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods'), (6, 'Snare tip coagulation')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='boston',
            field=models.IntegerField(null=True, verbose_name='Boston', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='boston_left',
            field=models.IntegerField(null=True, verbose_name='Boston left colon', blank=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='boston_right',
            field=models.IntegerField(null=True, verbose_name='Boston right colon', blank=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='boston_transverse',
            field=models.IntegerField(null=True, verbose_name='Boston transverse colon', blank=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='budding',
            field=models.IntegerField(null=True, verbose_name='Budding', blank=True, choices=[(0, 'No or low grade'), (1, 'High grade')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='case_number',
            field=models.IntegerField(null=True, verbose_name='Case number', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(null=True, verbose_name='Chicken skin mucosa around', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='chromoendoscopy',
            field=models.IntegerField(null=True, verbose_name='Cromoendoscopy', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='clipping',
            field=models.IntegerField(null=True, verbose_name='Clipping', blank=True, choices=[(0, 'No'), (1, 'Punctual (VISIBLE\xa0VESSEL)'), (2, 'Partially clipped'), (3, 'Complete clip closure')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='closure_technique',
            field=models.IntegerField(null=True, verbose_name='Closure technique', blank=True, choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='coagulation_forceps',
            field=models.IntegerField(null=True, verbose_name='Coagulation forceps', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(null=True, verbose_name='Colonoscopy indication', blank=True, choices=[(1, 'Symptoms'), (2, 'CRC screening'), (3, 'Follow up'), (4, 'Referred to resection')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(null=True, verbose_name='Correct Dx Adenoma Serrated', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='correct_dx_invasion',
            field=models.IntegerField(null=True, verbose_name='Correct Dx Invasion', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='country',
            field=models.IntegerField(null=True, verbose_name='Country', blank=True, choices=[(1, 'Spain'), (2, 'Japan'), (3, 'UK'), (4, 'USA'), (5, 'China')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='date',
            field=models.DateField(null=True, verbose_name='Date', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='day_of_reintroduction_antiagregant',
            field=models.IntegerField(null=True, verbose_name='Day of reintroduction anticoagulant/antiagregant', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='degree_differentiation',
            field=models.IntegerField(null=True, verbose_name='Degree differentiation', blank=True, choices=[(1, 'Well'), (2, 'Moderate'), (3, 'Poorly')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='delayed_bleeding',
            field=models.IntegerField(null=True, verbose_name='Delayed bleeding', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='demarcated_depressed_area',
            field=models.IntegerField(null=True, verbose_name='Demarcated depressed area', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='depth',
            field=models.IntegerField(null=True, verbose_name='Depth', blank=True, choices=[(1, 'Mucosa'), (2, 'SM1'), (3, 'SM2'), (4, 'SM3'), (5, 'MP or deeper')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='depth_sm_invasion',
            field=models.FloatField(null=True, verbose_name='Depth (Sm invasion: µ)', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='difficult_locations',
            field=models.IntegerField(null=True, verbose_name='Difficult locations', blank=True, choices=[(1, 'Ileo-cecal valve'), (2, 'Ileo-cecal valve+ distal ileum'), (3, 'Dentate line'), (4, 'Diverticula'), (5, 'Appendix')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='difficulty_of_emr',
            field=models.IntegerField(null=True, verbose_name='Difficutly of EMR', blank=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='doctor',
            field=models.ForeignKey(to='studies_app.UserProfile', verbose_name='Doctor', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='dye_submucosal_injection',
            field=models.IntegerField(null=True, verbose_name='Dye submucosal injection', blank=True, choices=[(0, 'No'), (1, 'Indigo carmin'), (3, 'Methylene blue')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='electrosurgical_generator_model',
            field=models.CharField(null=True, verbose_name='Electrosurgical generator model', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='endocut',
            field=models.IntegerField(null=True, verbose_name='Endocut/Blended', blank=True, choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut/Blended')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='endoscopemodel',
            field=models.CharField(null=True, verbose_name='Endoscope model', blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='endoscopic_technique',
            field=models.IntegerField(null=True, verbose_name='Endoscopic technique', blank=True, choices=[(1, 'Patient sent to surgery '), (2, 'EMR'), (3, 'Hybrid EMR'), (4, 'ESD'), (5, 'Full-thickness resection')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='endoscopist',
            field=models.CharField(null=True, verbose_name='Endoscopist', blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='fever',
            field=models.IntegerField(null=True, verbose_name='Fever', blank=True, choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='fold_convergency',
            field=models.IntegerField(null=True, verbose_name='Fold convergency', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='follow_up_months',
            field=models.IntegerField(null=True, verbose_name='Follow up months', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='free_horizontal_margins',
            field=models.IntegerField(null=True, verbose_name='Free horizontal margin (>1mm)', blank=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='free_vertical_margins',
            field=models.IntegerField(null=True, verbose_name='Free vertical margins (>1mm)', blank=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='global_recurrence',
            field=models.IntegerField(null=True, verbose_name='Global recurrence', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='group',
            field=models.IntegerField(null=True, verbose_name='Group', blank=True, choices=[(0, 'Control group'), (1, 'Treatment group')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='heparinbridgetherapy',
            field=models.IntegerField(null=True, verbose_name='Heparin Bridge Therapy', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='high_definition',
            field=models.IntegerField(null=True, verbose_name='High definition', blank=True, choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='histological_variants',
            field=models.IntegerField(null=True, verbose_name='Histological variants', blank=True, choices=[(1, 'Adenocarcinoma'), (2, 'Mucinous'), (3, 'Medullary'), (4, 'Signet ring')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='histology',
            field=models.IntegerField(null=True, verbose_name='Histology', blank=True, choices=[(1, 'Adenoma'), (2, 'HGD to intramucosal carcinoma in adenoma'), (3, 'Superficial submucosal carcinoma in adenoma'), (4, 'Deep submucosal carcinoma in adenoma'), (5, 'Hyperplastic'), (6, 'Sesil Serrated polyp'), (7, 'Traditional Serrated Adenoma'), (8, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (9, 'HGD to intramucosal carcinoma any serrated'), (10, 'Superficial submucosa carc. Any serrated'), (11, 'Deep submucosa carc. Any serrated'), (12, 'Carcinoid')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(null=True, verbose_name='Hospital stay by complication (days)', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(null=True, verbose_name='Hospital stay by technique (days)', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='hypertension',
            field=models.IntegerField(null=True, verbose_name='Hypertension', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id',
            field=models.AutoField(verbose_name='ID', default=1, primary_key=True, serialize=False, auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id_for_doctor',
            field=models.IntegerField(null=True, verbose_name='Id for doctor', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id_for_hospital',
            field=models.IntegerField(null=True, verbose_name='Id for hospital', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='id_number',
            field=models.IntegerField(null=True, verbose_name='ID Number', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='immediate_bleeding',
            field=models.IntegerField(null=True, verbose_name='Immediate bleeding', blank=True, choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact'), (2, 'Yes: during exploration without clinical impact')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='injection',
            field=models.IntegerField(null=True, verbose_name='Injection', blank=True, choices=[(0, 'No'), (1, 'Saline'), (2, 'Glycerol'), (3, 'Hyaluronic'), (4, 'Hydroxypropyl methylcellulose(Voluven®)'), (5, 'Succinylated gelatin (Gelafundina®)'), (6, 'Others')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='kudo',
            field=models.IntegerField(null=True, verbose_name='Kudo', blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='large_nodule_one_cm',
            field=models.IntegerField(null=True, verbose_name='Large nodule 1cm', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(null=True, verbose_name='Last date endoscopic follow up', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='laxative',
            field=models.IntegerField(null=True, verbose_name='Laxative', blank=True, choices=[(1, '4 litre polyethylene glycol (Bohm, Casenglicol)'), (2, 'Polyethylene gylcol plus ascorbate: 2 litres (Moviprep)'), (3, 'Sodium picosulfate, magnesium citrate (Citrafleet)'), (4, 'Fosfates (Fosfosoda)'), (5, 'Sulfates (Eziclen)')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='laxative_schedule',
            field=models.IntegerField(null=True, verbose_name='Laxative schedule', blank=True, choices=[(1, 'Day before of colonoscopy'), (2, 'Split dose overnight'), (3, 'Same day of colonoscopy')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='limit_marks',
            field=models.IntegerField(null=True, verbose_name='Limit marks', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='location',
            field=models.IntegerField(null=True, verbose_name='Location', blank=True, choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic flexure'), (6, 'Ascending'), (7, 'Cecum')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='lst_morphology',
            field=models.IntegerField(null=True, verbose_name='LST Morphology', blank=True, choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='lst_yn',
            field=models.IntegerField(null=True, verbose_name='LST yn', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='lymphatic_invasion',
            field=models.IntegerField(null=True, verbose_name='Lymphatic invasion', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='maximum_size_mm',
            field=models.IntegerField(null=True, verbose_name='Maximum size (mm)', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nbi',
            field=models.IntegerField(null=True, verbose_name='NBI/FICE', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nbi_nice',
            field=models.IntegerField(null=True, verbose_name='NICE', blank=True, choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nbi_sano',
            field=models.IntegerField(null=True, verbose_name='SANO', blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(null=True, verbose_name='Active ingredients anticoagulant/antiagregant', blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='non_lifting_sign',
            field=models.IntegerField(null=True, verbose_name='Non lifting sign', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='number_clips_needed',
            field=models.IntegerField(null=True, verbose_name='Number of clips needed', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='number_of_sessions',
            field=models.IntegerField(null=True, verbose_name='Number of endoscopic sessions needed', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='other_coagulopathies',
            field=models.IntegerField(null=True, verbose_name='Other coagulopathies', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='other_comments',
            field=models.TextField(null=True, verbose_name='Other comments', blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='other_complications_comments',
            field=models.TextField(null=True, verbose_name='Other complications comments', blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(null=True, verbose_name='Pain requiring medical intervantion', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='paris_calif',
            field=models.IntegerField(null=True, verbose_name='Paris Clasif.', blank=True, choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='perforation',
            field=models.IntegerField(null=True, verbose_name='Perforation', blank=True, choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='perineural_invasion',
            field=models.IntegerField(null=True, verbose_name='Perineural invasion', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='platelets',
            field=models.IntegerField(null=True, verbose_name='Platelets', blank=True, choices=[(0, '>150.000'), (1, '150.000-50.000'), (2, '< 50.000')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='pps',
            field=models.IntegerField(null=True, verbose_name='Post polypectomy syndrome', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(null=True, verbose_name='Prepathologic endoscopic diagnost 1', blank=True, choices=[(1, 'Adenoma'), (2, 'Serrated')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(null=True, verbose_name='Prepathologic endoscopic diagnost 2', blank=True, choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='previous_attempt',
            field=models.IntegerField(null=True, verbose_name='Previous attempt', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='previous_biopsy',
            field=models.IntegerField(null=True, verbose_name='Previous biopsy', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(null=True, verbose_name='Recurrence 3-6 months control', blank=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='recurrenec_one_year_control',
            field=models.IntegerField(null=True, verbose_name='Recurrence 1 year control', blank=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='resection',
            field=models.IntegerField(null=True, verbose_name='Resection', blank=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloc incomplete')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='sclerous_wall_change',
            field=models.IntegerField(null=True, verbose_name='Sclerous wall change', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='sedation',
            field=models.IntegerField(null=True, verbose_name='Sedation', blank=True, choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='sex',
            field=models.IntegerField(null=True, verbose_name='Sex', blank=True, choices=[(1, 'Male'), (2, 'Female')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='snare_tip_soft_coagulation',
            field=models.IntegerField(null=True, verbose_name='Snare tip soft coagulation', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='study',
            field=models.ForeignKey(to='studies_app.Study', verbose_name='Study', default=1, related_name='cases_obsinternationalcase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='successful_treatment',
            field=models.IntegerField(null=True, verbose_name=' Successful treatment', blank=True, choices=[(0, 'No (surgery)'), (1, 'Yes (endoscopic treatment)')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='surgery',
            field=models.IntegerField(null=True, verbose_name='Surgery', blank=True, choices=[(0, 'No needed'), (1, 'Primary for technical reasons'), (2, 'Primary for suspected invasiveness'), (3, 'Due to bleeding'), (4, 'Due to perforation'), (5, 'Histological reasons'), (6, 'Clinical/patient decision')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(null=True, verbose_name='Time of procedure (m)', blank=True),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='transfusion',
            field=models.IntegerField(null=True, verbose_name='Transfusion', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='treatment_of_residual_polyp',
            field=models.IntegerField(null=True, verbose_name='Treatment of residual polyp', blank=True, choices=[(1, 'Not necessary'), (2, 'APC'), (3, 'Snare tip coagulation'), (4, 'Cold avulsion plus coagulation'), (5, 'Hot avulsion'), (6, 'KAR (knife assisted resection)')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='vascular_invasion',
            field=models.IntegerField(null=True, verbose_name='Vascular invasion', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='visible_scar',
            field=models.IntegerField(null=True, verbose_name='Visible scar', blank=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
    ]
