import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv', header=0, index_col=0)
df = df.reset_index()
df['date'] = pd.to_datetime(df['date'])

filter_mask = (
		(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))
	)

df = df[filter_mask]

fig = df.plot.line(x='date',y='value',color='red',figsize=(20,7))
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.xticks(rotation=0)
fig = fig.figure

df_bar = df.copy()
print(df_bar.info())
df_bar.set_index(['date'],inplace=True)
df_bar['year'] = df_bar.index.year
df_bar['month'] = df_bar.index.month_name()
print(df_bar.head())


df_agg = pd.pivot_table(
    df_bar, 
    values="value",
    index="year",
    columns="month", 
    aggfunc='mean'
)

df_agg = df_agg[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]

fig = df_agg.plot(kind='bar',figsize = (9,9))
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.legend(title='Months')


df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
 
month_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(30,7))
ax1 = sns.boxplot(df_box,x='year',y='value',ax=ax1, hue='year', palette='pastel', legend=False, fliersize='1')
ax1.set_xlabel('Year')
ax1.set_ylabel('Page Views')
ax1.set_title('Year-wise Box Plot (Trend)')
ax2 = sns.boxplot(df_box,x='month',y='value',ax=ax2, order=month_label, hue='month', palette='pastel', fliersize='1')
ax2.set_xlabel('Month')
ax2.set_ylabel('Page Views')
ax2.set_title('Month-wise Box Plot (Seasonality)')
fig = fig.figure
