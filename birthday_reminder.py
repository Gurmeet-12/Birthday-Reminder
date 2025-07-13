import json
import os
from datetime import datetime

DATA_FILE = "birthdays.json"

def load_birthdays():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_birthdays(birthdays):
    with open(DATA_FILE, "w") as f:
        json.dump(birthdays, f, indent=4)

def add_birthday(birthdays):
    name = input("Enter name: ").strip()
    date_str = input("Enter birthday (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        return
    birthdays[name] = date_str
    save_birthdays(birthdays)
    print(f"Birthday added for {name}!")

def show_birthdays(birthdays):
    if not birthdays:
        print("No birthdays saved yet.")
        return
    print("Saved birthdays:")
    for name, date_str in birthdays.items():
        print(f"- {name}: {date_str}")

def main():
    birthdays = load_birthdays()
    while True:
        print("\nOptions:\n1. Add Birthday\n2. Show Birthdays\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_birthday(birthdays)
        elif choice == "2":
            show_birthdays(birthdays)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
