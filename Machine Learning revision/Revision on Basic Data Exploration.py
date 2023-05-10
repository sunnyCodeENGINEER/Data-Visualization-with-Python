import pandas as pd
from sklearn.tree import DecisionTreeRegressor

test_file_path = "melb_data.csv"
test_data = pd.read_csv(test_file_path)
print(test_data.describe())

print(test_data.columns)

test_data = test_data.dropna(axis=0)

y = test_data.Price

test_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']

X = test_data[test_features]
print(X.describe())
print(X.head())

test_model = DecisionTreeRegressor(random_state=1)

test_model.fit(X, y)


print("Making the predictions form the first 5 houses: ")
print(X.head())
print("The predictions are")
print(test_model.predict(X.head()))





