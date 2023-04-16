import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")
print(data.head())

# HISTOGRAMS
sns.histplot(data['Petal Length (cm)'])
plt.show()

# KERNEL DENSITY ESTIMATE (KDE)
sns.kdeplot(data=data['Petal Length (cm)'], fill=True)
plt.show()

# 2D KDE
sns.jointplot(x=data['Petal Length (cm)'], y=data['Sepal Width (cm)'], kind="kde")
plt.show()

# HISTOGRAM FOR EACH SPECIES (WITH COLOR CODING)
sns.histplot(data=data, x='Petal Length (cm)', hue='Species')
plt.title("Histogram of Petal Lengths by Species")
plt.show()

# KDE FOR EACH SPECIES
sns.kdeplot(data=data, x='Petal Length (cm)', hue='Species', fill=True)
plt.title("Distribution of Petal Lengths, by Species")
plt.show()







