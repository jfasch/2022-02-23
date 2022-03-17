from user import User
import pytest


def test_id_is_int_ok():
    u = User(1, 'x', 'y', 'z')
    assert u.id == 1
    assert u.firstname == 'x'
    assert u.lastname == 'y'
    assert u.birth == 'z'
    
def test_id_is_int_nok():
    with pytest.raises(TypeError):
        u = User('666', 'x', 'y', 'y')

def test_id_is_int_nok_2():
    with pytest.raises(TypeError):
        u = User([1,2,3], 'x', 'y', 'y')
