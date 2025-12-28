import os
import json

# check if user already has users.json
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)
        print("Created users.json")
else:
    print("users.json already exists")

def signup():
    
    username = input("Enter a new username: ")
    password = input("Enter a master password: ")

    with open("users.json", "r") as f:
        users = json.load(f)

    if username in users:
        print("Username already taken. Try another one")
        return
    
    users[username] = password

    with open("users.json")