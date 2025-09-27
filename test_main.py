from main import add, divide

import pytest

def test_add_elems():
    assert add(3,4) == 7
    assert add(4,7) == 11
    assert add(7,9) == 16

def test_exceptions():
    with pytest.raises(ValueError, match="Cannot divide by cero"):
        divide(3,0)