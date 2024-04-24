import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

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





# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['variable','cardio','value']).size().reset_index(name='total')
    

    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(x='variable',
        y='total',
        data=df_cat,
        hue='value',
        kind='bar',
        col='cardio'
    ).fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    heat_mask = (
        (
            (df['ap_lo'] <= df['ap_hi'])
        ) &
        (
            (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
        ) & 
        (
            (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
        )
    )
    df_heat = df[heat_mask]
    # Calculate the correlation matrix
    corr_matrix = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix))



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data = corr_matrix, 
        mask=mask,
        annot = True,
        annot_kws = {'size':8},
        fmt = '.1f',
        vmin = -0.7,
        vmax = 0.7,
        center = 0
    )


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
