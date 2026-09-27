"""App factory wiring Model-View-Controller pieces together."""
from pathlib import Path

from flask import Flask

from .config import MAX_UPLOAD_SIZE
from .controllers.docs_controller import docs_bp
from .controllers.pdf_controller import pdf_bp

_VIEWS_DIR = Path(__file__).resolve().parent / "views"


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(_VIEWS_DIR / "templates"),
        static_folder=str(_VIEWS_DIR / "static"),
    )
    app.secret_key = "dev-local-secret-key"
    app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_SIZE
    app.register_blueprint(pdf_bp)
    app.register_blueprint(docs_bp)
    return app


def main() -> None:
    app = create_app()
    app.run(debug=True)
