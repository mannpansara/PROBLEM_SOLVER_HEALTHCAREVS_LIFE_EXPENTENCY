import numpy as np
import matplotlib.pyplot as plt

# Data: Countries, healthcare spending (USD per capita), and life expectancy (years)
countries = np.array(["USA", "Canada", "Germany", "UK", "India", "Japan"])
healthcare_spending = np.array([12000, 6000, 6500, 5000, 1500, 4500])
life_expectancy = np.array([79, 82, 81, 80, 70, 85])

# Create a pie chart for Healthcare Spending
plt.figure(figsize=(12, 6))

# Subplot for Healthcare Spending
plt.subplot(1, 2, 1)
plt.pie(healthcare_spending, labels=countries, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)
plt.title("Healthcare Spending (Share)")

# Subplot for Life Expectancy
plt.subplot(1, 2, 2)
plt.pie(life_expectancy, labels=countries, autopct='%1.1f%%', startangle=90, colors=plt.cm.Set2.colors)
plt.title("Life Expectancy (Share)")

# Adjust layout and display
plt.tight_layout()
plt.show()
