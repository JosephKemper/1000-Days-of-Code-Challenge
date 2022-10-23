from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest



# Write test_make_full_name so that it tests make_full_name with various names, 
# including long names, short names, and hyphenated names. 
# Fix the mistake in the make_full_name function.
def test_make_full_name ():
    assert make_full_name ("Cho", "Lee") == "Lee; Cho"
    assert make_full_name ("Sallindrinia", "Mitchelson") == "Mitchelson; Sallindrinia"
    assert make_full_name ("Giovonie", "Haskil-Trolerson") == "Haskil-Trolerson; Giovonie"
    assert make_full_name("Sally", "Brown") == "Brown; Sally"


# Write test_extract_family_name so that it tests extract_family_name with various names, 
# including long names, short names, and hyphenated names.
def test_extract_family_name ():
    assert extract_family_name ("Lee; Cho") == "Lee"
    assert extract_family_name ("Mitchelson; Sallindrinia") == "Mitchelson"
    assert extract_family_name ("Haskil-Trolerson; Giovonie") == "Haskil-Trolerson"
    assert extract_family_name ("Brown; Sally") == "Brown"

# Write test_extract_given_name so that it tests extract_given_name with various names, 
# including long names, short names, and hyphenated names. 
# Fix the mistake in the extract_given_name function.
def test_extract_given_name ():
    assert extract_given_name ("Brown; Sally") == "Sally"
    assert extract_given_name ("Haskil-Trolerson; Giovonie") == "Giovonie"
    assert extract_given_name ("Lee; Cho") == "Cho"
    assert extract_given_name ("Mitchelson; Sallindrinia") == "Sallindrinia"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

