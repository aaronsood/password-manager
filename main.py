import os
import json
import string
import random

# setup
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)
        print("Created users.json")

# auth

def signup():
    
    username = input("Enter a new username: ")
    password = input("Enter a master password: ")

    with open("users.json", "r") as f:
        users = json.load(f)

    if username in users:
        print("Username already taken. Try another one")
        return
    
    users[username] = password

    with open("users.json", "w") as f:
        json.dump(users, f)
    
    vault_file = f"vault_{username}.json"
    with open(vault_file, "w") as f:
        json.dump({}, f)

    print(f"User '{username}' created successfully with empty vault!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your master password: ")
    with open("users.json", "r") as f:
        users = json.load(f)
    
    if username in users and users[username] == password:
        print(f"Login successful! Welcome, {username}")
        return username
    else:
        print("Login failed. Check your login credentials and try again.")
        return None
    
    with open("users.json", "r") as f:
        users = json.load(f)

        if not users:
            print("No users found. Please create a new account")
            signup()
            with open("users.json", "r") as f:
                users = json.load(f)

logged_in_user = login()
if logged_in_user:
    print("You can now access your passwords vault!")

def get_vault_file(username):
    return f"vault_{username}.json"

# password generator 
def generate_password():
    length = int(input("Password length: "))

    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ("!@#$%^&*()-_+=<>?")

    pool = letters[:]
    if use_numbers:
        pool += numbers
    if use_symbols:
        pool += symbols
    
    if not pool:
        print("You must at least allow letters")
        return None
    
    password_chars = []

    password_chars.append(random.choice(letters))
    if use_numbers:
        password_chars.append(random.choice(letters))
    if use_symbols:
        password_chars.append(random.choice(symbols))
    
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))
    
    random.shuffle(password_chars)
    password = "".join(password_chars)

    print(f"\nGenerated password: {password}\n")
    return password 
    
def add_password(username):
    site = input("Enter site name: ")
    password = input("Enter password: ")

    vault_file = get_vault_file(username)
    with open(vault_file, "r") as f:
        vault = json.load(f)

    vault[site] = password  

    with open(vault_file, "w") as f:
        json.dump(vault, f)

    print(f"Password for '{site}' added successfully!")

def get_password(username):
    site = input("Enter site name to retrieve: ")
    
    vault_file = get_vault_file(username)
    with open(vault_file, "r") as f:
        vault = json.load(f)

    if site in vault:
        print(f"Password for '{site}': {vault[site]}")
    else:
        print(f"No password found for '{site}'.")

def list_passwords(username):
    vault_file = get_vault_file(username)
    with open(vault_file, "r") as f:
        vault = json.load(f)

    if vault:
        print("Your saved passwords:")
        for site, pw in vault.items():
            print(f"{site}: {pw}")
    else:
        print("Vault is empty.")

def delete_password(username):
    site = input("Enter site name to delete: ")

    vault_file = get_vault_file(username)
    with open(vault_file, "r") as f:
        vault = json.load(f)

    if site in vault:
        del vault[site]
        with open(vault_file, "w") as f:
            json.dump(vault, f)
        print(f"Password for '{site}' deleted successfully!")
    else:
        print(f"No password found for '{site}'.")

if logged_in_user:
    while True:
        print("\nVault Menu:")
        print("1. Add password")
        print("2. Get password")
        print("3. List passwords")
        print("4. Delete password")
        print("5. Generate password")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_password(logged_in_user)
        elif choice == "2":
            get_password(logged_in_user)
        elif choice == "3":
            list_passwords(logged_in_user)
        elif choice == "4":
            delete_password(logged_in_user)
        elif choice == "5":
            generate_password()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")