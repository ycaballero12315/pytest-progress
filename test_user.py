import pytest
from user_easy import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_element_user(user_manager):
    """Create de fresh instance of UserManager before each test"""
    assert user_manager.add_user('Yoeny', 'hhgdggdj@jfhd.com') == True
    """Get email by key=username"""
    assert user_manager.get_user('Yoeny') == 'hhgdggdj@jfhd.com'

def test_add_ther_user(user_manager):
    user_manager.add_user('Yoeny', 'hhgdggdj@jfhd.com')
    with pytest.raises(ValueError):
        user_manager.add_user('Yoeny', 'hhgdggdjkfdsfds@jfhd.com')