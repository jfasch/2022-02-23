from user import User
import birthstat

def test_birth_stat():
    users = [
        User(1, 'Joerg', 'Faschingbauer', '19.6.1966'),
        User(2, 'Joerg', 'Faschingbauer', '19.6.1966'),
        User(3, 'Joerg', 'Faschingbauer', '19.6.1966'),
        User(4, 'Joerg', 'Faschingbauer', '19.6.1966'),
        User(5, 'Joerg', 'Faschingbauer', '19.6.1966'),
        User(6, 'Caro', 'Faschingbauer', '25.4.1997'),
        User(7, 'Joerg', 'Faschingbauer', '19.6.1966'),
        User(8, 'Elizabeth, II', 'Queen', '1.1.1900'),
    ]

    stat = birthstat.BirthStat()
    stat.count(users)

    assert stat.num_occurences('19.6.1966') == 6
    assert stat.num_occurences('25.4.1997') == 1
    assert stat.num_occurences('1.1.1900') == 1
    assert stat.num_occurences('2.1.1900') == 0
