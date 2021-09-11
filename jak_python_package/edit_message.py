import re


class EditMessage:
    def __init__(self, message: str):
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

    def print(self) -> str:
        return self.message

    def remove_spaces(self) -> str:
        return self.message.replace(" ", "")

    def to_lower_case(self) -> str:
        return self.message.lower()

    def to_upper_case(self) -> str:
        return self.message.upper()

    def to_title_case(self) -> str:
        return re.sub(
            r"[A-Za-z]+('[A-Za-z]+)?",
            lambda word: word.group(0).capitalize(),
            self.message,
        )
