"""Application configuration: paths shared across layers."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
MAX_UPLOAD_SIZE = 20 * 1024 * 1024  # 20 MB

DOCS_DIR = BASE_DIR / "docs"
USER_MANUAL_PATH = DOCS_DIR / "manual-usuario.md"
