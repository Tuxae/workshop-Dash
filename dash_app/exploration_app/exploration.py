from typing import List, Tuple

import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from dash_app.utils.navbar import Navbar


# ------------------------------------------------------------------------------
# Utils functions for data vizualisation before and after modeling

# TODO: implement functions for viz


def plot_histogram(dataframe: pd.DataFrame, col: str) -> go.Figure:
    fig = px.histogram(dataframe[col], x=col, histnorm="percent")
    return fig


def plot_density(dataframe: pd.DataFrame, col: str) -> go.Figure:
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
        dataframe.columns.tolist(),
        rotation=45,
        horizontalalignment='right'
    )
    ax.set_yticklabels(dataframe.columns.tolist())
    return fig, ax


def plot_scatter_matrix(
    dataframe: pd.DataFrame, dim: List[str], target: str
) -> go.Figure:
    fig = px.scatter_matrix(dataframe, dimensions=dim, color=target)
    return fig


# ------------------------------------------------------------------------------
# Build app layout
# TODO: implement viz layout, dropdown button, etc


# ------------------------------------------------------------------------------
# Instantiate the app layout


def Exploration():
    pass
