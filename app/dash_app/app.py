import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app.classif_module.data_prep import DataPrep
from app.dash_app import (
    plot_histogram,
    plot_density,
    Exploration,
    plot_scatter_matrix,
)
from app.dash_app.homepage_app.homepage import Homepage

# ------------------------------------------------------------------------------
# Instantiate the app
from app.dash_app.model_app.modelpage import Modelpage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.config.suppress_callback_exceptions = True
app.title = "Internal Workshop Tuxae"
server = app.server
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            children=[
                html.Div(id="page-content"),
                dcc.Store(id="dataframe", storage_type="memory"),
            ]
        ),
    ]
)


# ------------------------------------------------------------------------------
# Most important callback


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """
    This is the main callback of the app.
    It takes the url path as input and returns the corresponding page layout,
    thanks to the instantiation functions built in the various .py files.
    """
    if pathname == "/exploration":
        return Exploration()
    elif pathname == "/model":
        return Modelpage()
    else:
        return Homepage()


@app.callback(
    [
        Output("data_desc", "children"),
        Output("data_desc", "style"),
        Output("dataframe", "data"),
        Output("select_col", "options"),
        Output("menu_correlation1", "style"),
        Output("menu_correlation2", "style"),
    ],
    [Input("submit-data", "n_clicks")],
)
def load_data_and_display(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        pass

    df = DataPrep(
        "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
        ";",
    ).convert_target()

    data_head = df.head()
    columns = [{"name": i, "id": i} for i in data_head.columns]
    data = data_head.to_dict("records")

    return (
        dash_table.DataTable(id="spearman-table-1", columns=columns, data=data),
        {"display": "flex", "justify-content": "center"},
        df.to_json(),
        [{"label": i, "value": i} for i in df.drop("quality", axis=1).columns.tolist()],
        {
            "display": "flex",
            "flex-direction": "row",
            "justify-content": "space-around",
            "margin-top": "5pc",
            "margin-bottom": "5pc",
        },
        {
            "display": "flex",
            "flex-direction": "row",
            "justify-content": "space-around",
            "margin-top": "5pc",
            "margin-bottom": "5pc",
        },
    )


@app.callback(
    [Output("figure_exploration1", "figure"), Output("figure_exploration1", "style")],
    [Input("submit-val-col", "n_clicks")],
    [
        State("select_col", "value"),
        State("select_type_graph1", "value"),
        State("dataframe", "data"),
    ],
)
def update_figure_col(n_clicks, col, type_graph, dataframe):
    if n_clicks is None:
        raise PreventUpdate
    else:
        pass

    if type_graph == "Histogram":
        return plot_histogram(dataframe, col), {"display": "flex"}
    else:
        return plot_density(dataframe, col), {"display": "flex"}


@app.callback(
    [Output("figure_exploration2", "figure"), Output("figure_exploration2", "style")],
    [Input("submit-val-graph2", "n_clicks")],
    [State("select_type_graph2", "value"), State("dataframe", "data")],
)
def update_figure_col(n_clicks, type_graph, dataframe):
    if n_clicks is None:
        raise PreventUpdate
    else:
        pass

    dataframe = pd.read_json(dataframe)
    return (
        plot_scatter_matrix(
            dataframe, dim=dataframe.columns.tolist(), target="quality"
        ),
        {"display": "flex"},
    )


@app.callback(Output("hidden-df", "children"), [Input("dataframe", "data")])
def update_data(has_data):
    if has_data is None:
        df = DataPrep(
            "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
            ";",
        ).convert_target()
        return df.to_json()
    else:
        return has_data
