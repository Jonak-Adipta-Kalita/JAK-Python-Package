class EditMessage:
    def __init__(self, message: str):
        self.message = message

    def __repr__(self):
        return f"Message: {self.message}"

    def print(self):
        if self.message:
            return self.message
        else:
            print("What do you want to PRINT? (In String Only!!)")
            message = str(input(">> "))
            return message

    def remove_spaces(self):
        if self.message:
            return self.message.replace(" ", "")
        else:
            print("What do you want to REMOVE SPACES for? (In String Only!!)")
            message = str(input(">> "))
            return message.replace(" ", "")
