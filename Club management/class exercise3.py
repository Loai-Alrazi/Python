#class exercise 3 after clear
import os
import time


def clear_screen():
     os.system('cls' if os.name=='nt' else 'clear')

class User():
    def __init__(self,f_name,l_name,id,pas,status='Anactive'):
        self.f_name=f_name
        self.l_name=l_name
        self.id=id
        self.pas=pas
        self.status=status

    def display(self,):
        print(f"Frist Name: {self.f_name}")
        print(f"Last Name: {self.l_name} ")
        print(f"ID: {self.id}")
        # print(f"Password: {self.pas}")
        print(f"Stutes: {self.status}")
        print("*"*20)

def add():
    f_name=input("Enter your first name: ")        
    l_name=input("Enter your last name: ")
    id=input("Enter your id: ")
    password=input("Enter your password")       
    stutes=input("Enter the stutes or press Enter (anactive)")
    if not stutes: #if user input active
       stutes='anactive'#if user press enter
     
    return User(f_name,l_name,id,password,stutes)



def search(all_user):
    found_search=[]
    clear_screen()
    print("search by:\n1. Membership ID\n2. First Name\n3. Membership Status")
    search=input("Enter your way to search: ")
    if search=='1':       
            user_want=input("Enter the ID >> ")
            for i in all_user:
                if user_want==i.id:                  
                    found_search.append(i)
                    break #لان الرقم لا يتكرر لشخصين
            
    elif search=='2':
        user_want=input("Enter the first name >> ")
        for i in all_user:
            if user_want.lower()==i.f_name.lower():
                found_search.append(i)
    elif search=='3' :
            clear_screen()
            user_want=input("Enter the stutes >> ")
            for i in all_user:
                if user_want.lower()==i.stutes.lower():
                 found_search.append(i)
    else:
        print("Please enter the number choise ")
    if found_search:
        print("Member is found ")
        for i in found_search:
            i.display() 
    else:
        print("Member NOT found ")
    time.sleep(2)    



print("Welcome to GYM Membership Management\n")

all_user=[]

while True :
    print("Welcom to user management ")
    print("choose an action:\n1.Add new user\n2.Display all users\n3. Search for user\n4. Exit ")
    choose=int(input("Enter your choice: "))
    if choose==1:
        clear_screen()
        all_user.append(add())
        time.sleep(2)
        print("user added successfully ")
    elif choose==2:
        clear_screen()   
        if all_user:
            for i in all_user:
                i.display()
            time.sleep(3)
        else:
            clear_screen()
            print  ("No find for display....")
            time.sleep(2) 

    elif choose==3:
        clear_screen()
        if all_user:
            search(all_user)
        else:
            print("No found any users") 
        time.sleep(2)       
       
    else:
        print("plase Choose 1 or 2 or 3 ")             