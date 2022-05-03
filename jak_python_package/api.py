"""
JAK API Module
By: BeastNight TV
Website: https://jonakadiptakalita.vercel.app/
"""

import requests, json


class API:
    """
    Use the JAK API
    """

    def __init__(self, rapidapi_key: str):
        """
        :param rapidapi_key: The RapidAPI Key to be used
        :type rapidapi_key: String
        """
        self.RAPIDAPI_KEY = rapidapi_key
        self.BASE_URL = "https://jak_api.p.rapidapi.com"

    def get_jak(self) -> dict:
        """
        Get JAK
        :return: JAK's Details!!

        Basic usage:
            >>> from jak_python_package.api import API
            >>> jak_api = API("YOUR_RAPID_API_KEY")
            >>> message.get_jak()
        """
        resp = requests.get(
            f"{self.BASE_URL}/jak",
            headers={
                "X-RapidAPI-Host": "jak_api.p.rapidapi.com",
                "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            },
        )

        return json.loads(resp.text)

    def get_brawl_stars(self) -> dict:
        """
        Get Brawl Stars
        :return: Brawl Stars Data!!

        Basic usage:
            >>> from jak_python_package.api import API
            >>> jak_api = API("YOUR_RAPID_API_KEY")
            >>> message.get_brawl_stars()
        """
        resp = requests.get(
            f"{self.BASE_URL}/brawlStars",
            headers={
                "X-RapidAPI-Host": "jak_api.p.rapidapi.com",
                "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            },
        )

        return json.loads(resp.text)

    def get_miraculous(self) -> dict:
        """
        Get Miraculous
        :return: Miraculous Data!!

        Basic usage:
            >>> from jak_python_package.api import API
            >>> jak_api = API("YOUR_RAPID_API_KEY")
            >>> message.get_miraculous()
        """
        resp = requests.get(
            f"{self.BASE_URL}/miraculous",
            headers={
                "X-RapidAPI-Host": "jak_api.p.rapidapi.com",
                "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            },
        )

        return json.loads(resp.text)

    def get_mughal_empire(self) -> dict:
        """
        Get Mughal Empire
        :return: Mughal Empire Data!!

        Basic usage:
            >>> from jak_python_package.api import API
            >>> jak_api = API("YOUR_RAPID_API_KEY")
            >>> message.get_mughal_empire()
        """
        resp = requests.get(
            f"{self.BASE_URL}/mughalEmpire",
            headers={
                "X-RapidAPI-Host": "jak_api.p.rapidapi.com",
                "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            },
        )

        return json.loads(resp.text)

    def get_genshin_impact(self) -> dict:
        """
        Get Genshin Impact
        :return: Genshin Impact Data!!

        Basic usage:
            >>> from jak_python_package.api import API
            >>> jak_api = API("YOUR_RAPID_API_KEY")
            >>> message.get_genshin_impact()
        """
        resp = requests.get(
            f"{self.BASE_URL}/genshinImpact",
            headers={
                "X-RapidAPI-Host": "jak_api.p.rapidapi.com",
                "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            },
        )

        return json.loads(resp.text)

    def get_alexis_response(self, message: str) -> str:
        """
        Get Alexis Response
        :return: Alexis's Response!!

        Basic usage:
            >>> from jak_python_package.api import API
            >>> jak_api = API("YOUR_RAPID_API_KEY")
            >>> message.get_alexis_response()
        """
        resp = requests.get(
            f"{self.BASE_URL}/ai",
            headers={
                "X-RapidAPI-Host": "jak_api.p.rapidapi.com",
                "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            },
        )

        return json.loads(resp.text)
