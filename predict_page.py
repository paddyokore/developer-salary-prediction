# import the necessary packages
import streamlit as sl
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# load the prediction model
def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

dt = data['model'] # load model
le = data['le_target'] # load target label encoder

def show_predict_page():
    sl.title("Developer Salary Prediction")

    sl.write("""### Please enter the required information for salary prediction""")

    Code_Certifications = (
        'None of the Above', 'Coursera', 
        'Udemy', 'Other', 'Codecademy', 
        'Pluralsight', 'edX', 'Udacity')
    
    Employment_Status = (
        'Employed, full-time', 'Student, full-time', 'Student, part-time', 
        'Not employed, but looking for work', 
        'Independent contractor, freelancer, or self-employed', 
        'Employed, part-time', 'Not employed, and not looking for work', 
        'Retired', 'I prefer not to say')
    
    PurchaseInfluence = (
        'None of the Above', 'I have some influence', 
        'I have little or no influence', 
        'I have a great deal of influence')
    
    countries = (
        'Canada',
        'United Kingdom of Great Britain and Northern Ireland',
        'Israel',
        'United States of America',
        'Germany',
        'India',
        'Netherlands',
        'Croatia',
        'Australia',
        'Russian Federation',
        'Czech Republic',
        'Austria',
        'Serbia',
        'Italy',
        'Ireland',
        'Poland',
        'Slovenia',
        'Iraq',
        'Sweden',
        'Madagascar',
        'Norway',
        'Taiwan',
        'Hong Kong (S.A.R.)',
        'Mexico',
        'France',
        'Brazil',
        'Lithuania',
        'Uruguay',
        'Denmark',
        'Spain',
        'Turkey',
        'South Africa',
        'Ukraine',
        'Finland',
        'Romania',
        'Portugal',
        'Singapore',
        'Oman',
        'Belgium',
        'Chile',
        'Bulgaria',
        'Latvia',
        'Philippines',
        'Greece',
        'Belarus',
        'Saudi Arabia',
        'Kenya',
        'Switzerland',
        'Iceland',
        'Viet Nam',
        'Thailand',
        'China',
        'Montenegro',
        'Slovakia',
        'Japan',
        'Luxembourg',
        'Argentina',
        'Hungary',
        'Tunisia',
        'Bangladesh',
        'Maldives',
        'Dominican Republic',
        'Egypt',
        'Jordan',
        'Pakistan',
        'Nepal',
        'Iran, Islamic Republic of...',
        'Indonesia',
        'Ecuador',
        'Bosnia and Herzegovina',
        'Armenia',
        'Colombia',
        'Kazakhstan',
        'South Korea',
        'Costa Rica',
        'Honduras',
        'Mauritius',
        'Estonia',
        'Algeria',
        'Trinidad and Tobago',
        'Mali',
        'Morocco',
        'Swaziland',
        'New Zealand',
        'The former Yugoslav Republic of Macedonia',
        'Afghanistan',
        'Cyprus',
        'United Arab Emirates',
        'Peru',
        'Uzbekistan',
        'Ethiopia',
        'Bahrain',
        'Malta',
        'Nicaragua',
        'Andorra',
        'Republic of Korea',
        'Lebanon',
        'Belize',
        'Zambia',
        'Bolivia',
        'Malaysia',
        'Sri Lanka',
        "Lao People's Democratic Republic",
        'Guatemala',
        'Azerbaijan',
        'Suriname',
        'El Salvador',
        'Syrian Arab Republic',
        'Qatar',
        'Nigeria',
        'Kyrgyzstan',
        'Zimbabwe',
        'Rwanda',
        'Georgia',
        'Cambodia',
        'Malawi',
        'Yemen',
        'Fiji',
        'Nomadic',
        'Uganda',
        'Albania',
        'Timor-Leste',
        'Mongolia',
        'Republic of Moldova',
        'Tajikistan',
        'Ghana',
        'United Republic of Tanzania',
        'Myanmar',
        'Kuwait',
        'Cameroon',
        'Kosovo',
        'Jamaica',
        'Turkmenistan',
        'Benin',
        'Botswana',
        'Niger',
        'Palestine',
        'Cape Verde',
        'Libyan Arab Jamahiriya',
        'Venezuela, Bolivarian Republic of...',
        'Senegal',
        'Cuba',
        'Togo',
        'Angola',
        'Isle of Man',
        'Panama',
        'Bahamas',
        'Paraguay',
        'Sudan',
        'Liberia',
        'Bhutan',
        'Democratic Republic of the Congo',
        "Côte d'Ivoire",
        'Barbados',
        'Congo, Republic of the...',
        'Namibia',
        'Somalia',
        'Sierra Leone',
        'Mozambique',
        'Lesotho',
        'Chad',
        'North Korea',
        'Antigua and Barbuda',
        'Papua New Guinea',
        'Palau',
        'Guinea',
        'Haiti',
        'Gabon',
        'Mauritania',
        'San Marino',
        'Guyana',
        'Saint Lucia',
        'Burkina Faso',
        'Brunei Darussalam',
        'Gambia',
        'Monaco',
        'Djibouti',
        'Seychelles',
        'Solomon Islands',
        'Saint Kitts and Nevis')
    
    education_levels = (
        'Something else', "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)", 
        "Bachelor’s degree (B.A., B.S., B.Eng., etc.)", 
        "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)", 
        "Some college/university study without earning a degree", "Primary/elementary school", 
        "Other doctoral degree (Ph.D., Ed.D., etc.)", "Associate degree (A.A., A.S., etc.)", 
        "Professional degree (JD, MD, etc.)")
    
    Remote_vs_Onsite = ('Fully remote', 'Hybrid (some remote, some in-person)', 
           'None of the Above', 'Full in-person')
    DevType = (
        'None of the Above', 'Data scientist or machine learning specialist', 
        'Developer, full-stack', 'Developer, front-end', 'Developer, back-end', 
        'Developer, desktop or enterprise applications', 'Engineering manager', 
        'Engineer, data', 'Student', 'Other (please specify):', 'Engineer, site reliability', 
        'Developer, mobile', 'Marketing or sales professional', 
        'Developer, embedded applications or devices', 'DevOps specialist', 'Designer', 
        'Database administrator', 'System administrator', 'Developer, QA or test', 
        'Product manager', 'Project manager', 'Data or business analyst', 
        'Senior Executive (C-Suite, VP, etc.)', 'Security professional', 'Educator', 
        'Academic researcher', 'Developer, game or graphics', 'Cloud infrastructure engineer', 
        'Scientist' )
    
    Languages = ('JavaScript', 'C#', 'C++', 'C', 'Bash/Shell', 'Delphi', 'Elixir', 'HTML/CSS', 
                 'Python', 'VBA', 'Dart', 'MATLAB', 'Java', 'Haskell', 'Assembly', 'Groovy', 
                 'Go', 'APL', 'Crystal', 'PHP', 'Clojure', 'Erlang', 'Rust', 'Ruby', 'Perl', 
                 'Kotlin', 'TypeScript', 'SQL', 'Lua', 'COBOL', 'PowerShell', 'LISP', 'Scala', 
                 'Objective-C', 'F#')
    
    Developer_Description = (
        'I am a developer by profession', 
        'I am not primarily a developer, but I write code sometimes as part of my work', 
        'I code primarily as a hobby', 'I am learning to code', 
        'I used to be a developer by profession, but no longer am')
    
    # Mapping Purchace Influence
    PI = {'None of the Above': 0, 'I have little or no influence': 1, 
          'I have some influence': 2, 'I have a great deal of influence': 3}
    # Mapping Education Level
    EL = {'Something else': 0, 'Primary/elementary school': 1, 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 2,
      'Some college/university study without earning a degree': 3, 'Associate degree (A.A., A.S., etc.)':4, 'Bachelor’s degree (B.A., B.S., B.Eng., etc.)':5,
      'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)':6, 'Professional degree (JD, MD, etc.)':7, 'Other doctoral degree (Ph.D., Ed.D., etc.)':8}
    
    # Mapping Employment status
    ES = {'Employed, full-time':8,'Student, full-time': 1, 'Independent contractor, freelancer, or self-employed': 6,'Student, part-time': 2,'Not employed, but looking for work':5,
      'Employed, part-time':7,'Not employed, and not looking for work':3,'I prefer not to say':4, 'Retired':0}
    
    # Mapping Code Certifications
    CC = {'None of the Above': 0, 'Udemy': 1, 'Coursera': 2, 'Other': 3, 'Codecademy':4, 'Pluralsight':5,
      'edX':6, 'Udacity':7, 'Skillsoft':8}
    
    # Mapping Countries
    country_code = {'Canada': 0, 'United Kingdom of Great Britain and Northern Ireland': 1,
                'Israel': 2, 'United States of America': 3, 'Germany': 4, 'India': 5,
                'Netherlands': 6, 'Croatia': 7, 'Australia': 8, 'Russian Federation': 9,
                'Czech Republic': 10, 'Austria': 11, 'Serbia': 12, 'Italy': 13, 'Ireland': 14,
                'Poland': 15, 'Slovenia': 16, 'Iraq': 17, 'Sweden': 18, 'Madagascar': 19, 'Norway': 20,
                'Taiwan': 21, 'Hong Kong (S.A.R.)': 22, 'Mexico': 23, 'France': 24, 'Brazil': 25,
                'Lithuania': 26, 'Uruguay': 27, 'Denmark': 28, 'Spain': 29, 'Turkey': 30,
                'South Africa': 31, 'Ukraine': 32, 'Finland': 33, 'Romania': 34, 'Portugal': 35,
                'Singapore': 36, 'Oman': 37, 'Belgium': 38, 'Chile': 39, 'Bulgaria': 40, 'Latvia': 41,
                'Philippines': 42, 'Greece': 43, 'Belarus': 44, 'Saudi Arabia': 45, 'Kenya': 46,
                'Switzerland': 47, 'Iceland': 48, 'Viet Nam': 49, 'Thailand': 50, 'China': 51,
                'Montenegro': 52, 'Slovakia': 53, 'Japan': 54, 'Luxembourg': 55, 'Argentina': 56,
                'Hungary': 57, 'Tunisia': 58, 'Bangladesh': 59, 'Maldives': 60,
                'Dominican Republic': 61, 'Egypt': 62, 'Jordan': 63, 'Pakistan': 64, 'Nepal': 65,
                'Iran, Islamic Republic of...': 66, 'Indonesia': 67, 'Ecuador': 68,
                'Bosnia and Herzegovina': 69, 'Armenia': 70, 'Colombia': 71, 'Kazakhstan': 72,
                'South Korea': 73, 'Costa Rica': 74, 'Honduras': 75, 'Mauritius': 76, 'Estonia': 77,
                'Algeria': 78, 'Trinidad and Tobago': 79, 'Mali': 80, 'Morocco': 81, 'Swaziland': 82,
                'New Zealand': 83, 'The former Yugoslav Republic of Macedonia': 84,
                'Afghanistan': 85, 'Cyprus': 86, 'United Arab Emirates': 87, 'Peru': 88,
                'Uzbekistan': 89, 'Ethiopia': 90, 'Bahrain': 91, 'Malta': 92, 'Nicaragua': 93,
                'Andorra': 94, 'Republic of Korea': 95, 'Lebanon': 96, 'Belize': 97, 'Zambia': 98,
                'Bolivia': 99, 'Malaysia': 100, 'Sri Lanka': 101,
                "Lao People's Democratic Republic": 102, 'Guatemala': 103, 'Azerbaijan': 104,
                'Suriname': 105, 'El Salvador': 106, 'Syrian Arab Republic': 107, 'Qatar': 108,
                'Nigeria': 109, 'Kyrgyzstan': 110, 'Zimbabwe': 111, 'Rwanda': 112, 'Georgia': 113,
                'Cambodia': 114, 'Malawi': 115, 'Yemen': 116, 'Fiji': 117, 'Nomadic': 118, 'Uganda': 119,
                'Albania': 120, 'Timor-Leste': 121, 'Mongolia': 122, 'Republic of Moldova': 123,
                'Tajikistan': 124, 'Ghana': 125, 'United Republic of Tanzania': 126, 'Myanmar': 127,
                'Kuwait': 128, 'Cameroon': 129, 'Kosovo': 130, 'Jamaica': 131, 'Turkmenistan': 132, 'Benin': 133,
                'Botswana': 134, 'Niger': 135, 'Palestine': 136, 'Cape Verde': 137,
                'Libyan Arab Jamahiriya': 138, 'Venezuela, Bolivarian Republic of...': 139,
                'Senegal': 140, 'Cuba': 141, 'Togo': 142, 'Angola': 143, 'Isle of Man': 144, 'Panama': 145,
                'Bahamas': 146, 'Paraguay': 147, 'Sudan': 148, 'Liberia': 149, 'Bhutan': 150,
                'Democratic Republic of the Congo': 151, "Côte d'Ivoire": 152, 'Barbados': 153,
                'Congo, Republic of the...': 154, 'Namibia': 155, 'Somalia': 156, 'Sierra Leone': 157,
                'Mozambique': 158, 'Lesotho': 159, 'Chad': 160, 'North Korea': 161,
                'Antigua and Barbuda': 162, 'Papua New Guinea': 163, 'Palau': 164, 'Guinea': 165,
                'Haiti': 166, 'Gabon': 167, 'Mauritania': 168, 'San Marino': 169, 'Guyana': 170,
                'Saint Lucia': 171, 'Burkina Faso': 172, 'Brunei Darussalam': 173, 'Gambia': 174,
                'Monaco': 175, 'Djibouti': 176, 'Seychelles': 177, 'Solomon Islands': 178,
                'Saint Kitts and Nevis': 179}
    
    # Mapping Remote_vs_Onsite
    RO = {'Fully remote': 0, 'Hybrid (some remote, some in-person)': 1, 'None of the Above': 2, 'Full in-person': 3}

    # Mapping LanguageHaveWorkedWith
    programming_lang = {'JavaScript':42, 'HTML/CSS':41, 'SQL':40, 'Python':39, "TypeScript":38, 'Java':37, "Bash/Shell":36, "C#":35,
                    'C++':34, "PHP":33, "C":32, "PowerShell":31, "Go":30, "Rust":29, "Kotlin":28, "Dart":27, "Ruby":26, "Assembly":25,
                    "Swift":24, "R":23, "VBA":22, "MATLAB":21, "Lua":20, "Groovy":19, "Delphi":18, "Scala":17, "Objective-C":16,
                    "Perl":15, "Haskell":14, "Elixir":13, "Julia":12, "Clojure":11, 'Solidity':10, "LISP":9, 'F#':8, 'Fortran':7,
                    "Erlang":6, "APL":5, "COBOL":4, "SAS":3, "OCaml":2, "Crystal":1}
    
    # Mapping Developer Description
    dev_desc = {'I am a developer by profession': 0, 'I am learning to code': 1, 'I am not primarily a developer, but I write code sometimes as part of my work': 2,
            'I code primarily as a hobby': 3, 'I used to be a developer by profession, but no longer am':4}
    
    # Mapping Developer Type
    dev_type = {'Developer, full-stack':16, 'Developer, front-end':15,'Developer, back-end':14,'None of the Above':0,'Data scientist or machine learning specialist':27,'Engineer, data':26,'Developer, mobile':17,
        'Developer, desktop or enterprise applications':18,'Student':2,'Other (please specify):':1,'Engineer, site reliability':20,
        'Engineering manager':25,'Developer, embedded applications or devices':19,
        'Academic researcher':3,'DevOps specialist':12,
        'Developer, QA or test':28,'Educator':6,'Senior Executive (C-Suite, VP, etc.)':29,'Data or business analyst':21,'Project manager':11,
        'Developer, game or graphics':22,'System administrator':10,'Cloud infrastructure engineer':23,'Database administrator':7,'Product manager':9,
        'Security professional':24,'Scientist':13,'Designer':5,'Marketing or sales professional':4,'Blockchain':8}

    role = 'Please select the role you would like to apply for'
    educ = 'What is your level of education?'
    cert = 'What online courses or certifications did you use to learn to code?'
    job = 'What is your employment status?'
    decide = 'Please choose your level of influence in decision making in an organization?'
    live = 'Where do you live?'
    years = 'How many years of work experience do you have?'
    locate = 'Would you like to apply for remote or onsite jobs?'
    lang = 'Which of the following langages have you worked with before?'
    devdesc = ('Which of the following statements describes you?')

    DevType = sl.selectbox(role, DevType)
    Education_Level = sl.selectbox(educ, education_levels)
    Code_Certifications = sl.selectbox(cert, Code_Certifications)
    Employment_Status = sl.selectbox(job, Employment_Status)
    PurchaseInfluence = sl.selectbox(decide, PurchaseInfluence)
    Country = sl.selectbox(live, countries)
    Pro_Experience = sl.slider(years, 0, 50, 3)
    Remote_vs_Onsite = sl.selectbox(locate, Remote_vs_Onsite)
    Languages = sl.selectbox(lang, Languages)
    Developer_Description = sl.selectbox(devdesc, Developer_Description)

   

    

    ok = sl.button("Predict Salary")
    if ok:
        vals = [DevType, Education_Level, Code_Certifications,  
                Employment_Status, PurchaseInfluence, Country, 
                Pro_Experience, Remote_vs_Onsite, Languages, Developer_Description]
        col = ['DevType', 'Education_Level', 'Code_Certifications',  
               'Employment_Status', 'PurchaseInfluence', 'Country', 
               'Pro_Experience', 'Remote_vs_Onsite', 'LanguageHaveWorkedWith', 'Developer_Description']
        testdf = pd.DataFrame([vals], columns=col)# test data
        # encode test data
        testdf['PurchaseInfluence'] = testdf['PurchaseInfluence'].map(PI)
        testdf['Education_Level'] = testdf['Education_Level'].map(EL)
        testdf['Employment_Status'] = testdf['Employment_Status'].map(ES)
        testdf['Code_Certifications'] = testdf['Code_Certifications'].map(CC)
        testdf['Country'] = testdf['Country'].map(country_code)
        testdf['Remote_vs_Onsite'] = testdf['Remote_vs_Onsite'].map(RO)
        testdf['LanguageHaveWorkedWith'] = testdf['LanguageHaveWorkedWith'].map(programming_lang)
        testdf['Developer_Description'] = testdf['Developer_Description'].map(dev_desc)
        testdf['DevType'] = testdf['DevType'].map(dev_type)

        # reind 
        testdf = testdf.reindex(columns=['Code_Certifications', 'Education_Level', 'Employment_Status',
       'PurchaseInfluence', 'Country', 'Pro_Experience', 'Remote_vs_Onsite',
       'DevType', 'LanguageHaveWorkedWith', 'Developer_Description'])
                
        response = dt.predict(testdf) # predict salary
        sl.subheader(f'The predicted annual salary is: {le.inverse_transform(response)[0]}') # output prediction


