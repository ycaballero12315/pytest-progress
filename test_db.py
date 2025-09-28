from db import Database
import pytest

@pytest.fixture
def db_instance():
    data_base = Database()
    yield data_base
    data_base.data.clear()

def test_add_user_id(db_instance):
    db_instance.add_user_id(1, 'Yoe')
    assert db_instance.get_user_id(1) == "Yoe"

def test_add_duplicate_user(db_instance):
    db_instance.add_user_id(1, 'Yoe')
    with pytest.raises(ValueError, match='User already exists'):
        db_instance.add_user_id(1, 'Pedro')

def test_delete_user(db_instance):
    db_instance.add_user_id(2, 'Bob')
    db_instance.delete_user_id(2)
    assert db_instance.get_user_id(2) is None