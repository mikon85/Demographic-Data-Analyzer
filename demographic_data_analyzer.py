import pandas as pd

# Load the dataset
df = pd.read_csv('adult.data.csv')

# How many people of each race are represented in this dataset? 
race_counts = df['race'].value_counts()

# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = higher_education[higher_education['salary'] == '>50K']
percentage_higher_education_rich = (len(higher_education_rich) / len(higher_education)) * 100

# What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education_rich = lower_education[lower_education['salary'] == '>50K']
percentage_lower_education_rich = (len(lower_education_rich) / len(lower_education)) * 100

# What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100

# What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100

# Identify the most popular occupation for those who earn >50K in India
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

# Print results
print("How many people of each race are represented in this dataset? \n", race_counts)
print("\nWhat is the average age of men? \n", average_age_men)
print("\nWhat is the percentage of people who have a Bachelor's degree? \n", percentage_bachelors)
print("\nWhat percentage of people with advanced education make more than 50K? \n", percentage_higher_education_rich)
print("\nWhat percentage of people without advanced education make more than 50K? \n", percentage_lower_education_rich)
print("\nWhat is the minimum number of hours a person works per week? \n", min_work_hours)
print("\nWhat percentage of the people who work the minimum number of hours per week have a salary of more than 50K? \n", rich_percentage)
print("\nWhat country has the highest percentage of people that earn >50K and what is that percentage? \n", highest_earning_country, highest_earning_country_percentage)
print("\nIdentify the most popular occupation for those who earn >50K in India \n", top_IN_occupation)
