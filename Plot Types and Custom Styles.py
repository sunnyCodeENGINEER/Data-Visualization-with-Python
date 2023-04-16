import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

spotify_filepath = "spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Line chart
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

# Change the style of the figure to the "dark" theme
sns.set_style("dark")

# Line chart
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

plt.show()