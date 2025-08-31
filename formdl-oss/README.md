# FormDL — Invisible AI Superpowers for Legacy Forms

**FormDL** is an open-source spec + reference implementation for making *unchanged-looking* forms
(PDFs, scans, even faxes) **AI-native**. We embed *invisible intelligence* — identifiers, anchors,
schema, validation codex, and LLM prompt packs — into a profile carried by a tiny QR/DataMatrix or
as an attached file inside the PDF. End-users see the same form; downstream AI gets structure.

- 🔖 **Stable form identifiers** (`form_uid` + versioning)
- 📐 **Anchors**: coordinates and types for robust OCR/vision extraction
- 📚 **Schema & ontology mapping** (JSON Schema + optional domain mapping)
- ✅ **Validation codex**: ranges/regex, cross-field rules, quality signals
- 🧠 **Prompt pack**: compact LLM guidance for consistent extraction
- 🔒 **Integrity**: bind profile to a template hash; optional signing
- 🔌 **Routing**: destinations, SLAs, approvers

> Think: ZUGFeRD/iXBRL-style hybrid docs + GS1 Digital Link + LLM-ready instructions — but for any form.

---

## Quickstart

```bash
# 1) Install (editable)
pip install -e .

# 2) Create a QR (pointer mode) from a FormDL profile
formdl qr encode examples/profiles/sample_formdl.json --out examples/pdfs/sample_form_qr.png

# 3) Embed the profile inside a PDF as an attachment
formdl pdf attach examples/pdfs/sample_template.pdf examples/profiles/sample_formdl.json   --out examples/pdfs/sample_template_with_profile.pdf

# 4) Verify & extract (demo pipeline; OCR/LLM hooks are modular)
formdl verify examples/profiles/sample_formdl.json
formdl extract examples/pdfs/sample_template_with_profile.pdf --out /tmp/extracted.json
```

> The reference implementation focuses on **correct packaging, validation, and pluggable extraction**.
> OCR/LLM calls are abstracted; bring your favorite engine or gateway.

---

## Spec (v0.1) — Minimal fields

```json
{
  "form_uid": "org.example.sample.v1",
  "issuer": "example.org",
  "version": "1.0.0",
  "variant": {"lang":"en-GB","region":"UK"},
  "template": {"pdf_sha256": "<hash-of-visible-template>"},
  "anchors": [{"field_id":"person.nin","page":1,"bbox":[100,600,200,20],"type":"string","required":true}],
  "schema_uri": "https://registry.example.org/schemas/sample/1.0.0.json",
  "validation": {
    "rules":[{"field":"person.nin","regex":"^[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]$"}]
  },
  "prompt_pack_uri": "https://registry.example.org/prompts/sample/1.0.0",
  "destinations": [{"type":"api","uri":"https://intake.example.org"}]
}
```

### Design goals
- **Zero UX change**: Same-visible PDFs/faxes/scripts.
- **Deterministic parsing** where possible; **LLM-assisted** where helpful.
- **Cryptographic binding** to templates to prevent drift.
- **Composable** with existing standards (PDF/A, GS1, HL7 FHIR, XBRL).

---

## Repo layout

```
formdl-oss/
  ├─ src/formdl/           # library + CLI
  ├─ examples/             # sample profiles, schemas, prompts, PDFs
  ├─ tests/                # lightweight tests
  ├─ .github/workflows/    # CI
  ├─ pyproject.toml
  ├─ LICENSE
  └─ README.md
```

---

## Roadmap

- [ ] Optional **COSE/JOSE** signatures for profiles (VC-friendly envelopes)
- [ ] DataMatrix/PDF417 support (offline CBOR payloads)
- [ ] PDF/A-3 conformance helper
- [ ] Rich quality scorecards + remediation prompts
- [ ] Labeling tool for anchors + template hashing

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Security

Never embed secrets in profiles. Consider signing profiles when used in regulated environments.
See [SECURITY.md](SECURITY.md).

---

## License

Apache-2.0. See [LICENSE](LICENSE).
