from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Alex-Benjamin", "Dombroski") == "Dombroski;Alex-Benjamin"

def test_extract_family_name():
    assert extract_family_name("Dombroski; Alex") == "Dombroski"

def test_extract_given_name():
    assert extract_given_name("Dombroski/ Alex") == "Alex"

pytest.main(["-v", "--tb=line", "-rN", __file__])