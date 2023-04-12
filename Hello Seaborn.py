import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("fifa.csv")
print(data.head())
print(data.columns)

list_cols = ['ARG', 'BRA']

print(list_cols)

# Set the width and height of the figure
plt.figure(figsize=(16, 6))

# Add title
plt.title("FIFA World Rankings for 6 countries")

sns.lineplot(data=data['ARG'], label="Argentina")
sns.lineplot(data=data['BRA'], label="Brazil")

plt.show()

