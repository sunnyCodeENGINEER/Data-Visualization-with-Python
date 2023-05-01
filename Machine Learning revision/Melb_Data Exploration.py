import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

data = pd.read_csv("melb_data.csv")
print(data.describe())
print(data.head())
print(data.tail())


