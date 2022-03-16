from user import User


def test_id_is_int():
    u = User(1, 'x', 'y', 'z')
    assert u.id == 1
    assert u.firstname == 'x'
    assert u.lastname == 'y'
    assert u.birth == 'z'
    
