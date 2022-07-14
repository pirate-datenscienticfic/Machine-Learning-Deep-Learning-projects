
# HR Analytics

### About Practice Problem: HR Analytics

HR analytics is revolutionising the way human resources departments operate, 
leading to higher efficiency and better results overall. Human resources has 
been using analytics for years. However, the collection, processing and 
analysis of data has been largely manual, and given the nature of human 
resources dynamics and HR KPIs, the approach has been constraining HR. 
Therefore, it is surprising that HR departments woke up to the utility of 
machine learning so late in the game. Here is an opportunity to try 
predictive analytics in identifying the employees most likely to get 
promoted.


### Overview

Your client is a large MNC and they have 9 broad verticals across the 
organisation. One of the problem your client is facing is around identifying 
the right people for promotion (only for manager position and below) and 
prepare them in time. Currently the process, they are following is:

They first identify a set of employees based on recommendations/ past 
performance Selected employees go through the separate training and 
evaluation program for each vertical. These programs are based on the 
required skill of each vertical At the end of the program, based on various 
factors such as training performance, KPI completion (only employees with 
KPIs completed greater than 60% are considered) etc., employee gets 
promotion For above mentioned process, the final promotions are only 
announced after the evaluation and this leads to delay in transition to 
their new roles. Hence, company needs your help in identifying the eligible 
candidates at a particular checkpoint so that they can expedite the entire 
promotion cycle.


### Breif about datasets

Dataset Description
Variable	Definition
employee_id	Unique ID for employee
department	Department of employee
region	Region of employment (unordered)
education	Education Level
gender	Gender of Employee
recruitment_channel	Channel of recruitment for employee
no_of_trainings	no of other trainings completed in previous year on soft skills, technical skills etc.
age	Age of Employee
previous_year_rating	Employee Rating for the previous year
length_of_service	Length of service in years
KPIs_met >80%	if Percent of KPIs(Key performance Indicators) >80% then 1 else 0
awards_won?	if awards won during previous year then 1 else 0
avg_training_score	Average score in current training evaluations
is_promoted	(Target) Recommended for promotion
