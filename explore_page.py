import streamlit as sl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import seaborn as sns
sns.set_style('dark')
import warnings
warnings.filterwarnings('ignore')

def rename(data):

    # import text doc with old and new col names
    cols = pd.read_csv(r'cols.txt', sep='\t')

    # create a dictionary with the cols df
    cols_dict = dict(zip(cols['Old'], cols['New']))

    # rename cols in the dataframe
    df = data.rename(columns = cols_dict)

    return df

# function to drop rows with more than 50% missing values
def drop_50(data):
    threshold = len(data.columns) * 0.5  # 50% of total columns
    data = data.dropna(thresh=threshold)

    return data

def replace_yesna(data, columns_range, valuefill):
    # Replace 'NA' with 'not answered' in the specified range of columns
    data[columns_range] = data[columns_range].fillna(valuefill)
    return data

# Function to rename values in the 'Experience' column
def rename_values(df, column):
    df[column] = df[column].replace({'Less than 1 year': 0.5, 'More than 50 years': 50})
    return df

# Code to extract first mentions
def extract_first_value_from_columns(df, columns):
    first_values = {}
    for col in columns:
        first_values[col] = df[col].apply(lambda x: x.split(";")[0].strip() if isinstance(x, str) and ";" in x else x)
    return pd.DataFrame(first_values)

# load the data only once, instead of every time you run code
def load_data():
    finalf=  ['Code_Certifications', 'Education_Level', 'Employment_Status',
            'PurchaseInfluence', 'Country', 'Pro_Experience', 'Remote_vs_Onsite',
            'DevType', 'LanguageHaveWorkedWith', 'Developer_Description', 
            'Gender', 'Age', 'Annual_Salary', 'continents']

    df = pd.read_csv("survey_results_public.csv")
    continents = {
        'Asia': ['Israel', 'Hong Kong (S.A.R.)', 'India', 'China', 'Singapore', 'Iraq',
                 'Philippines', 'Iran, Islamic Republic of...', 'Indonesia', 'Afghanistan',
                 'Viet Nam', 'South Korea', 'Taiwan', 'Japan', 'Thailand', 'Bangladesh',
                 'Nepal', 'United Arab Emirates', 'Pakistan', 'Sri Lanka', 'Azerbaijan',
                 'Uzbekistan', 'Kazakhstan', 'North Korea', 'Timor-Leste', 'Brunei Darussalam',
                 'Oman', 'Saudi Arabia', 'Maldives', 'Jordan', 'Bahrain', 'Republic of Korea',
                'Lebanon', 'Malaysia', "Lao People's Democratic Republic", 'Syrian Arab Republic',
                'Qatar', 'Kyrgyzstan', 'Cambodia', 'Yemen', 'Mongolia', 'Tajikistan', 'Myanmar',
                'Kuwait', 'Turkmenistan', 'Palestine', 'Bhutan'],
        'Oceania': ['Australia', 'New Zealand', 'Fiji', 'Solomon Islands', 'Papua New Guinea',
                    'Palau'],
        'North America': ['Canada', 'United States of America', 'Mexico', 'Dominican Republic',
                         'Costa Rica', 'Nicaragua', 'Belize', 'Guatemala', 'El Salvador',
                         'Jamaica', 'Cuba', 'Panama', 'Bahamas', 'Barbados', 'Antigua and Barbuda',
                          'Haiti', 'Saint Lucia', 'Saint Kitts and Nevis'],
        'Europe': ['Croatia', 'Netherlands', 'Czech Republic', 'Sweden', 'Denmark',
                   'Finland', 'United Kingdom of Great Britain and Northern Ireland',
                   'Austria', 'France', 'Portugal', 'Belgium', 'Ireland', 'Iceland',
                   'Montenegro', 'Germany', 'Belarus', 'Switzerland', 'Poland',
                   'Ukraine', 'Russia', 'Serbia', 'Luxembourg', 'Spain', 'Norway',
                   'Romania', 'Italy', 'Turkey', 'Greece', 'Hungary', 'Malta',
                   'Estonia', 'Slovenia', 'Bosnia and Herzegovina', 'Bulgaria',
                   'Georgia', 'Latvia', 'Lithuania', 'Moldova', 'Macedonia (FYROM)', 'Armenia',
                   'Monaco', 'Slovakia', 'Cyprus', 'Russian Federation',
                  'The former Yugoslav Republic of Macedonia', 'Andorra', 'Nomadic', 'Albania',
                  'Republic of Moldova', 'Kosovo', 'Isle of Man', 'San Marino'],
        'Africa': ['Madagascar', 'South Africa', 'Swaziland', 'Mali', 'Egypt', 'Nigeria',
                   'Tunisia', 'Cameroon', 'Ethiopia', 'Ghana', 'Rwanda', 'Senegal',
                   'Chad', 'Benin', 'Angola', 'Namibia', 'Malawi', 'Sierra Leone',
                   'Zimbabwe', 'Mauritius', 'Morocco', 'Kenya', 'Botswana', 'Liberia', 'Lesotho',
                   'Guinea', 'Gabon', 'Seychelles', 'Algeria', 'Zambia', 'Uganda',
                  'United Republic of Tanzania', 'Niger', 'Cape Verde', 'Libyan Arab Jamahiriya',
                  'Togo', 'Sudan', 'Democratic Republic of the Congo', "Côte d'Ivoire",
                  'Congo, Republic of the...', 'Somalia', 'Mozambique', 'Mauritania',
                  'Burkina Faso', 'Gambia', 'Djibouti'],
        'South America': ['Brazil', 'Argentina', 'Colombia', 'Chile', 'Peru',
                          'Venezuela, Bolivarian Republic of...', 'Bolivia', 'Paraguay',
                          'Ecuador', 'Uruguay', 'Honduras', 'Trinidad and Tobago', 'Suriname',
                         'Guyana']
        }
    
    # Create the 'continents' column by mapping the 'countries' column to the continents dictionary
    df['continents'] = pd.Series(df['Country']).map({country: continent for continent, countries in continents.items()
                                            for country in countries})
    df = rename(df)
    df = df[finalf]
    df = drop_50(df)
    df = replace_yesna(df, ['Code_Certifications', 'PurchaseInfluence', 'Remote_vs_Onsite', 'DevType'],'None of the Above')
    df = rename_values(df, 'Pro_Experience')
    df = replace_yesna(df, 'Gender','Prefer not to say')
    df = replace_yesna(df, 'Employment_Status','I prefer not to say')
    df = replace_yesna(df, 'Age','25-34 years old')
    df['Pro_Experience'].fillna(df['Pro_Experience'].median(), inplace=True)
    df = replace_yesna(df, 'Education_Level',"Something else")
    df = replace_yesna(df, 'LanguageHaveWorkedWith',"HTML/CSS")
    # data with cols of first mentions
    colslist = ['Code_Certifications', 'Employment_Status',  'DevType',  'LanguageHaveWorkedWith',  'Gender']
    zer = extract_first_value_from_columns(df, colslist)
    df[colslist] = zer

    # for those who don't work and have no salary
    # fill missing salary with 0
    nonwork = ['Student, full-time', 'Student, part-time',
        'Not employed, but looking for work',
    'Not employed, and not looking for work',
        'Retired', 'I prefer not to say']
    
    work = ['Employed, full-time', 'Independent contractor, freelancer, or self-employed', 'Employed, part-time']

    df.loc[(df['Employment_Status'].isin(nonwork)) & (df['Annual_Salary'].isna()), 'Annual_Salary'] = 0
    
    continent_mapping = {
    'Africa': 18126.0,
    'Asia': 23215.0,
    'Europe': 59720.0,
    'North America': 132000.0,
    'Oceania': 92002.0,
    'South America': 27008.5}

    new_column = df.groupby('continents')['Annual_Salary'].apply(lambda x: x.fillna(continent_mapping[x.name]))
    df['Annual_Salary'] = new_column.reset_index(level=0, drop=True)

    # replace nonsense salary for students, retired, no work
    df.loc[(df['Employment_Status'].isin(nonwork)) & (df['Annual_Salary'] != 0)
        & (df['Annual_Salary'] <= 5000), 'Annual_Salary'] = 0


    #replace workers with nonsense salary with null
    df.loc[(df['Employment_Status'].isin(work)) & (df['Annual_Salary'] != 0)
            & (df['Annual_Salary'] <= 5000), 'Annual_Salary'] = np.nan

    # replace nonsense salary for workers
    new_column1 = df.groupby('continents')['Annual_Salary'].apply(lambda x: x.fillna(continent_mapping[x.name]))
    df['Annual_Salary'] = new_column1.reset_index(level=0, drop=True)
    
    return df

df = load_data()

def show_explore_page():
    sl.title("Understand The Data")

    sl.write(
        """
        ### Stack Overflow Developer Survey 2022
        """)
    
    tab1, tab2, tab3, tab4, tab5 = sl.tabs(['\# of Developers', 'Annual Salary', 'Work Experience', 'Education', 'Online Certs'])
    
    with tab1:
        data = df["continents"].value_counts()

        sl.write("""#### Number of Developers By Continent""")

        sl.bar_chart(data)

    with tab2:
        sl.write(
            """
        #### Average Annual Salary in USD Per Continent
        """
        )

        
        data = df.groupby(["continents"])["Annual_Salary"].mean().sort_values(ascending=True)
        sl.bar_chart(data)

    with tab3:
        sl.write(
            """
        #### Years of Professional Experience
        """
        )

        data = [df[df['Pro_Experience'].astype('float') <= 20].Pro_Experience.astype('int')]
        group_labels = ['Work Experience in years']
        fig = ff.create_distplot(data, group_labels, bin_size=0.9, histnorm= '')
        fig.update_layout(showlegend=False, width=700, bargap=0.01)
        sl.plotly_chart(fig)

    with tab4:
        data = df["Education_Level"].value_counts()

        sl.write("""#### Level of Education""")

        sl.bar_chart(data)    

    with tab5:
        data = df["Code_Certifications"].value_counts()


        sl.write("""#### Online Certifications""")

        sl.bar_chart(data) 