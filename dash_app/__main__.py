import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_app.utils.config as cfg
from dash_app.homepage_app.homepage import Homepage

# ------------------------------------------------------------------------------
# Instantiate the app

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.config.suppress_callback_exceptions = True
app.title = "Internal Workshop Tuxae"
server = app.server
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
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
    if pathname == "exploration":
        pass
    elif pathname == "model":
        pass
    else:
        return Homepage()


# ------------------------------------------------------------------------------
# Running the web-app server


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Dash internal workshop Tuxae",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host of the server"
    )
    parser.add_argument(
        "--port", type=int, default=8050, help="Port to run the server on"
    )
    args = parser.parse_args()

    app.run_server(
        host=args.host, port=args.port, debug=cfg.DEBUG, dev_tools_hot_reload=cfg.DEBUG
    )
