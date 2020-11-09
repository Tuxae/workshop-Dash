from sklearn.svm import SVC


class SVCModel(SVC):
    def __init__(self, C: float, gamma: float, kernel: str) -> None:
        super().__init__(C=C, kernel=kernel, gamma=gamma)
