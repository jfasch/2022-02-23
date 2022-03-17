from user import User


def test_id_is_int_ok():
    u = User(1, 'x', 'y', 'z')
    assert u.id == 1
    assert u.firstname == 'x'
    assert u.lastname == 'y'
    assert u.birth == 'z'
    
def test_id_is_int_nok():
    try:
        u = User('666', 'x', 'y', 'y')
        assert False
    except TypeError:
        assert True   # hm, pass would be sufficient

def test_id_is_int_nok_2():
    try:
        u = User([1,2,3], 'x', 'y', 'y')
        assert False
    except TypeError:
        assert True   # hm, pass would be sufficient
