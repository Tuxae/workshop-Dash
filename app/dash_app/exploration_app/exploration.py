from typing import List, Tuple

import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from app.dash_app.utils import Navbar

# ------------------------------------------------------------------------------
# Constants

all_graphs = ["Scatter_matrix"]

all_graphs_with_cols = ["Histogram", "Density"]


# ------------------------------------------------------------------------------
# Utils functions for data vizualisation before and after modeling


def plot_histogram(dataframe: List[str], col: str) -> go.Figure:
    dataframe = pd.read_json(dataframe)
    fig = px.histogram(dataframe[col], x=col, histnorm="percent")
    return fig


def plot_density(dataframe: List[str], col: str) -> go.Figure:
    dataframe = pd.read_json(dataframe)
    hist_data = [dataframe[col]]
    group_labels = [col]
    fig = ff.create_distplot(hist_data, group_labels)
    return fig


def plot_correlation_matrix(dataframe: pd.DataFrame) -> Tuple[Figure, Axes]:
    correlations = dataframe.corr()
    fig, ax = plt.subplots(figsize=(10, 10))
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlations, cmap=colormap, annot=True, fmt=".2f")
    ax.set_xticklabels(
        dataframe.columns.tolist(), rotation=45, horizontalalignment="right"
    )
    ax.set_yticklabels(dataframe.columns.tolist())
    return fig, ax


def plot_scatter_matrix(
    dataframe: pd.DataFrame, dim: List[str], target: str
) -> go.Figure:
    fig = px.scatter_matrix(dataframe, dimensions=dim, color=target)
    fig.update_layout(autosize=True, width=900, height=900)
    return fig


# ------------------------------------------------------------------------------
# Build app layout


def build_create_data() -> html.Div:
    menu = html.Div(
        id="data_loading",
        children=[
            html.Div(
                children=[
                    html.Button(
                        "Chargement des données et exploration",
                        id="submit-data",
                        style={"display": "flex"},
                    )
                ],
                style={
                    "display": "flex",
                    "justify-content": "center",
                    "margin-bottom": "1.5em",
                    "margin-top": "1.5em",
                },
            ),
            dcc.Loading(
                html.Div(
                    id="data_desc",
                    children=[],
                    style={"display": "none"},
                )
            ),
        ],
    )
    return menu


def build_exploration_menu() -> html.Div:
    menu1 = html.Div(
        id="menu_correlation1",
        children=[
            html.Div(
                children=[
                    html.H6(
                        "Sélectionner un type de graphique:",
                        style={"margin-top": "0px"},
                    ),
                    dcc.Dropdown(
                        id="select_type_graph1",
                        options=[
                            {"label": i, "value": i} for i in all_graphs_with_cols
                        ],
                        multi=False,
                        style={"width": "100%"},
                        placeholder="Sélectionner un type de graphique",
                    ),
                    html.H6("Sélectionner une variable:", style={"margin-top": "0px"}),
                    dcc.Dropdown(
                        id="select_col",
                        multi=False,
                        style={"width": "100%"},
                        placeholder="Sélectionner une variable",
                    ),
                    html.Button(
                        "Entrer",
                        id="submit-val-col",
                        style={"display": "flex", "justify-content": "flex-end"},
                    ),
                ],
                style={
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "first baseline",
                    "margin-left": "2pc",
                },
            ),
            dcc.Loading(
                html.Div(dcc.Graph(id="figure_exploration1", style={"display": "none"}))
            ),
        ],
        style={"display": "none"},
    )

    menu2 = html.Div(
        id="menu_correlation2",
        children=[
            html.Div(
                [
                    html.H6(
                        "Sélectionner un type de graphique: ",
                        style={"margin-top": "0px"},
                    ),
                    dcc.Dropdown(
                        id="select_type_graph2",
                        options=[{"label": i, "value": i} for i in all_graphs],
                        multi=False,
                        style={"width": "100%"},
                        placeholder="Selectionner un type de graphique",
                    ),
                    html.Button(
                        "Entrer",
                        id="submit-val-graph2",
                        style={"display": "flex", "justify-content": "flex-end"},
                    ),
                ],
                style={
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "first baseline",
                    "margin-left": "2pc",
                },
            ),
            dcc.Loading(
                html.Div(dcc.Graph(id="figure_exploration2", style={"display": "none"}))
            ),
        ],
        style={"display": "none"},
    )
    return html.Div([menu1, menu2])


# ------------------------------------------------------------------------------
# Instantiate the app layout
nav = Navbar()

menu1 = build_create_data()
menu2 = build_exploration_menu()


def Exploration():
    return html.Div([nav, menu1, menu2])
