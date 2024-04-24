import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are reprddddesented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts(['race']).reset_index(name='counts')['counts']

    # What is the average age of men?
    sex_mask = (df['sex'] == 'Male')
    average_age_men = round(df[sex_mask]['age'].mean(axis=0),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df['education']=='Bachelors']['education'].size / df['education'].size * 100,1)
    education_higher = (df['education'].isin(['Bachelors','Masters','Doctorate']))
    percent_higher = df[education_higher]['education'].size/df['education'].size*100
    
    education_lower = (~df['education'].isin(['Bachelors','Masters','Doctorate']))
    percent_lower = df[education_lower]['education'].size/df['education'].size*100


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    education_salary_mask = ((df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K'))
    percent_adv_50Kmore = df[education_salary_mask]['education'].size/df[df['education'].isin(['Bachelors','Masters','Doctorate'])]['education'].size*100
    # What percentage of people without advanced education make more than 50K?
    education_salary_mask_lower = (~(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K'))
    percent_non_50Kmore = df[education_salary_mask_lower]['education'].size/df[~(df['education'].isin(['Bachelors','Masters','Doctorate']))]['education'].size*100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = percent_higher
    lower_education = percent_lower

    # percentage with salary >50K
    higher_education_rich = round(percent_adv_50Kmore,1)
    lower_education_rich = round(percent_non_50Kmore,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask_min_50Kmore = ((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K'))
    percent_min_workers = df[mask_min_50Kmore]['hours-per-week'].size / df[(df['hours-per-week'] == min_work_hours)]['hours-per-week'].size*100

    rich_percentage = percent_min_workers


    df_groupby_country_salary = df.groupby(['native-country','salary']).size().reset_index(name='counts_country_salary')
    df_groupby_country = df.groupby(['native-country']).size().reset_index(name='counts_country')
    df_merged = pd.merge(df_groupby_country_salary,df_groupby_country,how='inner',on=['native-country'])
    df_merged['percent_dist'] = round(df_merged['counts_country_salary']/df_merged['counts_country']*100,1)
    df_high_sorted = df_merged[df_merged['salary']=='>50K'].sort_values(by='percent_dist',ascending=0)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df_high_sorted.iloc[0,0]
    highest_earning_country_percentage = df_high_sorted.iloc[0,4]

    # Identify the most popular occupation for those who earn >50K in India.
    df_groupby_india_occ = df[df['native-country']=='India'].groupby(['occupation']).size().reset_index(name='counts_occupation').sort_values(by='counts_occupation',ascending=0)
    top_IN_occupation = df_groupby_india_occ.iloc[0,0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

