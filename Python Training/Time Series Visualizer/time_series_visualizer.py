import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', header=0, index_col=0)
df = df.reset_index()
df['date'] = pd.to_datetime(df['date'])


# Clean data
filter_mask = (
        (df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))
    )

df = df[filter_mask]


def draw_line_plot():
    # Draw line plot
    fig = df.plot.line(x='date',y='value',color='red',figsize=(20,7))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=0)
    fig = fig.figure



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.set_index(['date'],inplace=True)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()


    df_agg = pd.pivot_table(
        df_bar, 
        values="value",
        index="year",
        columns="month", 
        aggfunc='mean'
    )

    df_agg = df_agg[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]

    # Draw bar plot
    fig = df_agg.plot(kind='bar',figsize = (10,10))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    fig = fig.figure





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

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





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
