from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

from app.classif_module import AdaModel
from app.classif_module.data_prep import DataPrep
from app.classif_module import Standardizer
from app.classif_module.svc_model import SVCModel
from app.dash_app import plot_correlation_matrix

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

# SVC
svc = SVCModel(1.3, 1.3, "rbf")
svc.fit(X_train, y_train)
predictions = svc.predict(X_test)

print(classification_report(y_test, predictions))

plt, ax = plot_correlation_matrix(df)
plt.show()

# AdaBoost Classifier
ada = AdaModel(100)
ada.fit(X_train, y_train)
predictions = ada.predict(X_test)

# Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)

# Log Reg
log = LogisticRegression()
log.fit(X_train, y_train)
predictions = log.predict(X_test)
