import dash_bootstrap_components as dbc
import dash_html_components as html

from dash_app.utils.navbar import Navbar

nav = Navbar()

body = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src="../assets/Logo_Tuxae.png",
                            id="sncf-image",
                            style={
                                "height": "100px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "TUXAE WORKSHOP",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Identification et description des comportements de conduite",
                                    style={"margin-top": "0px"},
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flex-direction": "column",
                                "align-items": "center",
                                "justify-content": "center",
                            },
                        ),
                    ],
                    className="one-half column",
                    id="title",
                    style={"display": "flex"},
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px", 'display': 'flex'},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # TODO: description
                        html.H2("Description du projet"),
                        html.P(("Projet description ")),
                    ],
                    md=12,
                )
            ]
        ),
    ],
    className="mt-4",
)


def Homepage():
    home_page = html.Div([nav, body])

    return home_page
