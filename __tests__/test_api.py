from jak_python_package.api import API

RAPIDAPI_KEY = "d3474315fcmshe6f03eb826f16bcp181f82jsn7d262d2601be"


def test_get_jak():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_jak()


def test_get_brawl_stars():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_brawl_stars()


def test_get_miraculous():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_miraculous()


def test_get_mughal_empire():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_mughal_empire()


def test_get_genshin_impact():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_genshin_impact()


def test_get_alexis_response():
    jak_api = API(rapidapi_key=RAPIDAPI_KEY)

    assert jak_api.get_alexis_response("Hello!!")
