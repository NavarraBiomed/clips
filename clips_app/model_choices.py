
# Choices for model Clips
_SEX = (
	(1, "Male"),
	(2, "Female")
	)

_TRAMOS_EDAD = (
	(1, "< 60"),
	(2, "60-74"),
	(3, ">= 75")
	)

_ASA = (
	(1, "I"),
	(2, "II"),
	(3, "III"),
	(4, "IV")
	)

_NO_YES = (
	(0, "No"),
	(1, "Yes")
	)

_ASPIRIN = (
	(0, "No"),
	(1, "100mg cease"),
	(2, "300mg cease"),
	(3, "100mg during EMR"),
	(4, "300mg during EMR")
	)

_ANTICOAGULANT = (
	(0, "No"),
	(1, "Aspirin"),
	(2, "Clopidogrel"),
	(3, "Other antiagregant"),
	(4, "Warfarin"),
	(5, "NSAID"),
	(6, "2 NSAID including aspiring or not"),
	(7, "Aspirin+clopidogrel"),
	(8, "NACOs")
	)

_ANTIPLATELET = (
	(0, "No"),
	(1, "Antiplatelet"),
	(2, "Double antiplatelet"),
	(3, "Warfarin acenocumarol"),
	(4, "Dabigatran (new antic)")
	)

_PARIS = (
	(1, "0Is"),
	(2, "0IIa"),
	(3, "0IIa+0Is"),
	(4, "0Is+0IIa"),
	(5, "0IIb"),
	(6, "0IIc"),
	(7, "0IIa+0IIc"),
	(8, "0IIb+0IIc"),
	(9, "0IIb+0IIa")
	)

_MORPHOLOGY = (
	(1, "Granular homogeneous"),
	(2, "Focal nodular mixed type"),
	(3, "Whole nodular mixed type"),
	(4, "Flat elevated"),
	(5, "Psudodepressed")
	)

_LOCATION = (
	(1, "Rectum"),
	(2, "Left colon"),
	(3, "Splenic flexure"),
	(4, "Transverse"),
	(5, "Hepatic"),
	(6, "Ascendent"),
	(7, "Cecum")
	)

_HIGH_DEFINITION = (
	(1, "Conventional endoscope"),
	(2, "High definition"),
	(3, "Optic magnification")
	)

_NBI_SANO = (
	(1, "I"),
	(2, "II"),
	(3, "IIIA"),
	(4, "IIIB")
	)

_NBI_NICE = (
	(1, "Type 1"),
	(2, "Type 2"),
	(3, "Type 3")
	)

_KUDO = (
	(1, "I"),
	(2, "II"),
	(3, "IIIS"),
	(4, "IIIL"),
	(5, "IV"),
	(6, "V-I"),
	(7, "V-N")
	)

_PED_A = (
	(1, "Adenoma"),
	(2, "Serrated")
	)

_PED_B = (
	(1, "NodisplasiaToSuperficial submucosal carcinoma"),
	(2, "Deep submucosal carcinoma")
	)

_HISTOLOGY = (
	(1, "Adenoma"),
	(2, "HGD-intraepitelial carcinoma in adenoma"),
	(3, "Intramucosal carcinoma in adenoma"),
	(4, "Superficial submucosal carcinoma in adenoma"),
	(5, "Deep submucosal carcinoma in adenoma"),
	(6, "Hyperplastic"),
	(7, "Sesil Serrated polyp"),
	(8, "Traditional Serrated Adenoma"),
	(9, "Polyp Serrated Mixed or serrated polyp with dysplasia"),
	(10, "Intraepitelial carcinoma Any serrated"),
	(11, "Intramucosal carcinoma Any serrated"),
	(12, "Superficial submucosa carc. Any serrated"),
	(13, "Deep submucosa carc. Any serrated"),
	(14, "Carinoid")
	)

_HISTOLOGY_SIMP = (
	(1, "Adenoma"),
	(2, "HGD-Imucosal"),
	(3, "Invasive adenoma"),
	(4, "Serrated"),
	(5, "HGD-Imucosal serrated"),
	(6, "Invasive serrated"),
	(7, "Carcinoid")
	)

_DIFFICULTY = (
	(1, "Easy"),
	(2, "Medium"),
	(3, "Difficult")
	)

_RESECTION = (
	(1, "Piecemeal complete"),
	(2, "Piecemeal incomplete"),
	(3, "En bloc R0"),
	(4, "En bloq incomplete")
	)

_RESECTION_YN = (
	(1, "Piecemeal"),
	(2, "En bloc")
	)

_TECHNIQUE = (
	(1, "EMR"),
	(2, "Hybrid-EMR")
	)

_TECHNIQUE_TWO = (
	(1, "One-step"),
	(2, "Two-steps")
	)

_MARKS = (
	(0, "No marks"),
	(1, "APC marks")
	)

_INJECTION = (
	(0, "No"),
	(1, "Saline"),
	(2, "Glicerin"),
	(3, "Hyaluronic"),
	(4, "Hidrox-propil-cellulose: VOLUVEN(r)"),
	(5, "Gelafundin"),
	(6, "Others")
	)

_ENDOCUT = (
	(1, "Only cut current"),
	(2, "Only coagulation current"),
	(3, "Endocut/Blended")
	)

_POLYP_RETRIEVAL = (
	(1, "Roth net"),
	(2, "By aspiration"),
	(3, "Both methods"),
	(4, "By snare")
	)

_ARGON_PC = (
	(0, "No"),
	(1, "Yes: incomplete resection"),
	(2, "Yes: coagulation"),
	(3, "Yes: per protocol")
	)

_CLIPS = (
	(0, "Control group"),
	(1, "Treatment group")
	)

_CLIPS_CONTROL = (
	(0, "No"),
	(1, "Punctual coagulation")
	)

_CLIPS_TREAT_GROUP = (
	(1, "Complete closure with complete mucosal apposition"),
	(2, "Complete closure without complete mucosal apposition"),
	(3, "Total failed closure"),
	(4, "Partial failed closure"),
	(5, "Closure not tried")
	)

_NOT_TRIED = (
	(1, "Big size"),
	(2, "Difficult location"),
	(3, "Both")
	)

_CLOSURE_TECHNIQUE = (
	(1, "Simple clipping"),
	(2, "Clip-Poly loop"),
	(3, "Clip Silk loop")
	)

_PERFORATIOM = (
	(0, "No"),
	(1, "Yes: endoscopic resolution"),
	(2, "Yes: surgical resolution")
	)

_SURGERY_BY_COMPLICATION = (
	(0, "No"),
	(1, "Yes: bleeding"),
	(2, "Yes: perforation")
	)

_BLEEDING = (
	(0, "No"),
	(1, "During no clinical impact-autol"),
	(2, "During exploration with clinical impact"),
	(3, "24h"),
	(4, "24-48h"),
	(5, "3-7 days"),
	(6, ">7 days")
	)

_IMMEDIATE_BLEEDING = (
	(0, "No"),
	(1, "Yes: during exploration with clinical impact"),
	(2, "Yes: during exploration without clinical impact")
	)

_BLEEDING_TREATMENT = (
	(0, "No"),
	(1, "Inyection"),
	(2, "Clipping"),
	(3, "ArgonPC"),
	(4, "Coagulation forceps"),
	(5, "2 methods")
	)

_FEVER = (
	(0, "No"),
	(1, "37-37.9"),
	(2, "38 or more")
	)

_SUCCESSFUL_TREATMENT = (
	(0, "No: surgical treatment"),
	(1, "Yes: in 1 session (includes one or two steps"),
	(2, "Yes, in 2 or more sessions (one session and treatment in controls")
	)

_SEDATION = (
	(0, "Without sedation"),
	(1, "By gastroenterologist other than Propofol"),
	(2, "By gastroenterologist based on Propofol"),
	(3, "By anesthesiologist")
	)

_RECURRENCE_THREE_SIX = (
	(0, "No"),
	(1, "Yes: positive biopsy: endoscopic treatment"),
	(2, "Yes: visible recurrence: endoscopic treatment"),
	(3, "Yes: surgical treatment needed")
	)

_RECURRENCE_ONE_YEAR = (
	(0, "No"),
	(1, "Yes: positive biopsy: endoscopic treatment"),
	(2, "Yes: visible recurrence: endoscopic treatment"),
	(3, "Yes: surgical treatment needed")
	)

_ENDOCUT_MODE = (
	(1, "1"),
	(2, "2"),
	(3, "3"),
	(4, "4")
	)

_COAGULATION = (
	(0, "Soft"),
	(1, "Force")
	)
