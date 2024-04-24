import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
print(df.describe())
print(df.info())

# Add 'overweight' column
df['bmi'] = df['weight']/(df['height']/100)**2
df.loc[df['bmi'] >25,'overweight'] = int(1)
df.loc[df['bmi'] <=25,'overweight'] = int(0)
df.drop(['bmi'],axis=1,inplace=True)



# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize_health(x):
    if x == 1:
        return int(0)
    else:
        return int(1)

df['cholesterol'] = df.apply(lambda x: normalize_health(x.cholesterol), axis=1)
df['gluc'] = df.apply(lambda x: normalize_health(x.gluc), axis=1)


df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'], var_name='variable')

print(df_cat.head(10))


df_cat = df_cat.groupby(['variable','cardio','value']).size().reset_index(name='total')

fig = sns.catplot(x='variable',
    y='total',
    data=df_cat,
    hue='value',
    kind='bar',
    col='cardio'
    )

fig.savefig('catplot_fig1.png')


heat_mask = (
    ((df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975))) |
    ((df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))))
df_heat = df[heat_mask]
corr_matrix = df_heat.corr()
mask = np.triu(np.ones_like(corr_matrix))
fig = plt.figure(figsize=(15,10))
sns.heatmap(data = corr_matrix, 
    mask=mask,
    annot = True,
    annot_kws = {'size':8},
    fmt = '.1f',
    vmin = -0.7,
    vmax = 0.7,
    center = 0)

plt.show()
