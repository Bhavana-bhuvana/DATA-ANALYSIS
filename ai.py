import re

# Keywords you want to search for
keywords = ["Python", "Java", "SQL", "machine learning","Communication","communication skills", "Collaboration", "Problem-solving", "Critical Thinking",
    "Attention to Detail"]

# Text to search
text = ("23andme, leading consumer genetics company, accumulated wealth genotypic "
        "phenotypic information participants committed improving human health "
        " genomics. therapeutics team uses data discover develop novel medicines treat "
        "important diseases. team currently research programs across several therapeutic areas,"
        " including oncology, skin, respiratory cardiovascular disease. seeking outstanding "
        ""
        "associate scientist senior associate scientist contribute generation, discovery"
        " characterization antibodies across therapeutics portfolio. information therapeutics team,"
        " please visit https //therapeutics.23andme.com/. handle aspects hybridoma workflow including "
        "performing fusions, clone picking hybridoma antibody screening develop establish novel methods "
        ""
        "improve current antibody discovery workflows antibody characterization including affinity specificity determination, epitope binning antibody sequencing collaborate therapeutic leads plan strategy antibody discovery interpret, record present complex biological data communicate collaborate colleagues effectively bring b.s. 5 years research experience industry academia, master 3 years research experience industry academia , phd molecular biology, cell biology related field strong technical expertise molecular biology including dna rna purification, diverse pcr methods rt pcr, race pcr , illumina miseq library preparation, cloning adept characterization protein protein interaction using variety methods elisa, facs, bio layer interferometry octet and/or surface plasmon resonance technology biacore cell biology expertise including mammalian cell culture, transfection running functional cell based assays excellent communication skills ability work independently team environment critical thinking high degree innovative analytical skills pluses experience using hybridoma technology antibody discovery including immunization, hybridoma fusion, clone picking screening experience applying single b cell antibody technologies antibody discovery e.g. single cell facs sorting, microfluidics note job title commensurate experience academic credentials. us 23andme, inc. leading consumer genetics research company. mission help people access, understand benefit human genome. company named mit technology review 50 smartest companies, 2017 list, named one fast company 25 brands matter now, 2017 . 23andme 10 million customers worldwide, ~80 percent customers consented participate research. 23andme, value diverse, inclusive workforce provide equal employment opportunity applicants employees. qualified applicants employment considered without regard individual race, color, sex, gender identity, gender expression, religion, age, national origin ancestry, citizenship, physical mental disability, medical condition, family care status, marital status, domestic partner status, sexual orientation, genetic information, military veteran status, basis protected federal, state local laws. unable submit application incompatible assistive technology disability, please contact us accomodations ext 23andme.com. 23andme reasonably accommodate qualified individuals disabilities extent required applicable law. please note 23andme accept agency resumes responsible fees related unsolicited resumes. thank you.")

# Create a regex pattern to match any of the keywords
pattern = r'\b(?:' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b'

# Search the text for matches
found_skills = re.findall(pattern, text, re.IGNORECASE)

print("Found Skills:", found_skills)
