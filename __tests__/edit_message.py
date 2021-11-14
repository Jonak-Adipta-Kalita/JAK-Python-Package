from jak_python_package.edit_message import EditMessage


def test_remove_spaces():
    message = EditMessage("heLlo woRLd")
    assert message.remove_spaces() == "heLlowoRLd"


def test_to_lower_case():
    message = EditMessage("heLlo woRLd")
    assert message.to_lower_case() == "hello world"


def test_to_upper_case():
    message = EditMessage("heLlo woRLd")
    assert message.to_upper_case() == "HELLO WORLD"


def test_to_title_case():
    message = EditMessage("heLlo woRLd")
    assert message.to_title_case() == "Hello World"
