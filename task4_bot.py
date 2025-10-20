def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please provide name and phone number."


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Error: Please provide name and new phone number."


def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    except IndexError:
        return "Error: Please provide contact name."


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        try:
            user_input = input("Enter a command: ")
            
            if not user_input.strip():
                continue
                
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
            
            elif command == "phone":
                print(show_phone(args, contacts))
            
            elif command == "all":
                print(show_all(contacts))
            
            else:
                print("Invalid command.")
        
        except KeyboardInterrupt:
            print("\nGood bye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()