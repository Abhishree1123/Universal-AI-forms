from __future__ import annotations
from pathlib import Path
import pikepdf
import hashlib

def compute_pdf_sha256(pdf_path: str | Path) -> str:
    data = Path(pdf_path).read_bytes()
    return hashlib.sha256(data).hexdigest()

def attach_profile_to_pdf(pdf_in: str | Path, profile_json_path: str | Path, out_path: str | Path) -> str:
    """Attach a JSON profile to a PDF without altering its visible content."""
    pdf_in = Path(pdf_in)
    out_path = Path(out_path)
    profile_json_path = Path(profile_json_path)

    with pikepdf.open(str(pdf_in)) as pdf:
        pdf.attach_file(str(profile_json_path), name="formdl_profile.json")
        pdf.save(str(out_path))
    return str(out_path)
