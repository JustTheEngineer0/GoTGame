import json
import os
from character import characterScript

def main():
    while True:
        print("\nMain Menu")
        print("1. Enter Character Menu")
        print("2. Exit Game")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            characterScript()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()


#Ideas for systems: Travel system for both roads and ports
#Ravens and social interactions
#Shops
#Random Events
#Enemy Encounters
#recommend adding a "test feature" menu choice on the main menu