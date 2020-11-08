import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Home", href="/home"),
            dbc.DropdownMenuItem("Exploration", href="/exploration"),
            dbc.DropdownMenuItem("Model", href="/model"),
        ],
        nav=True,
        in_navbar=True,
        label="Explore",
    )

    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src="/assets/Logo_transparent.png", height="70px"
                                )
                            ),
                            dbc.Col(dbc.NavbarBrand("TUXAE", className="ml-2")),
                        ],
                        align="center",
                        no_gutters=True,
                    ),
                    href="https://www.tuxae.fr/",
                ),
                dbc.NavbarToggler(id="navbar-toggler2"),
                dbc.Collapse(
                    dbc.Nav(
                        # right align dropdown menu with ml-auto className
                        [dropdown],
                        className="ml-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
        className="mb-4",
        sticky="top",
    )
    return navbar
