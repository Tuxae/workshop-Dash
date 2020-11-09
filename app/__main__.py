from app.dash_app import app_instance
from app.dash_app import config as cfg


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

    app_instance.run_server(
        host=args.host, port=args.port, debug=cfg.DEBUG, dev_tools_hot_reload=cfg.DEBUG
    )
