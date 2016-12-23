# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0013_auto_20161205_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clipscase',
            name='day_of_reintroduction_antiagregant',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='day_of_reintroduction_antiagregant',
        ),
        migrations.RemoveField(
            model_name='obsinternationalcase',
            name='day_of_reintroduction_antiagregant',
        ),
        migrations.AddField(
            model_name='clipscase',
            name='day_of_reintroduction_antiaggregant',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of reintroduction anticoagulant/antiaggregant'),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='caps_accessories',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Simple Cap'), (2, 'Endocuffs'), (3, 'Endorings'), (4, 'G-eye'), (5, 'Thrid-eye')], verbose_name='Caps/accessories*'),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='day_of_reintroduction_antiaggregant',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of reintroduction anticoagulant/antiaggregant'),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='caps_accessories',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Simple Cap'), (2, 'Endocuffs'), (3, 'Endorings'), (4, 'G-eye'), (5, 'Thrid-eye')], verbose_name='Caps/accessories*'),
        ),
        migrations.AddField(
            model_name='obsinternationalcase',
            name='day_of_reintroduction_antiaggregant',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of reintroduction anticoagulant/antiaggregant'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='anticoagulants',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiaggregant'), (4, 'Acenocumarol or warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'DOAC')], verbose_name='Anticoagulants'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='immediate_bleeding',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact (treatment needed)'), (2, 'Yes: during exploration without clinical impact')], verbose_name='Immediate bleeding'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(blank=True, null=True, max_length=128, verbose_name='Active ingredients anticoagulant/antiaggregant'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='accesibility',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Accesibility*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='adrenaline',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Adrenaline*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age*', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='age_interval',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], verbose_name='Age interval*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='anticoagulants',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiaggregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], verbose_name='Anticoagulants*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='argon_PC',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: incomplete resection'), (2, 'Yes: coagulation'), (3, 'Yes: per protocol')], verbose_name='Argon PC*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='asa',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], verbose_name='ASA*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='aspirin',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, '100mg cease'), (2, '300mg cease'), (3, '100mg during EMR'), (4, '300mg during EMR')], verbose_name='Aspirin*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='bleeding',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'During no clinical impact-autol'), (2, 'During exploration with clinical impact'), (3, '24h'), (4, '24-48h'), (5, '3-7 days'), (6, '>7 days')], verbose_name='Bleeding*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='bleeding_treatment',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Injection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods'), (6, 'Snare tip coagulation')], verbose_name='Bleeding treatment*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='boston',
            field=models.IntegerField(blank=True, null=True, verbose_name='BBPS*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='boston_left',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], verbose_name='Boston left*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='boston_right',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], verbose_name='Boston right*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='boston_transverse',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], verbose_name='Boston transverse*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='budding',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No or low grade'), (1, 'High grade')], verbose_name='Budding**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='case_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Case number*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Chicken skin mucosa around*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='chromoendoscopy',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Chromoendoscopy*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='clipping',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Punctual (VISIBLE\xa0VESSEL)'), (2, 'Partially clipped'), (3, 'Complete clip closure')], verbose_name='Clipping*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='closure_technique',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Simple clipping'), (2, 'Clip-Poly loop'), (3, 'Clip Silk loop')], verbose_name='Closure technique*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='coagulation_forceps',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Coagulation forceps*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Symptoms'), (2, 'CRC screening'), (3, 'Follow up'), (4, 'Referred to resection')], verbose_name='Colonoscopy indication*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Adenoma Serrated*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='correct_dx_invasion',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Invasion*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='country',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Spain'), (2, 'Japan'), (3, 'UK'), (4, 'USA'), (5, 'China')], verbose_name='Country*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='degree_differentiation',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Well'), (2, 'Moderate'), (3, 'Poorly')], verbose_name='Degree differentiation**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='delayed_bleeding',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Delayed bleeding*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='demarcated_depressed_area',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Demarcated depressed area*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='depth',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Mucosa'), (2, 'SM1'), (3, 'SM2'), (4, 'SM3'), (5, 'MP or deeper')], verbose_name='Depth**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='depth_sm_invasion',
            field=models.FloatField(blank=True, null=True, verbose_name='Depth (Sm invasion: µ)**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='difficult_locations',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Ileo-cecal valve'), (2, 'Ileo-cecal valve+ distal ileum'), (3, 'Dentate line'), (4, 'Diverticula'), (5, 'Appendix')], verbose_name='Difficult locations*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='difficulty_of_emr',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Difficutly of EMR*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='dye_submucosal_injection',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Indigo carmin'), (3, 'Methylene blue')], verbose_name='Dye submucosal injection*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='electrosurgical_generator_model',
            field=models.CharField(blank=True, null=True, max_length=100, verbose_name='Electrosurgical generator model*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='endocut',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut/Blended')], verbose_name='Endocut/Blended*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='endoscopic_technique',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Patient sent to surgery '), (2, 'EMR'), (3, 'Hybrid EMR'), (4, 'ESD'), (5, 'Full-thickness resection')], verbose_name='Endoscopic technique*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='endoscopist',
            field=models.CharField(blank=True, null=True, max_length=128, verbose_name='Endoscopist*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='fever',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, '37-37.9'), (2, '38 or more')], verbose_name='Fever*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='fold_convergency',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Fold convergency*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='free_horizontal_margins',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], verbose_name='Free horizontal margin (>1mm)**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='free_vertical_margins',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], verbose_name='Free vertical margins (>1mm)**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='global_recurrence',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Global recurrence*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='heparinbridgetherapy',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Heparin Bridge Therapy*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='high_definition',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')], verbose_name='High definition*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='histological_variants',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Adenocarcinoma'), (2, 'Mucinous'), (3, 'Medullary'), (4, 'Signet ring')], verbose_name='Histological variants**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='histology',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Adenoma'), (2, 'HGD to intramucosal carcinoma in adenoma'), (3, 'Superficial submucosal carcinoma in adenoma'), (4, 'Deep submucosal carcinoma in adenoma'), (5, 'Hyperplastic'), (6, 'Sesil Serrated polyp'), (7, 'Traditional Serrated Adenoma'), (8, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (9, 'HGD to intramucosal carcinoma any serrated'), (10, 'Superficial submucosa carc. Any serrated'), (11, 'Deep submucosa carc. Any serrated'), (12, 'Carcinoid')], verbose_name='Histology*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by complication (days)*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by technique (days)*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='hypertension',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Hypertension*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID Number*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='immediate_bleeding',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact (treatment needed)'), (2, 'Yes: during exploration without clinical impact')], verbose_name='Immediate bleeding*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='injection',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Saline'), (2, 'Glycerol'), (3, 'Hyaluronic'), (4, 'Hydroxypropyl methylcellulose(Voluven®)'), (5, 'Succinylated gelatin (Gelafundina®)'), (6, 'Others')], verbose_name='Injection*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='large_nodule_one_cm',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Large nodule 1cm*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(blank=True, null=True, verbose_name='Last date endoscopic follow u*p'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='laxative',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '4 litre polyethylene glycol (Bohm, Casenglicol...)'), (2, 'Polyethylene gylcol plus ascorbate: 2 litres (Moviprep...)'), (3, 'Sodium picosulfate, magnesium citrate (Citrafleet...)'), (4, 'Fosfates (Fosfosoda...)'), (5, 'Sulfates (Eziclen...)')], verbose_name='Laxative*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='laxative_schedule',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Day before of colonoscopy'), (2, 'Split dose overnight'), (3, 'Same day of colonoscopy')], verbose_name='Laxative schedule*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='limit_marks',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Limit marks*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='location',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic flexure'), (6, 'Ascending'), (7, 'Cecum')], verbose_name='Location*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='lst_morphology',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], verbose_name='LST Morphology*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='lst_yn',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='LST yn*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='lymphatic_invasion',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Lymphatic invasion**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='maximum_size_mm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Maximum size (mm)*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='nbi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='NBI/FICE/electronic chromoendoscopy*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='nbi_nice',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], verbose_name='NICE*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(blank=True, null=True, max_length=128, verbose_name='Active ingredients anticoagulant/antiaggregant*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='non_lifting_sign',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Non lifting sign*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='number_clips_needed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of clips needed*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='number_of_sessions',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], verbose_name='Number of endoscopic sessions needed*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='other_coagulopathies',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Other coagulopathies*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='other_complications_comments',
            field=models.TextField(blank=True, null=True, max_length=500, verbose_name='Other complications comments*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Pain requiring medical intervantion*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='paris_calif',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], verbose_name='Paris Clasif.*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='perforation',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: endoscopic resolution'), (2, 'Yes: surgical resolution')], verbose_name='Perforation*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='perineural_invasion',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Perineural invasion**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='platelets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, '>150.000'), (1, '150.000-50.000'), (2, '< 50.000')], verbose_name='Platelets*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='pps',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Post polypectomy syndrome*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Adenoma'), (2, 'Serrated')], verbose_name='Prepathologic endoscopic diagnost 1*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], verbose_name='Prepathologic endoscopic diagnost 2*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='previous_attempt',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous attempt*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='previous_biopsy',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous biopsy*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], verbose_name='Recurrence 3-6 months c*ontrol'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='recurrenec_one_year_control',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], verbose_name='Recurrence 1 year c*ontrol'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='resection',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloc incomplete')], verbose_name='Resection*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='sclerous_wall_change',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Sclerous wall change*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='sedation',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], verbose_name='S*edation'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='sex',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Male'), (2, 'Female')], verbose_name='Sex*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='snare_tip_soft_coagulation',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Snare tip soft coagulation*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='successful_treatment',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No (surgery)'), (1, 'Yes (endoscopic treatment)')], verbose_name=' Successful t*reatment'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='surgery',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Not needed'), (1, 'Primary for technical reasons'), (2, 'Primary for suspected invasiveness'), (3, 'Due to bleeding (after EMR)'), (4, 'Due to perforation (after EMR)'), (5, 'Histological reasons (after EMR)'), (6, 'Clinical/patient decision (after EMR)')], verbose_name='Surgery*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(blank=True, null=True, verbose_name='Time of procedure (m)*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='transfusion',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Transfusion*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='treatment_of_residual_polyp',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 'Not necessary'), (2, 'APC'), (3, 'Snare tip coagulation'), (4, 'Cold avulsion plus coagulation'), (5, 'Hot avulsion'), (6, 'KAR (knife assisted resection)')], verbose_name='Treatment of residual polyp*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='vascular_invasion',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Vascular invasion**'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='visible_scar',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Visible scar*'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='anticoagulants',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Aspirin'), (2, 'Clopidogrel'), (3, 'Other antiaggregant'), (4, 'Warfarin'), (5, 'NSAID'), (6, '2 NSAID including aspiring or not'), (7, 'Aspirin+clopidogrel'), (8, 'NACOs')], verbose_name='Anticoagulants'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='immediate_bleeding',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact (treatment needed)'), (2, 'Yes: during exploration without clinical impact')], verbose_name='Immediate bleeding'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='laxative',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '4 litre polyethylene glycol (Bohm, Casenglicol...)'), (2, 'Polyethylene gylcol plus ascorbate: 2 litres (Moviprep...)'), (3, 'Sodium picosulfate, magnesium citrate (Citrafleet...)'), (4, 'Fosfates (Fosfosoda...)'), (5, 'Sulfates (Eziclen...)')], verbose_name='Laxative'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(blank=True, null=True, max_length=128, verbose_name='Active ingredients anticoagulant/antiaggregant'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='number_of_sessions',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], verbose_name='Number of endoscopic sessions needed'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='surgery',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Not needed'), (1, 'Primary for technical reasons'), (2, 'Primary for suspected invasiveness'), (3, 'Due to bleeding (after EMR)'), (4, 'Due to perforation (after EMR)'), (5, 'Histological reasons (after EMR)'), (6, 'Clinical/patient decision (after EMR)')], verbose_name='Surgery'),
        ),
    ]
