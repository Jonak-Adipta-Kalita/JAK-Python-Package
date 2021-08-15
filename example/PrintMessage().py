from jak_python_package.print_message import PrintMessage

message = input(">> ")
message_to_print = PrintMessage(message).print()

print(message_to_print)
