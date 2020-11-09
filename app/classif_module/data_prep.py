from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


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
