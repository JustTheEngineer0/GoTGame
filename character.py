import json
import os

# Character data structure
character = {
    "name": "",
    "status": "",
    "house": None,
    "bastard": False,
    "age": 0,
    "gender": "",
    "stats": {
        "Leadership": 1,
        "Strength": 1,
        "Agility": 1,
        "Intelligence": 1,
        "Wisdom": 1,
        "Constitution": 1
    },
    "inventory": {
        "Head": None,
        "Chest": "Cloth Shirt",
        "Legs": "Cloth Leggings",
        "Hands": None,
        "Feet": "Leather Boots",
        "Neck": None,
        "Back": None,
        "Ring": None,
        "Main Hand": None,
        "Second Hand": None
    },
    "currency": {
        "Gold Dragons": 0,
        "Silver Stags": 5,
        "Copper Stars": 10
    }
}

def create_character():
    print("Create Your Character")
    character["name"] = input("Enter character name: ")

    # Choose status
    while True:
        status = input("Choose status (Noble, Commoner, Slave): ").capitalize()
        if status in ["Noble", "Commoner", "Slave"]:
            character["status"] = status
            break
        else:
            print("Invalid choice. Please select Noble, Commoner, or Slave.")

    # If Noble, ask for house
    if character["status"] == "Noble":
        character["house"] = input("Enter noble house: ")
    else:
        character["house"] = None

    # Option to be a bastard
    while True:
        bastard = input("Is the character a bastard? (yes/no): ").lower()
        if bastard in ["yes", "no"]:
            character["bastard"] = True if bastard == "yes" else False
            break
        else:
            print("Please enter 'yes' or 'no'.")

    #Setting Age
    value = int(input("Enter age (18-80): "))
    if 18 <= value <= 80:
        character["age"] = value
    else:
        print("Value must be between 18 and 80.")
   
    # Setting Gender
    while True:
        gender = input("Enter gender (male/female): ").lower()
        if gender in ["male", "female"]:
            character["gender"] = gender
            break
        else:
            print("Please enter 'male' or 'female'.")
            
    # Setting Stats
    statPoints = 12
    while statPoints > 0:
        print("Assign stats Leadership, Strength, Agility, Intelligence, Wisdom, Constitution")
        print(f"\nPoints Remaining: {statPoints}")
        for stat in character["stats"]:
            while True:
                value = int(input(f"Enter {stat} (0-4): "))
                if 0 <= value <= 4:
                    if statPoints - value >= 0:
                        character["stats"][stat] = character["stats"][stat] + value
                        statPoints = statPoints - value
                        print(character["stats"][stat])
                        print(f"\nPoints Remaining: {statPoints}")
                        break
                    else:
                        print(f"That value is too high. Points Remaining: {statPoints}")
                else:
                    print("Points to be added must be between 0 and 4.")

def new_func(totalStats):
    print(totalStats)

def save_character(filename="character_data.json"):
    with open(filename, "w") as f:
        json.dump(character, f, indent=4)
    print("Character data saved.")

def load_character(filename="character_data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            character.update(data)
        print("Character data loaded.")
    else:
        print("No saved character data found.")

def show_character():
    print("\nCharacter Details")
    print(f"Name: {character['name']}")
    print(f"Status: {character['status']}")
    if character["house"]:
        print(f"House: {character['house']}")
    if character["bastard"]:
        print("Bastard: Yes")
    else:
        print("Bastard: No")
    print(f"Age: {character['age']}")
    print(f"Gender: {character['gender']}")
    print("Stats:")
    for stat, value in character["stats"].items():
        print(f"  {stat}: {value}")
    
    print("Inventory:")
    for slot, item in character["inventory"].items():
        print(f"  {slot}: {item if item else 'Empty'}")
        
    print("Currency:")
    for slot, item in character["currency"].items():
        print(f"  {slot}: {item}")

def characterScript():
    while True:
        print("\nCharacter Menu")
        print("1. Create a new character")
        print("2. Load existing character")
        print("3. Save character")
        print("4. Show character details")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_character()
        elif choice == '2':
            load_character()
        elif choice == '3':
            save_character()
        elif choice == '4':
            show_character()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select from the menu.")

