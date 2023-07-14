developer-salary-prediction
This repository contains code and resources for predicting developer salaries. The goal of this project is to develop a model that can accurately predict the salary of a developer based on various features such as programming languages, experience level, education, and location.

Table of Contents
Business Overview
Stakeholders
Business Understanding
Project Statement
Objectives
Success Metrics
Installation
Usage
Data
Modeling
Evaluation
Deployment
Contributing
License

Business Overview
Syria Tel Company is a telecommunications company providing various services such as mobile, internet, and landline connections to customers in Syria. Customer churn, which is defined as customers quitting a service or transferring to a rival, is a worry for the business. Because it affects sales and client loyalty, churn is a major problem for the business. Your objective is to create a prediction model that can spot clients who are most likely to leave, allowing the business to take preventative action to keep them.

Stakeholders
Jobseekers
Employers
Recruitment agencies
Business Understanding
Salary negotiation can be a critical stage in the job search process, and job seekers often encounter various challenges during this phase like lack of information on salary trends. This means that a jobseeker might spend valuable time researching industry salary trends. Some might not be so lucky as the information might be non existent. As the Tech labour market becomes more competitive, offering the right salary for new and current employees is crucial for employers as it means keeping or losing a valued resource. Thus it is imperative for them to offer fair and competitive compensation that is benchmarked to their industry. Our project looks at coming up with salary prediction model to help both jobseekers and employers with the above challenges. We will focus on the tech industry (developers) and use data from stackoverflow's annual developer survey.

Project Statement
Our solution to the problem of inadequate salary data for both employees and employers is to develop a salary prediction model, to estimate salaries based on relevant job specifications. The model will assist in making informed decisions related to compensation and provide valuable insights for both job seekers and employers. The salary prediction model will enable job seekers to have a better understanding of the salary expectations associated with their qualifications and experience. Employers can use the model to make informed decisions regarding fair compensation packages for new hires or salary adjustments for existing employees. Job sites like LinkedIn, Glassdoor, Brighter Monday can use this model for jobs displayed on the sites by quoting the estimated salaries.

Objectives
The main objective of this project is to come up with a salary prediction model that will:

Enable jobseekers to ask for competitive salaries during contract negotiations.
Assist employers in offering fair compensation to their employees.
Assist recruitment agencies in offering accurate salary estimates to their clients.
These objectives will be achieved through the following specific objectives:

Select the most important features in the dataset to be used in salary prediction.
Describe how features such as professional experience and education level affect annual compensation.
Build multiple regression models and identify the most suitable model to be used in the prediction.
Deploy the model using Streamlit as an online dashboard.
Success Metrics
The metrics to be used to measure the success of the model are:

Mean Absolute Error
Root Mean Square Error
R-squared
For the regression model, and:

F1 score
Precision
Recall
Accuracy score
For the classification model.

An accuracy score of 75% or more on the training data and 70% on the test data will be considered a success.

Installation
To use the code in this repository, you need to have the following dependencies installed:

Python 3.7 or higher
Jupyter Notebook
Required Python libraries (numpy, pandas, scikit-learn, matplotlib, etc.)
You can install the required Python libraries by running the following command:

Copy code
pip install -r requirements.txt
Usage
To run the code and reproduce the analysis, follow these steps:

Clone this repository:
bash
Copy code
git clone https://github.com/your-username/developer-salary-prediction.git
Navigate to the project directory:
bash
Copy code
cd developer-salary-prediction
Launch Jupyter Notebook:
Copy code
jupyter notebook
Open the Developer_Salary_Prediction.ipynb notebook in your browser.

Follow the instructions in the notebook to execute the code cells and perform the analysis.

Data
The data comes from Stack Overflow's annual developer survey for 2022. Each row shows the responses given by a developer. It has 73268 rows and 79 columns. The data has missing values but no duplicate rows. The target variable ConvertedCompYearly shows the annual salary for each developer.

Modeling
The modeling process involves building a classification model to predict developer salary ranges based on the available features. We explore various machine learning algorithms, such as logistic regression, decision trees, and random forests, to find the best-performing model.

Evaluation
The evaluation of the models is based on several metrics, including F1 score, precision, recall, and accuracy score. The performance of the models is compared, and the model with the best performance, which is Random Forest, is selected as the final model.

Deployment
We use Streamlit to deploy the model as an online dashboard.

Contributing
Contributions to this project are welcome. If you have suggestions, bug fixes, or enhancements, please submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

