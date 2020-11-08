from sklearn.preprocessing import StandardScaler

from dash_app.classif_module.data_prep import DataPrep

standardizer = StandardScaler()

X_train, X_test, y_train, y_test = DataPrep(
    "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
    ";",
).get_standardized_data(standardizer)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

df = DataPrep(
    "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
    ";",
).convert_target()

print(df)
