from address import extract_city, \
    extract_state,extract_zipcode
import pytest

# write a test function named test_extract_city that verifies 
# that the extract_city function works correctly.
def test_extract_city():
    assert extract_city ("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city ("4996 Rd A NE, Moses Lake, WA 98837") == "Moses Lake"

# Write a test function named test_extract_state 
# that verifies that the extract_state function works correctly.
def test_extract_state ():
    assert extract_state ("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state ("4996 Rd A NE, Moses Lake, WA 98837") == "WA"

# Write a test function named test_extract_zipcode 
# that verifies that the extract_zipcode function works correctly.
def test_extract_zipcode ():
    assert extract_zipcode ("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode ("4996 Rd A NE, Moses Lake, WA 98837") == "98837"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
