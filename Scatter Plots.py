import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = pd.read_csv("insurance.csv")
print(data.head())
print(data.columns)

sn.scatterplot(x=data.bmi, y=data.charges)

plt.show()

sn.regplot(x=data.bmi, y=data.charges)

plt.show()

sn.scatterplot(x=data.bmi, y=data.charges, hue=data.smoker)

plt.show()

sn.lmplot(x="bmi", y="charges", hue="smoker", data=data)

plt.show()

sn.swarmplot(x=data['smoker'],
              y=data['charges'])

plt.show()



