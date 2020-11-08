from typing import Tuple, Union

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    StandardScaler,
    RobustScaler,
    MinMaxScaler,
    MaxAbsScaler,
    Normalizer,
    LabelEncoder,
)

Scaler = Union[StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler, Normalizer]


class DataPrep:
    def __init__(self, source: str, sep: str) -> None:
        self.source = source
        self.sep = sep

    def get_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(self.source, sep=self.sep)

    def convert_target(self) -> pd.DataFrame:
        bins = (2, 6, 8)
        group_names = ["bad", "good"]
        dataframe = self.get_dataframe()
        dataframe["quality"] = pd.cut(
            dataframe["quality"], bins=bins, labels=group_names
        )
        label_quality = LabelEncoder()
        dataframe["quality"] = label_quality.fit_transform(dataframe["quality"])
        return dataframe

    def get_train_test(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        dataframe = self.convert_target()
        return train_test_split(
            dataframe.drop("quality", axis=1),
            dataframe["quality"],
            test_size=0.3,
            random_state=0,
        )

    def get_standardized_data(
        self, standardizer: Scaler
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        X_train, X_test, y_train, y_test = self.get_train_test()
        X_train = standardizer.fit_transform(X_train)
        X_test = standardizer.fit_transform(X_test)
        return X_train, X_test, y_train, y_test