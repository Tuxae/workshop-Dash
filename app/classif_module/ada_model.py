from sklearn.ensemble import AdaBoostClassifier


class AdaModel(AdaBoostClassifier):
    def __init__(self, n_estimators: int) -> None:
        super().__init__(n_estimators=n_estimators)
