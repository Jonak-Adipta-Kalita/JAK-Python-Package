from jak_python_package.edit_message import EditMessage

message = input(">> ")
message_passed = EditMessage(message)

# Remove Spaces from the String
remove_spaces = message_passed.remove_spaces()

# Change to Lower Case
lower_cased = message_passed.to_lower_case()

# Change to Upper Case
upper_cased = message_passed.to_upper_case()

# Change to Title Case
title_cased = message_passed.to_title_case()
