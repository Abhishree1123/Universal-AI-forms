# Universal-AI-forms

FormDL (Universal-AI-forms)
Universal-AI-forms is an open-source project that makes any legacy form—PDFs, scans, or faxes—"AI-native" by attaching an invisible digital profile. This approach provides a universal, future-proof solution for intelligent document processing, eliminating manual data entry and minimizing the need for constant human intervention.

FormDL treats forms not as static images, but as self-describing, intelligent documents, ready for an agentic AI future.

🌟 Why FormDL?
Zero UX Change: Keep existing forms and workflows. FormDL works without altering the visual layout of your documents.

Agentic Intelligence: Embeds intelligence directly into the form itself, guiding AI agents for precise extraction.

Future-Proof: Designed to get better over time. As LLMs become faster and cheaper, FormDL's approach scales universally without requiring a re-engineering of your entire pipeline.

Abstracts SME Need: Reduces reliance on Subject Matter Experts for every new form extraction task.

Occam's Razor of Intelligence: Compresses complex data, validation rules, and LLM prompts into a lean, actionable profile.

Portable & Auditable: Profiles can be embedded directly in a PDF or referenced via a stable QR code, ensuring strong co-location and auditability.

💡 How It Works (High-Level Architecture)
The core of FormDL is the Profile, a JSON file that acts as the "brain" of a form. This profile is invisibly bound to the document and contains:

Anchors: Precise coordinates (bbox) for each field on the form.

Schema: The JSON schema for the structured output.

Validation Codex: Rules (regex, min/max) for data integrity.

LLM Prompt Pack: Hints and few-shot examples to guide an LLM for accurate extraction.

Identifiers: form_uid and template.pdf_sha256 for versioning and cryptographic binding to the exact template.

The processing pipeline is a clean, three-step flow:

Detect Profile: The system reads an embedded JSON file from the PDF or follows a URL from a QR code.

Process: It uses the anchors to perform targeted OCR, then sends the raw data and the prompt pack to an LLM for structuring and validation against the schema and validation rules.

Route: The final structured JSON is routed to a specified destination (API, queue, etc.) for further processing.




📦 Repo Layout
formdl-oss/
  ├─ src/formdl/
  │   ├─ models.py            # Pydantic models for profiles, anchors, etc.
  │   ├─ codec.py             # CBOR+zlib encoder/decoder for offline payloads
  │   ├─ qr.py                # QR code generator (pointer mode)
  │   ├─ pdf.py               # Attaches JSON profile to a PDF
  │   ├─ validate.py          # Validation utilities
  │   └─ cli.py               # Click-powered CLI
  │
  ├─ examples/
  │   ├─ profiles/            # Full example profiles
  │   ├─ schemas/             # Example JSON schemas
  │   ├─ prompts/             # Example LLM prompt packs
  │   └─ pdfs/                # Sample PDF templates
  │
  ├─ tests/                   # Basic correctness tests
  ├─ .github/workflows/ci.yml # Python 3.11 CI
  └─ README.md                # This file!
🚀 Quickstart
Clone the repository:

Bash
git clone https://github.com/your-username/formdl.git
cd formdl
Install dependencies:

Bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
Run tests to ensure everything is working:

Bash
pytest
Try a demo command (Pointer Mode):
This creates a QR code with a pointer to the sample profile.

Bash
formdl qr examples/profiles/sample_formdl.json --out examples/pdfs/sample_form_qr.png
Try a demo command (Embedded Mode):
This embeds the profile JSON directly into a PDF.

Bash
formdl pdf examples/pdfs/sample_template.pdf examples/profiles/sample_formdl.json --out examples/pdfs/sample_template_with_profile.pdf
🤝 Contributing
We welcome contributions from everyone! FormDL is an open-source project and we believe that a strong community is key to building a robust and universal standard.

Suggested Areas for Contribution:

Extraction Integration: Replace the cli.py:extract stub with a real OCR + LLM pipeline using your favorite providers (e.g., Google Vision, AWS Textract).

Security & Integrity: Implement cryptographic signing for profiles (COSE/JOSE) and a signature verification step.

More Encodings: Add support for other 2D barcodes like DataMatrix and PDF417 for the offline CBOR mode.

Tooling: Help build a simple web-based Anchor Labeling Tool or a read-only registry server.

Please read our CONTRIBUTING.md for more details on how to get started.

FormDL is a project led by Abhishek Kodi from Greater Manchester, UK.
