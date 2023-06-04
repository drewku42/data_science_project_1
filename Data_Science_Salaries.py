# This code was initially written in a Jupyter notebook but I adapted it to a single module.
# pandas for data manipulation, numpy for computation, 
# matplotlib/seaborn for visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("All libraries imported.")

df = pd.read_csv('ds_salaries.csv') # create data frame from csv
df.head() # observe first few values

# CREATE BAR GRAPH FOR JOB TITLES
job_counts = df['job_title'].value_counts() # Count the occurrences of each job title

top_10_and_misc = pd.concat([job_counts[:10], pd.Series([job_counts[10:].sum()], index=['Misc'])])
# Create a new series with the top 10 job titles and a 'Misc' category for all others

# Create a bar chart
plt.figure(figsize=(10,8))
top_10_and_misc.plot(kind='bar')

plt.xlabel('Job Titles') # Add labels
plt.ylabel('Count')
plt.title('Distribution of Job Titles') # Add title
plt.show() # Display the plot

# TOP 10 PAYING JOBS
# Count the occurrences of each job title
job_counts = df['job_title'].value_counts()

# Create a new series with the top 4 job titles and a 'Misc' category for all others
top_4_and_misc = pd.concat([job_counts[:4], pd.Series([job_counts[4:].sum()], index=['Misc'])])

# Create a pie chart
plt.figure(figsize=(10,8))
top_4_and_misc.plot(kind='pie', autopct='%1.1f%%')

# Add a title
plt.title('Distribution of Job Titles')

# Display the plot
plt.show()


# SALARY DISTRIBUTION FOR TOP 10 JOBS
# Get the top 10 most common job titles
top_10_jobs = df['job_title'].value_counts().index[:10]

# Create a new DataFrame containing only rows with the top 10 job titles
top_10_jobs_df = df[df['job_title'].isin(top_10_jobs)]

# Create a box plot of salaries for each job title
plt.figure(figsize=(10,8))
sns.boxplot(x='job_title', y='salary_in_usd', data=top_10_jobs_df)

# Rotate the x-axis labels for readability
plt.xticks(rotation=90)

# Add labels and title
plt.xlabel('Job Title')
plt.ylabel('Salary in USD')
plt.title('Salary Distribution by Job Title')

# Set y-ticks to whole numbers
max_salary = top_10_jobs_df['salary_in_usd'].max()
plt.yticks(np.arange(0, max_salary+1, step=25000))  # Set step size to 5000

# Display the plot
plt.show()

# Create a new DataFrame containing only rows with 'S', 'M', and 'L' company sizes
filtered_df = df[df['company_size'].isin(['S', 'M', 'L'])]

# Create a box plot of salaries for each company size
plt.figure(figsize=(10,8))
sns.boxplot(x='company_size', y='salary_in_usd', data=filtered_df)

# Add labels and title
plt.xlabel('Company Size')
plt.ylabel('Salary in USD')
plt.title('Salary Distribution by Company Size')

# Display the plot
plt.show()

unique_jobs = df['job_title'].unique() # get list of unique job titles
print(f"There are {len(unique_jobs)} unique jobs in the Data Science industry!")

# Create a new column 'job_type' categorizing jobs as 'remote' or 'in-person'
df['job_type'] = df['remote_ratio'].apply(lambda x: 'remote' if x > 0.5 else 'in-person')

job_type_counts = df['job_type'].value_counts() # Count the number of remote and in-person jobs

# Create a pie chart
plt.figure(figsize=(10,8))
job_type_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title('Distribution of Remote and In-person Jobs') # Add a title
plt.show() # Display the plot
