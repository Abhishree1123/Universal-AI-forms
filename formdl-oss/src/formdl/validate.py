from __future__ import annotations
from typing import Dict, Any, List
import re
from jsonschema import validate as js_validate, Draft202012Validator

from .models import FormDLProfile, ValidationRule

def validate_profile(profile: FormDLProfile) -> List[str]:
    """Light validation of FormDL profile shape (not a formal spec validator)."""
    errors: List[str] = []
    if not profile.form_uid:
        errors.append("form_uid is required")
    if not profile.version:
        errors.append("version is required")
    if profile.schema_inline is None and profile.schema_uri is None:
        errors.append("Either schema_inline or schema_uri must be provided")
    return errors

def validate_output_against_schema(output: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    v = Draft202012Validator(schema)
    for e in v.iter_errors(output):
        errors.append(e.message)
    return errors

def apply_validation_rules(output: Dict[str, Any], rules: List[ValidationRule]) -> List[str]:
    errors: List[str] = []
    for r in rules:
        val = _get(output, r.field)
        if r.regex and isinstance(val, str) and not re.match(r.regex, val or ""):
            errors.append(f"{r.field} failed regex")
        if isinstance(val, (int, float)):
            if r.min is not None and val < r.min:
                errors.append(f"{r.field} < min {r.min}")
            if r.max is not None and val > r.max:
                errors.append(f"{r.field} > max {r.max}")
        if r.enum and val not in r.enum:
            errors.append(f"{r.field} not in enum {r.enum}")
        if r.expression:
            # Very simple / unsafe eval stub; replace in production
            env = {"value": val, **output}
            try:
                if not eval(r.expression, {"__builtins__": {}}, env):  # noqa: S307
                    errors.append(f"{r.field} failed expression: {r.expression}")
            except Exception:
                errors.append(f"rule expression error for {r.field}")
    return errors

def _get(d: Dict[str, Any], dotted: str):
    cur = d
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur
