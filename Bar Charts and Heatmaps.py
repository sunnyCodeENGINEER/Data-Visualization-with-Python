import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("flight_delays.csv")
print(data.head())

# BAR CHART
plt.figure(figsize=(10, 6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

sns.barplot(x=data.index, y=data.NK)

plt.ylabel("Arrival delay (in minutes)")

plt.show()

# HEATMAP
plt.figure(figsize=(14, 7))

plt.title("Average Arrival Delay for Each Airline, by Month")

sns.heatmap(data=data, annot=True)

plt.xlabel("Airline")

plt.show()








