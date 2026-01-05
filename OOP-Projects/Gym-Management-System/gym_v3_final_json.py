import os
import time
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. كلاس القاعدة (الوراثة)
class Person:
    def __init__(self, first_name, last_name, person_id, password):
        self.f_name = first_name
        self.l_name = last_name
        self.id = person_id
        self.passw = password

# 2. كلاس المستخدم الذي يرث من Person
class User(Person):
    def __init__(self, f_name, l_name, person_id, pas, status='Inactive'):
        super().__init__(f_name, l_name, person_id, pas)
        self.status = status

    def display(self):
        print(f"First Name: {self.f_name}")
        print(f"Last Name: {self.l_name}")
        print(f"ID: {self.id}")
        print(f"Status: {self.status}")
        print("-" * 20)

# 3. دوال إدارة البيانات (JSON)
def save_data(all_users):
    """تحويل الكائنات إلى قواميس وحفظها في ملف JSON"""
    data_to_save = []
    for user in all_users:
        data_to_save.append({
            'f_name': user.f_name,
            'l_name': user.l_name,
            'id': user.id,
            'passw': user.passw,
            'status': user.status
        })
    with open('gym_data.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)

def load_data():
    """تحميل البيانات من ملف JSON وتحويلها إلى كائنات User"""
    if os.path.exists('gym_data.json'):
        try:
            with open('gym_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [User(u['f_name'], u['l_name'], u['id'], u['passw'], u['status']) for u in data]
        except:
            return []
    return []

# 4. وظائف النظام
def add_user():
    f_name = input("Enter first name: ")        
    l_name = input("Enter last name: ")
    while True:
        id_input = input("Enter ID (numbers only): ")
        if id_input.isdigit():
            person_id = int(id_input)
            break
        print("❌ Invalid ID. Please use numbers.")
    password = input("Enter password: ")       
    status = input("Enter status (active/inactive) [Default: inactive]: ")
    return User(f_name, l_name, person_id, password, status if status else 'inactive')

def search_user(all_users):
    clear_screen()
    print("Search by:\n1. ID\n2. First Name\n3. Status")
    choice = input("Your choice: ")
    found = []
    if choice == '1':
        uid = input("ID: ")
        found = [u for u in all_users if str(u.id) == uid]
    elif choice == '2':
        name = input("First Name: ").lower()
        found = [u for u in all_users if u.f_name.lower() == name]
    elif choice == '3':
        stat = input("Status: ").lower()
        found = [u for u in all_users if u.status.lower() == stat]
    
    if found:
        print(f"\n✅ Found {len(found)} member(s):")
        for u in found: u.display()
    else:
        print("\n❌ No members found.")
    input("\nPress Enter to return...")

# 5. البرنامج الرئيسي
all_users = load_data()

while True:
    clear_screen()
    print(f"--- GYM Management System (Users: {len(all_users)}) ---")
    print("1. Add New User\n2. Display All\n3. Search\n4. Save & Exit")
    
    cmd = input("Choice: ")
    if cmd == '1':
        all_users.append(add_user())
        save_data(all_users) # حفظ تلقائي بعد كل إضافة
        print("User added!")
        time.sleep(1)
    elif cmd == '2':
        clear_screen()
        if not all_users: print("No users.")
        else:
            for u in all_users: u.display()
        input("\nPress Enter...")
    elif cmd == '3':
        search_user(all_users)
    elif cmd == '4':
        save_data(all_users)
        print("Data saved. Goodbye!")
        break