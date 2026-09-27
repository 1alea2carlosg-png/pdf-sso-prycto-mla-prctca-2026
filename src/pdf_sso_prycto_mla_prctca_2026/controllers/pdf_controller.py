"""Controller: wires HTTP routes to the PDF model and views."""
import io
from pathlib import Path

from flask import Blueprint, redirect, render_template, request, send_file, session, url_for
from werkzeug.utils import secure_filename

from ..config import UPLOAD_DIR
from ..models.pdf_model import PdfModel

pdf_bp = Blueprint("pdf", __name__)

STORED_PDF_NAME = "current.pdf"


@pdf_bp.route("/")
def index():
    original_name = session.get("original_name")
    upload_error = session.pop("upload_error", None)
    text = ""
    error = None

    if original_name:
        model = PdfModel(UPLOAD_DIR / STORED_PDF_NAME)
        try:
            text = model.extract_text()
        except FileNotFoundError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        filename=original_name,
        text=text,
        error=error,
        upload_error=upload_error,
    )


@pdf_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("pdf_file")

    if not file or file.filename == "" or not file.filename.lower().endswith(".pdf"):
        session.pop("original_name", None)
        session["upload_error"] = "Selecciona un archivo PDF válido."
        return redirect(url_for("pdf.index"))

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file.save(UPLOAD_DIR / STORED_PDF_NAME)
    session["original_name"] = secure_filename(file.filename)
    session.pop("upload_error", None)

    return redirect(url_for("pdf.index"))


@pdf_bp.route("/export")
def export():
    original_name = session.get("original_name")
    if not original_name:
        return redirect(url_for("pdf.index"))

    model = PdfModel(UPLOAD_DIR / STORED_PDF_NAME)
    text = model.extract_text()

    buffer = io.BytesIO(text.encode("utf-8"))
    download_name = Path(original_name).stem + ".txt"

    return send_file(
        buffer,
        mimetype="text/plain",
        as_attachment=True,
        download_name=download_name,
    )
