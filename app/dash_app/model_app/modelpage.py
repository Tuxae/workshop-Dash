from typing import List, Dict

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from app.classif_module import AdaModel
from app.classif_module import Standardizer
from app.classif_module.svc_model import SVCModel
from app.dash_app.utils import Navbar


# ------------------------------------------------------------------------------
# Utils functions for modeling purposes


def build_model(value_model: str, df_json: Dict[List[str], List[str]]) -> float:
    # read le json
    dataframe = pd.read_json(df_json)
    # split
    X_train, X_test, y_train, y_test = train_test_split(
        dataframe.drop("quality", axis=1),
        dataframe["quality"],
        test_size=0.3,
        random_state=0,
    )
    # normalisation
    standardizer = StandardScaler()
    X_train, X_test = Standardizer(standardizer).get_standardized_data(X_train, X_test)

    if value_model == "ada":
        # AdaBoost Classifier
        ada = AdaModel(100)
        ada.fit(X_train, y_train)
        predictions = ada.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy

    else:
        # SVC
        svc = SVCModel(1.3, 1.3, "rbf")
        svc.fit(X_train, y_train)
        predictions = svc.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy


# ------------------------------------------------------------------------------
# Build app layout


def build_menu() -> html.Div:
    menu = html.Div(
        id="menu_model_choice",
        children=[
            dcc.RadioItems(
                id="choice_model",
                options=[
                    {"label": "SVC", "value": "SVC"},
                    {"label": "AdaBoost", "value": "ada"},
                ],
                value="SVC",
                style={
                    "display": "flex",
                    "flex-direction": "column",
                },
            ),
            html.Div(id="hidden-df", style={"display": "none"}),
            html.Div(
                id="div_accuracy",
                children=[
                    html.P("This is the accuracy achieved by the chosen model: "),
                    html.P(id="display_accuracy"),
                ],
            ),
        ],
        style={
            "display": "flex",
            "flex-direction": "row",
            "justify-content": "space-around",
            "align-items": "center",
            "margin-top": "10pc",
        },
    )
    return menu


# ------------------------------------------------------------------------------
# Instantiate the app layout
nav = Navbar()
menu = build_menu()


def Modelpage():
    return html.Div([nav, menu])
