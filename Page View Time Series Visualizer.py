import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

# Draw line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    return fig

# Draw bar plot
def draw_bar_plot():
    df_bar = df.groupby([df.index.year, df.index.month]).mean().unstack()
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Page Views per Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    return fig

# Draw box plots
def draw_box_plot():
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    
    df_box_year = df.copy()
    df_box_year.reset_index(inplace=True)
    df_box_year['year'] = [d.year for d in df_box_year['date']]
    df_box_year['month'] = [d.strftime('%b') for d in df_box_year['date']]
    df_box_year = df_box_year.sort_values(by=['year', 'date'])

    sns.boxplot(x='year', y='value', data=df_box_year, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box_year, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.savefig('box_plot.png')
    return fig

# Draw line plot
draw_line_plot()

# Draw bar plot
draw_bar_plot()

# Draw box plots
draw_box_plot()
