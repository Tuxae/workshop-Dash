from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

from classif_module.data_prep import DataPrep
from classif_module.standardizer import Standardizer
from classif_module.svc_model import SVCModel
# from dash_app.exploration_app.exploration import plot_correlation_matrix
from dash_app.exploration_app.exploration import plot_correlation_matrix

standardizer = StandardScaler()

preparator = DataPrep(
    "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
    ";",
)

df = preparator.get_dataframe()

X_train, X_test, y_train, y_test = preparator.get_train_test()

X_train, X_test = Standardizer(standardizer).get_standardized_data(X_train, X_test)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

svc = SVCModel(1.3, 1.3, "rbf")
svc.fit(X_train, y_train)
predictions = svc.predict(X_test)

print(classification_report(y_test, predictions))

plt, ax = plot_correlation_matrix(df)
plt.show()
