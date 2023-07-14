# developer-salary-prediction
This repository contains code and resources for predicting developer salaries. The goal of this project is to develop a model that can accurately predict the salary of a developer based on various features such as programming languages, experience level, education, and location.

Table of Contents
- [Project Background](#project-background)
- [Stakeholders](#stakeholders)
- [Business Understanding](#business-understanding)
- [Project Statement](#project-statement)
- [Objectives](#objectives)
- [Success Metrics](#success-metrics)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

  
Project Background

Africa’s Tech sector has become one of the fastest growing tech ecosystems in the world with tech being one of the fastest growing sectors in Africa. This has led to a rise in demand for jobs in the industry.
However, unlike other parts of the world, information on remuneration in these jobs remains hard to come by. Existing resources such as glassdoor and brighter monday have limited information on salaries in Africa.
Over the past few years, it has been observed that foreign companies enter the African Market, offering more competitive salaries compared to local companies resulting in mass movement of experienced developers into these new roles.
This project seeks to solve this problem by developing a platform that can predict developer salaries based on their personal information, and also, providing comparison between different incomes in different regions for similar roles.

Stakeholders

- Jobseekers
- Employers
- Recruitment agencies
  
Business Understanding

Salary negotiation can be a critical stage in the job search process, and job seekers often encounter various challenges during this phase like lack of information on salary trends. This means that a jobseeker might spend valuable time researching industry salary trends. Some might not be so lucky as the information might be non existent.
As the Tech labour market becomes more competitive, offering the right salary for new and current employees is crucial for employers as it means keeping or losing a valued resource. Thus it is imperative for them to offer fair and competitive compensation that is benchmarked to their industry
Our project looks at coming up with salary prediction model to help both jobseekers and employers with the above challenges. We will focus on the tech industry (developers) and use data from stackoverflow's annual developer survey.

Problem Statement

Our solution to the problem of inadequate salary data for both employees and employers is to develop a salary prediction model, to estimate salaries based on relevant job specifications. The model will assist in making informed decisions related to compensation and provide valuable insights for both job seekers and employers.
The salary prediction model will enable job seekers to have a better understanding of the salary expectations associated with their qualifications and experience. Employers can use the model to make informed decisions regarding fair compensation packages for new hires or salary adjustments for existing employees. Job sites like linkedin, glassdoor, brigther monday can use this model for jobs displayed on the sites by quoting the estimated salaries.

Objectives

- The main objective of this project is to come up with a salary rediction model that will:
- Enable Jobseekers to ask for competitive salaries during contract negotiations.
- Assist employers in offering fair compensation to their employees.
- Assist Recruitment agencies offer accurate salary estimates to their clients.

These objectives will be achieved through the following specific objectives:

- To select the most important features in the dataset to be used in Salary prediction.
- To describe how features such as Proffessional experience and Education level affect Annual compensation.
- To build multiple regression models and identify the most suitable model to be used in the prediction.
- To deploy the model using streamlit as an online dashboard.

Success Metrics

The metrics to be used to measure the success of the model are:
- Mean Absolute Error
- Root Mean Square Error
- Rsquared

For the regression model and;
- F1 score
- Precision
- Recall
- Accuracy score

For the classification model 

An Accuracy score of 75% or more on the training data and 70% on the test data will be considered a success.
  
Installation

To use the code in this repository, you need to have the following dependencies installed:

Python 3.7 or higher
Jupyter Notebook
Required Python libraries (numpy, pandas, scikit-learn, matplotlib, etc.)
You can install the required Python libraries by running the following command:

Data

The data comes from [stakoverflow annual developer survey](https://insights.stackoverflow.com/survey/) for 2022. Each row shows the responses given by a developer. It has 73268 rows and  79 columns. The data has missing values, but no duplicate rows. The target variable ConvertedCompYearly shows the annual salary for each developer.

Modeling

The modeling process involves building a classification model to predict developer salary ranges based on the available features. We explore various machine learning algorithms, such as logistic regression, decision trees, and random forests, to find the best-performing model.

Evaluation

The evaluation of the models is based on several metrics, including F1 score, Precision, Recall, and Accuracy score. The performance of the models is compared, and the model with the best performance which is Random Forest is selected as the final model.
![image](https://github.com/paddyokore/developer-salary-prediction/assets/93999002/31c46a96-c18f-4a70-984c-4f8dfbb81958)

Deployment

We use streamlit to delpoy..............(unfinished)

Contributing

Contributions to this project are welcome. If you have suggestions, bug fixes, or enhancements, please submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

