# -*- coding: utf-8 -*-

import userdb_csv

def test_woswasi():
    users = userdb_csv.read_noheader('tests/Users-noheader-cp1252.csv')
    assert len(users) == 5

    assert users[0].id == 1
    assert users[0].firstname == 'Jörg;DI'
    assert users[0].lastname == 'Faschingbauer'
    assert users[0].birth == '19.6.1966'

    assert users[1].id == 2
    assert users[1].firstname == 'Caro'
    assert users[1].lastname == 'Faschingbauer'
    assert users[1].birth == '25.4.1997'

    assert users[2].id == 3
    assert users[2].firstname == 'Johanna'
    assert users[2].lastname == 'Faschingbauer'
    assert users[2].birth == '11.6.1995'

    assert users[3].id == 4
    assert users[3].firstname == 'Philipp'
    assert users[3].lastname == 'Lichtenberger'
    assert users[3].birth == '6.4.1986'

    assert users[4].id == 5
    assert users[4].firstname == 'Elizabeth II'
    assert users[4].lastname == 'Queen'
    assert users[4].birth == '1.1.1900'

