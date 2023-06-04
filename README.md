# Data Science Salaries Analysis
This project is an exploratory data analysis of the 'Data Science Salaries 2023' dataset from Kaggle. The goal of the project is to gain insights into the data science job market, including the distribution of job titles, the relationship between company size and salary, and the comparison of remote and in-person jobs.

Dataset
The dataset includes the following columns:

work_year: The year the salary was paid.
experience_level: The experience level in the job during the year.
employment_type: The type of employment for the role.
job_title: The role worked in during the year.
salary: The total gross salary amount paid.
salary_currency: The currency of the salary paid as an ISO 4217 currency code.
salaryinusd: The salary in USD.
employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
remote_ratio: The overall amount of work done remotely.
company_location: The country of the employer's main office or contracting branch.
company_size: The median number of people that worked for the company during the year.
Methodology
The analysis was conducted in a Jupyter Notebook using Python. The pandas library was used for data manipulation, and matplotlib and seaborn were used for data visualization.

The analysis included the following steps:

Data Importing: The dataset was imported into a pandas DataFrame.

Data Exploration: The data was explored to understand the distribution of values in each column. This included calculating basic statistics and creating visualizations such as bar charts and box plots.

Data Analysis: The data was analyzed to answer specific questions, such as which job titles are most common, how company size affects salary, and how the number of remote and in-person jobs compare. This involved creating more complex visualizations and calculating correlations between different variables.

Findings
The analysis revealed several interesting insights:

The most common job titles in the data science field were Data Engineer, Data Scientist, and Data Analyst.
There was a positive correlation between company size and salary, with larger companies generally paying higher salaries.
The distribution of salaries varied significantly between different job titles.
The majority of jobs were in-person, but a significant proportion were remote.
Conclusion
This project provided valuable insights into the data science job market. However, it's important to note that the findings are based on the specific dataset used and may not be representative of the entire field. Future work could include analyzing more recent data, incorporating additional variables, or using more advanced statistical techniques to gain deeper insights.
