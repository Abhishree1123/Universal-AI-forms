from formdl.codec import encode_cborz, decode_cborz

def test_cborz_roundtrip():
    obj = {"a": 1, "b": "x"}
    blob = encode_cborz(obj)
    out = decode_cborz(blob)
    assert out == obj
