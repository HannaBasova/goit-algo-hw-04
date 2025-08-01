def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."
def show_all_contacts(contacts):
    for name, phones in contacts.items():
        return name, phones



def phone_username(args,contacts: dict)-> str|None:
    for arg in args:
        if arg in contacts:
            arg =contacts[arg]
            return arg
        else:
            return "No such contact."




def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            for name, phones in contacts.items():
                print(name, phones)
        elif command == "phone":
            print(phone_username(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
