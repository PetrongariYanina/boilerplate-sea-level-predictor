import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit
    slope, intercept, _, _, _  = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(1880, 2051)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, color='red', label='Line of Best Fit (1880 - 2050)')


    # Create second line of best fit
    recent_years_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years_data['Year'], recent_years_data['CSIRO Adjusted Sea Level'])
    x_values_recent = range(2000, 2051) 
    y_values_recent = slope_recent * x_values_recent + intercept_recent
    plt.plot(x_values_recent, y_values_recent, color='green', label='Line of Best Fit (2000 - Recent)')

    sea_level_2050_recent = slope_recent * 2050 + intercept_recent
    plt.scatter(2050, sea_level_2050_recent, color='green', label='Prediction for 2050 (2000 - Recent)')

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()