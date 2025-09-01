import os
# Set working directory to Trend_analysis
os.chdir(r'c:/Users/nsuwal1/OneDrive - Louisiana State University/PhD papers/Chapter_2/Revision_2/Data_for analysis/Spatiotemporal Trend/Spatiotemporal-trends-/Trend_analysis')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kendalltau

# Load the data
data = pd.read_excel(r'c:/Users/nsuwal1/OneDrive - Louisiana State University/PhD papers/Chapter_2/Revision_2/Data_for analysis/Spatiotemporal Trend/Spatiotemporal-trends-/Trend_analysis/Sea_10D_TMIN_A.xlsx')

# Extract relevant columns
years = data['Year']
winter_values = data['Winter']

# Apply the Mann-Kendall Trend Test
tau, p_value = kendalltau(years, winter_values)

# Calculate Sen's slope
def sens_slope(x, y):
    n = len(y)
    slopes = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            slopes.append((y[j] - y[i]) / (x[j] - x[i]))
    return np.median(slopes)

sen_slope = sens_slope(years, winter_values)

# Line plot with trend line and displaying Kendall Tau, P-value, and Sen's slope
plt.figure(figsize=(14, 8))
plt.plot(years, winter_values, marker='o', linestyle='-', label='Minimum Temperature(TMIN)')
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Minimum Temperature (\u00B0C)', fontsize=14, fontweight='bold')

# Set the font size of the tick labels
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add trend line
z = np.polyfit(years, winter_values, 1)
p = np.poly1d(z)

# Determine if the trend is increasing or decreasing
trend_label = 'Trend Line (Increasing)' if z[0] > 0 else 'Trend Line (Decreasing)'

# Plot the trend line with the updated label
plt.plot(years, p(years), "r--", label=trend_label)

# Add legend with increased font size
plt.legend(loc='lower left', fontsize=12)

# Add legend and Kendall Tau/P-value/Sen's slope text
plt.text(0.3, 0.1, f'Kendall Tau: {tau:.3f}\nP-value: {p_value:.2e}\nSen\'s Slope: {sen_slope:.3f}', 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

plt.savefig('TMIN_LA_1.tiff', dpi=300)
plt.show()
