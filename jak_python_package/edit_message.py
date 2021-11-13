"""
Edit Message Module
By: BeastNight TV
Website: https://jonakadiptakalita.herokuapp.coom/
"""


class EditMessage:
    """
    Edit any Message/Text
    """

    def __init__(self, message: str):
        """
        :param message: Message to Edit!!
        """
        if message:
            if isinstance(message, str):
                self.message = message
            else:
                raise Exception("Message must be a String!!")
        else:
            print("What Message do you want to Edit? (In String Only!!)")
            message = input(">> ")

            if isinstance(message, str):
                self.message = message
            else:
                raise Exception("Message must be a String!!")

    def __repr__(self):
        return f"Message: {self.message}"

    def remove_spaces(self) -> str:
        """
        Remove Spaces from Message
        :return: Message but Removed Spaces!!
        """
        return self.message.replace(" ", "")

    def to_lower_case(self) -> str:
        """
        Remove Spaces from Message
        :return: Message but Lower Cased!!
        """
        return self.message.lower()

    def to_upper_case(self) -> str:
        """
        Remove Spaces from Message
        :return: Message but Upper Cased!!
        """
        return self.message.upper()

    def to_title_case(self) -> str:
        """
        Remove Spaces from Message
        :return: Message but Title Cased!!
        """
        return self.message.title()
