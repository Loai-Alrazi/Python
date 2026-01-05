import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Person:
    def __init__(self, first_name, last_name, person_id, password):
        self.f_name = first_name
        self.l_name = last_name
        self.id = person_id
        self.passw = password

class User(Person):
    def __init__(self, f_name, l_name, person_id, pas, status='Inactive'):
        super().__init__(f_name, l_name, person_id, pas)
        self.status = status

    def display(self):
        print(f"First Name: {self.f_name}")
        print(f"Last Name: {self.l_name}")
        print(f"ID: {self.id}")
        print(f"Status: {self.status}")
        print("*" * 20)

def add_user():
    f_name = input("Enter your first name: ")        
    l_name = input("Enter your last name: ")
    
    while True:
        id_input = input("Enter your ID > ")
        if id_input.isdigit(): # التأكد أن المدخل رقم
            person_id = int(id_input)
            break
        else:
            print("❌ Invalid input. Please enter a valid number for the ID.")

    password = input("Enter your password: ")       
    status = input("Enter the status (active/inactive) or press Enter for 'inactive': ")
    if not status:
       status = 'inactive'
     
    return User(f_name, l_name, person_id, password, status)

def search_user(all_users):
    clear_screen()
    print("Search by:\n1. Membership ID\n2. First Name\n3. Membership Status")
    choice = input("Enter your choice: ")
    found_search = []

    if choice == '1':       
        target_id = input("Enter the ID >> ")
        if target_id.isdigit():
            target_id = int(target_id)
            for user in all_users:
                if user.id == target_id:
                    found_search.append(user)
                    break
    elif choice == '2':
        target_name = input("Enter the first name >> ").lower()
        for user in all_users:
            if user.f_name.lower() == target_name:
                found_search.append(user)
    elif choice == '3':
        target_status = input("Enter the status >> ").lower()
        for user in all_users:
            if user.status.lower() == target_status:
                found_search.append(user)

    if found_search:
        print("\n✅ Member(s) found:")
        for user in found_search:
            user.display() 
    else:
        print("\n❌ Member NOT found.")
    time.sleep(2)    

# Main Program
all_users = []
while True:
    print("\n--- GYM Membership Management ---")
    print("1. Add new user\n2. Display all users\n3. Search for user\n4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        all_users.append(add_user())
        print("User added successfully!")
    elif choice == '2':
        clear_screen()   
        if all_users:
            for user in all_users:
                user.display()
            input("Press Enter to continue...")
        else:
            print("No users to display.")
    elif choice == '3':
        if all_users:
            search_user(all_users)
        else:
            print("No users in the system.") 
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please select 1-4.")