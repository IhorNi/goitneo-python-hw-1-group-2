"""CLI assistant functions"""

from typing import Optional

Contacts = dict[str, str]
CommandArguments = list[str]


HELP_ERROR_MESSAGE = """Supported functions:
- 'add': Add new contact, the correct format is 'add username phone'
- 'change': Change existing contact, the correct format is 'change username phone'
- 'phone': Print existing contact number, the correct format is 'phone username'
- 'all': Print all existing contact numbers if any, the correct format is 'all'
- 'exit' | 'close': Close the app, the correct format 'exit' and 'close'
"""


def parse_input(user_input: str) -> tuple[str, Optional[CommandArguments]]:
    if not user_input.strip():
        return "", None
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    if len(args) == 0:
        return cmd, None

    return cmd, *args

def add_contact(args: CommandArguments, contacts: Contacts) -> str:
    if args is None or len(args) < 2:
        return "Error: 'add' command expects two arguments 'name' and 'phone'."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: CommandArguments, contacts: Contacts) -> str:
    if args is None or len(args) < 2:
        return "Error: 'change' command expects two arguments 'name' and 'phone'."

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated."
    else:
        return f"No contact named {name} exists."


def print_phone(args: CommandArguments, contacts: Contacts) -> str:
    if args is None or len(args) < 1:
        return "Error: 'phone' command expects one argument 'name'."

    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"No contact named {name} exists."


def print_all(contacts: Contacts) -> str:
    if not contacts:
        return "No contacts stored."
    else:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
