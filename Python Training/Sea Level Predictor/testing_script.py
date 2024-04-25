import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


df = pd.read_csv('epa-sea-level.csv')
print(df.head(5))
print(df.info())
print(df.describe())



# Create scatter plot
x1 = df['Year']
y1 = df['CSIRO Adjusted Sea Level']
plt.scatter(x1,y1)



# Create first line of best fit
result1 = linregress(x=x1,y=y1)
x1_fit = np.arange(x1.min(),2051,1)
y1_fit = result1.intercept+result1.slope*x1_fit
plt.plot(x1_fit, y1_fit,'r')

# Create second line of best fit
x2 = df[df['Year']>=2000]['Year']
y2 = df[df['Year']>=2000]['CSIRO Adjusted Sea Level']
result2 = linregress(x2,y2)
x2_fit = np.arange(2000,2051,1)
y2_fit = result2.intercept+result2.slope*x2_fit
plt.plot(x2_fit,y2_fit,color='green')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
plt.show()