from __future__ import annotations
import json
from pathlib import Path
import click

from .models import FormDLProfile
from .qr import make_qr_png
from .pdf import attach_profile_to_pdf, compute_pdf_sha256
from .validate import validate_profile

@click.group()
def app():
    """FormDL CLI — profiles, QR, PDF-attach, verify, extract (stubs)."""

@app.command()
@click.argument("profile_json", type=click.Path(exists=True))
@click.option("--out", type=click.Path(), required=True, help="PNG output path")
@click.option("--pointer", is_flag=True, help="Treat input as a URI string instead of JSON")
def qr(profile_json, out, pointer):
    """Encode profile as a QR (pointer-mode by default)."""
    if pointer:
        data = Path(profile_json).read_text().strip()
        make_qr_png(data, out)
        click.echo(f"QR saved -> {out}")
        return

    prof = json.loads(Path(profile_json).read_text())
    # Minimal pointer-mode demo: embed a short URI if present, else the form_uid
    payload = prof.get("prompt_pack_uri") or prof.get("schema_uri") or prof.get("form_uid", "formdl")
    make_qr_png(payload, out)
    click.echo(f"QR saved -> {out}")

@app.command()
@click.argument("pdf_in", type=click.Path(exists=True))
@click.argument("profile_json", type=click.Path(exists=True))
@click.option("--out", type=click.Path(), required=True)
def pdf(pdf_in, profile_json, out):
    """Attach a profile JSON to a PDF."""
    attach_profile_to_pdf(pdf_in, profile_json, out)
    click.echo(f"Wrote -> {out}")

@app.command()
@click.argument("profile_json", type=click.Path(exists=True))
def verify(profile_json):
    """Lightweight profile verification (shape + optional template hash)."""
    prof = FormDLProfile(**json.loads(Path(profile_json).read_text()))
    errs = validate_profile(prof)
    if prof.template and "pdf_sha256" in prof.template:
        click.echo("template.pdf_sha256 present: " + prof.template["pdf_sha256"])
    if errs:
        raise SystemExit("\n".join(errs))
    click.echo("Profile OK")

@app.command()
@click.argument("pdf_in", type=click.Path(exists=True))
@click.option("--out", type=click.Path(), required=True)
def extract(pdf_in, out):
    """Stub extraction (demo). In real deployments, hook OCR + LLM here."""
    # For now, just output a demo payload.
    demo = {"status": "not-implemented", "pdf_sha256": compute_pdf_sha256(pdf_in)}
    Path(out).write_text(json.dumps(demo, indent=2))
    click.echo(f"Extraction stub wrote -> {out}")
