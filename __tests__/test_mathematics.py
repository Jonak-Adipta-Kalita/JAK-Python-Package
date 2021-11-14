from jak_python_package.mathematics import Mathematics


def test_add():
    number = Mathematics(5)
    assert number.add(2) == 7


def test_sub():
    message = Mathematics(5)
    assert message.sub(2) == 3


def test_mul():
    message = Mathematics(5)
    assert message.mul(2) == 10


def test_div():
    message = Mathematics(5)
    assert message.div(2) == 2.5
