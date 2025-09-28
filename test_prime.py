from prime import isprime
import pytest

@pytest.mark.parametrize('num, expected',[
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False)
])
def test_in_prime(num, expected):
    assert isprime(num) == expected