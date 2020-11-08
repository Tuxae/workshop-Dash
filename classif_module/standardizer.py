from typing import Tuple, Union
import numpy as np
import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    RobustScaler,
    MinMaxScaler,
    MaxAbsScaler,
    Normalizer,
)


Scaler = Union[StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler, Normalizer]


class Standardizer:
    def __init__(self, standardizer: Scaler):
        self.scaler = standardizer

    def get_standardized_data(
        self, X_train: pd.DataFrame, X_test: pd.DataFrame
    ) -> Tuple[np.array, np.array]:
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.fit_transform(X_test)
        return X_train, X_test
