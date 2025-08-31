from __future__ import annotations
import zlib
import cbor2
from typing import Any, Dict

def encode_cborz(obj: Dict[str, Any]) -> bytes:
    """Encode dict to CBOR then zlib-compress (for offline QR/DataMatrix payloads)."""
    cbor = cbor2.dumps(obj)
    return zlib.compress(cbor, level=9)

def decode_cborz(blob: bytes) -> Dict[str, Any]:
    """Decompress zlib, then decode CBOR back to dict."""
    cbor = zlib.decompress(blob)
    return cbor2.loads(cbor)
