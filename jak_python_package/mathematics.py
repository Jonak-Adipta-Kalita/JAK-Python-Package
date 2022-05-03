"""
Mathematics Module
By: BeastNight TV
Website: https://jonakadiptakalita.vercel.app/
"""


class Mathematics:
    """
    Do Mathematics with JAK Python Package
    """

    def __init__(self, number: int):
        """
        :param number: Number to do math with!!
        :type number: Integer
        """
        if number:
            if isinstance(number, int):
                self.number = number
            else:
                raise Exception("Number must be a Integer!!")
        else:
            print("Please Provide a Integer")
            number = input(">> ")

            if isinstance(number, int):
                self.number = number
            else:
                raise Exception("Number must be a Integer!!")

    def __repr__(self):
        return f"Number: {self.number}"

    def add(self, number: int) -> int:
        """
        Add two Numbers
        :param number: Number to Add!!
        :return: Number + new Number

        Basic usage:
            >>> from jak_python_package.mathematics import Mathematics
            >>> number = Mathematics(5)
            >>> number.add(2)
            7
        """
        return self.number + number

    def sub(self, number: int) -> int:
        """
        Subtract two Numbers
        :param number: Number to Subtract!!
        :return: Number - new Number

        Basic usage:
            >>> from jak_python_package.mathematics import Mathematics
            >>> number = Mathematics(5)
            >>> number.sub(2)
            3
        """
        return self.number - number

    def mul(self, number: int) -> int:
        """
        Multiply two Numbers
        :param number: Number to Multilpy!!
        :return: Number * new Number

        Basic usage:
            >>> from jak_python_package.mathematics import Mathematics
            >>> number = Mathematics(5)
            >>> number.mul(2)
            10
        """
        return self.number * number

    def div(self, number: int) -> int:
        """
        Divide two Numbers
        :param number: Number to Divide
        :return: Number / new Number

        Basic usage:
            >>> from jak_python_package.mathematics import Mathematics
            >>> number = Mathematics(5)
            >>> number.div(2)
            2.5
        """
        return self.number / number
