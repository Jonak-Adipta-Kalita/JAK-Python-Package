class PrintMessage():
    def __init__(self, message : str):
        self.message = message
    
    def print(self):
        if self.message:
            return self.message
        else:
            print("What do you want to PRINT? (In String Only!!)")
            message = str(input(">> "))
            return message
