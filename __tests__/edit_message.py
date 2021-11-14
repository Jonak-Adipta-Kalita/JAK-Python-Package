from jak_python_package.edit_message import EditMessage


def remove_spaces():
    message = EditMessage("heLlo woRLd")
    assert message.remove_spaces() == "heLlowoRLd"


def to_lower_case():
    message = EditMessage("heLlo woRLd")
    assert message.to_lower_case() == "hello world"


def to_upper_case():
    message = EditMessage("heLlo woRLd")
    assert message.to_upper_case() == "HELLO WORLD"


def to_title_case():
    message = EditMessage("heLlo woRLd")
    assert message.to_title_case() == "Hello World"
