from jak_python_package.edit_message import EditMessage

message = input(">> ")
message_passed = EditMessage(message)

# Print the Message
print_message = message_passed.print()

# Remove Spaces from the String
remove_spaces = message_passed.remove_spaces()
