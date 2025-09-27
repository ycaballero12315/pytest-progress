import pytest

def f():
    raise SystemExit(1)

def test_sys_exist():
    with pytest.raises(SystemExit):
        f()