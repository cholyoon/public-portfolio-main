import pandas as pd




df = pd.read_csv('adult.data.csv')


df.info()
df.describe()

print(df.head(10))
print('race size is '+ str(df.value_counts(['race']).reset_index(name='counts')['counts']))



sex_mask = (df['sex'] == 'Male')

average_age_men = df[sex_mask]['age'].mean(axis=0)
print(f'average age of a man is {average_age_men}')


percent_bachelor = df[df['education']=='Bachelors']['education'].size / df['education'].size * 100
print(percent_bachelor) 

df_groupby_ed = df.groupby(['education','salary']).size().reset_index(name='counts')
print(df_groupby_ed)

education_salary_mask = ((df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K'))
percent_adv_50Kmore = df[education_salary_mask]['education'].size/df['education'].size*100
print(percent_adv_50Kmore)

education_salary_mask_lower = (~(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '<=50K'))
percent_adv_50Kless = df[education_salary_mask_lower]['education'].size/df['education'].size*100
print(percent_adv_50Kless)

education_salary_mask = ((df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary'] == '>50K'))
percent_adv_50Kmore = df[education_salary_mask]['education'].size/df[df['education'].isin(['Bachelors','Masters','Doctorate'])]['education'].size*100
# What percentage of people without advanced education make more than 50K?
df_lower_ed = df[~(df['education'].isin(['Bachelors','Masters','Doctorate']))]
print(df_lower_ed.size)

df_groupby_country_salary = df.groupby(['native-country','salary']).size().reset_index(name='counts_country_salary')
df_groupby_country = df.groupby(['native-country']).size().reset_index(name='counts_country')
df_merged = pd.merge(df_groupby_country_salary,df_groupby_country,how='inner',on=['native-country'])
df_merged['percent_dist'] = round(df_merged['counts_country_salary']/df_merged['counts_country']*100,1)
df_high_sorted = df_merged[df_merged['salary']=='>50K'].sort_values(by='percent_dist',ascending=0)
print(df_high_sorted.head(5))

df_groupby_india_occ = df[df['native-country']=='India'].groupby(['occupation']).size().reset_index(name='counts_occupation').sort_values(by='counts_occupation',ascending=0)
print(df_groupby_india_occ.head(5))

