"""Controller: serves the user manual as a web page."""
from flask import Blueprint, render_template

from ..config import USER_MANUAL_PATH
from ..models.docs_model import DocsModel

docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/docs")
def index():
    model = DocsModel(USER_MANUAL_PATH)
    content_html = ""
    error = None

    try:
        content_html = model.render_html()
    except FileNotFoundError as exc:
        error = str(exc)

    return render_template("docs.html", content_html=content_html, error=error)
