"""Model: loads the user manual and converts it from Markdown to HTML."""
from pathlib import Path

import markdown


class DocsModel:
    """Reads a Markdown file from disk and renders it as HTML."""

    def __init__(self, docs_path: Path | str) -> None:
        self.docs_path = Path(docs_path)

    def exists(self) -> bool:
        return self.docs_path.is_file()

    def render_html(self) -> str:
        if not self.exists():
            raise FileNotFoundError(f"No se encontró el manual: {self.docs_path}")

        raw_markdown = self.docs_path.read_text(encoding="utf-8")
        return markdown.markdown(raw_markdown, extensions=["fenced_code", "tables"])
