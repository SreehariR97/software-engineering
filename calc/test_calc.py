import calc


def test_calc_add():
    """test calc add() function"""
    assert calc.add(2, 2) == 4
    assert calc.add(2.0, 2.0) == 4.0
    assert calc.add(-2.0, -2.0) == -4.0


def test_calc_mul():
    """test calc add() function"""
    assert calc.mul(2, 2) == 4
    assert calc.mul(2.0, 2.0) == 4.0
    assert calc.mul(-2.0, -2.0) == 4.0

if __name__ == "__main__":
    test_calc_mul()
    print("done")