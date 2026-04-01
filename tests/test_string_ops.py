from py_regexcite.string_ops import strsplit1

def test_strsplit1():
    assert strsplit1("a,b,c", ",") == "a"