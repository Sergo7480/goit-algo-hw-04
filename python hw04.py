def parse_command(command):
    
    pass
contacts = {}  

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added.")

def change_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name):
    if name in contacts:
        print(f"Phone number for {name}: {contacts[name]}")
    else:
        print("Contact not found.")

def show_all():
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")
def main():
    while True:
        command = input("Введіть команду: ")
        keywords = command.lower().split()
        if "add" in keywords:
            _, name, phone_number = keywords
            add_contact(name, phone_number)
        elif "change" in keywords:
            _, name, new_phone_number = keywords
            change_contact(name, new_phone_number)
        elif "phone" in keywords:
            _, name = keywords
            show_phone(name)
        elif "all" in keywords:
            show_all()
        elif "exit" in keywords or "close" in keywords:
            print("Good bye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()