"""
Unit tests for the ata4t package.
"""

# Import package, test suite, and other packages as needed
import ata4t
import pytest 
import sys

def test_ata4t_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "ata4t" in sys.modules

 # At the beginning of a test can change the result of the tests
#@pytest.mark.xfail
#@pytest.mark.skip()