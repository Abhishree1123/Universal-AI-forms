from formdl.models import FormDLProfile

def test_profile_fingerprint_stable():
    p = FormDLProfile(
        form_uid="org.example.sample.v1",
        issuer="example.org",
        version="1.0.0",
        schema_inline={"type": "object"}
    )
    fp1 = p.fingerprint()
    fp2 = p.fingerprint()
    assert fp1 == fp2 and len(fp1) == 64
