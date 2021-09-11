# EditMessage()

## Initialize

```
from jak_python_package.edit_message import EditMessage

message = input(">> ")
message_passed = EditMessage(message)
```

## Print the Message

```
print_message = message_passed.print()
print(print_message)
```

## Remove Spaces from the String

```
remove_spaces = message_passed.remove_spaces()
print(remove_spaces)
```

## Change to Lower Case

```
lower_cased = message_passed.to_lower_case()
print(lower_cased)
```

## Change to Upper Case

```
upper_cased = message_passed.to_upper_case()
print(upper_cased)
```

## Change to Title Case

```
title_cased = message_passed.to_title_case()
print(title_cased)
```