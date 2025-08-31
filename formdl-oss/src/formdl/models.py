from __future__ import annotations
from typing import List, Optional, Literal, Dict, Any, Tuple
from pydantic import BaseModel, Field, HttpUrl

class Anchor(BaseModel):
    field_id: str
    page: int = Field(ge=1, description="1-indexed page number")
    bbox: Tuple[float, float, float, float] = Field(
        description="[x, y, width, height] in PDF points"
    )
    type: Literal["string", "number", "date", "enum", "currency", "boolean"] = "string"
    required: bool = False

class ValidationRule(BaseModel):
    field: str
    regex: Optional[str] = None
    min: Optional[float] = None
    max: Optional[float] = None
    enum: Optional[List[str]] = None
    depends_on: Optional[str] = None
    expression: Optional[str] = None  # e.g. "amount > 0 and currency == 'USD'"

class Destination(BaseModel):
    type: Literal["api", "queue", "file"] = "api"
    uri: str

class FormDLProfile(BaseModel):
    form_uid: str
    issuer: str
    version: str
    variant: Optional[Dict[str, str]] = None
    template: Optional[Dict[str, str]] = None  # e.g., {"pdf_sha256": "..."}
    anchors: List[Anchor] = []
    schema_uri: Optional[HttpUrl] = None
    schema_inline: Optional[Dict[str, Any]] = None
    validation: Optional[Dict[str, List[ValidationRule]]] = None
    prompt_pack_uri: Optional[HttpUrl] = None
    prompt_pack_inline: Optional[Dict[str, Any]] = None
    destinations: List[Destination] = []

    def fingerprint(self) -> str:
        import json, hashlib
        data = self.model_dump(exclude_none=True)
        blob = json.dumps(data, sort_keys=True).encode("utf-8")
        return hashlib.sha256(blob).hexdigest()
