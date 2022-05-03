from jak_python_package.api import API

RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"


def test_get_jak():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_jak()
    assert type(jak_api.get_jak()) == dict


def test_get_brawl_stars():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_brawl_stars()
    assert type(jak_api.get_brawl_stars()) == dict


def test_get_miraculous():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_miraculous()
    assert type(jak_api.get_miraculous()) == dict


def test_get_mughal_empire():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_mughal_empire()
    assert type(jak_api.get_mughal_empire()) == dict


def test_get_genshin_impact():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_genshin_impact()
    assert type(jak_api.get_genshin_impact()) == dict


def test_get_alexis_response():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_alexis_response("Hello!!")
    assert type(jak_api.get_alexis_response("Hello!!")) == str
