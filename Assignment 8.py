import pandas as pd
import seaborn as sns
import numpy as np


# Load the data
data = pd.read_csv('Exercise_Data.csv')

# Set the style for better look
sns.set_theme(style='whitegrid')

# Create a heatmap of pulse data
pulse_columns = ['1 min', '15 min', '30 min']
pulse_data = data[pulse_columns]

# Create heatmap directly with seaborn
sns.heatmap(pulse_data, annot=True, fmt='d', cmap='YlGnBu',cbar=True, linewidths=0.5)

# Set titles and labels
sns.set_context("notebook")
sns.despine()
import matplotlib.pyplot as plt  # Needed for title and labels, but minimal

plt.title('Heatmap of Pulse Rates at Different Times')
plt.xlabel('Time Interval')
plt.ylabel('Person ID')
plt.xticks(ticks=np.arange(len(pulse_columns)) + 0.5, labels=pulse_columns)
plt.yticks(ticks=np.arange(len(data)) + 0.5, labels=data.index + 1)
plt.show()

# Pulse values by diet and exercise type
melted = pd.melt(data, id_vars=['id', 'diet', 'kind'], value_vars=pulse_columns,var_name='Time', value_name='Pulse')

# Create catplot
sns.catplot(x='diet', y='Pulse', hue='kind', data=melted, kind='box', height=6, aspect=2)

# Titles and Labels
plt.title('Pulse Rates by Diet and Exercise Type')
plt.xlabel('Diet Type')
plt.ylabel('Pulse Rate')
plt.legend(title='Exercise Type')
plt.tight_layout()
plt.show()

# Load the planets' dataset
planets = sns.load_dataset('planets')
print(planets)

# Set grid style
sns.set_theme(style='whitegrid')

# Mass vs. orbital period for planets
plt.figure(figsize=(8, 6))
sns.scatterplot(data=planets, x='orbital_period', y='mass', hue='method', alpha=0.7)
plt.title('Mass vs. Orbital Period of Planets')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Earth masses)')
plt.legend(title='Detection Method')
plt.tight_layout()
plt.show()

# Number of planets discovered over the years
plt.figure(figsize=(8, 6))
sns.scatterplot(data=planets, x='year', y='orbital_period', hue='method', alpha=0.7)
plt.title('Discovery Year vs. Orbital Period of Planets')
plt.xlabel('Year of Discovery')
plt.ylabel('Orbital Period (days)')
plt.legend(title='Detection Method')
plt.tight_layout()
plt.show()

# Distribution of planet masses
plt.figure(figsize=(8, 6))
sns.histplot(data=planets, x='mass', bins=30, kde=True, color='skyblue')
plt.title('Distribution of Planet Masses')
plt.xlabel('Mass (Earth masses)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Average orbital period per detection method
mean_orbital_period = planets.groupby('method')['orbital_period'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.lineplot(data=mean_orbital_period, x='method', y='orbital_period', marker='o')
plt.title('Average Orbital Period by Detection Method')
plt.xlabel('Detection Method')
plt.ylabel('Average Orbital Period (days)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






