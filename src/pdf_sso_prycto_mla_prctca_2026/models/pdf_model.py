"""Model: encapsulates PDF text extraction logic."""
from pathlib import Path

from pypdf import PdfReader


class PdfModel:
    """Reads a PDF file from disk and exposes its plain-text content."""

    def __init__(self, pdf_path: Path | str) -> None:
        self.pdf_path = Path(pdf_path)

    @property
    def filename(self) -> str:
        return self.pdf_path.name

    def exists(self) -> bool:
        return self.pdf_path.is_file()

    def extract_text(self) -> str:
        if not self.exists():
            raise FileNotFoundError(f"No se encontró el PDF: {self.pdf_path}")

        reader = PdfReader(self.pdf_path)
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages).strip()
