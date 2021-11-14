from jak_python_package.mathematics import Mathematics

number = input(">> ")
number_passed = Mathematics(number)

# Remove Spaces from the String
added_number = number_passed.add(2)

# Change to Lower Case
substracted_number = number_passed.sub(2)

# Change to Upper Case
multiplied_number = number_passed.mul(2)

# Change to Title Case
divided_number = number_passed.div(2)
