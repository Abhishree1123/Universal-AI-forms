from __future__ import annotations
import qrcode
from pathlib import Path

def make_qr_png(data: str, out_path: str | Path, box_size: int = 10, border: int = 2) -> str:
    """Create a QR code PNG from a string (pointer-mode)."""
    img = qrcode.make(data, box_size=box_size, border=border)
    out_path = str(out_path)
    img.save(out_path)
    return out_path
