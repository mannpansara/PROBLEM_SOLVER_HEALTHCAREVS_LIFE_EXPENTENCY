import numpy as np
import matplotlib.pyplot as plt

# Data: Countries, healthcare spending (USD per capita), and life expectancy (years)
countries = np.array(["USA", "Canada", "Germany", "UK", "India", "Japan"])
healthcare_spending = np.array([12000, 6000, 6500, 5000, 1500, 4500])
life_expectancy = np.array([79, 82, 81, 80, 70, 85])

# Create indices for the x-axis
indices = np.arange(len(countries))

# Bar width
bar_width = 0.4

# Create the bar graph
plt.figure(figsize=(12, 6))
plt.bar(indices - bar_width / 2, healthcare_spending, bar_width, label='Healthcare Spending (USD)', color='blue')
plt.bar(indices + bar_width / 2, life_expectancy, bar_width, label='Life Expectancy (Years)', color='green')

# Add labels, title, and legend
plt.xticks(indices, countries)
plt.xlabel("Countries", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.title("Healthcare Spending vs. Life Expectancy", fontsize=16)
plt.legend()

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
