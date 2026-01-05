# class exercise2

import os 
import time

def clear_secreen():
     os.system('cls' if os.name=='nt' else 'clear')

class User:
    def __init__(self, first_n,last_n,email , password,stutes="en active"):
        self.first=first_n
        self.last=last_n
        self.email=email
        self.pas=password
        self.stutes=stutes
    
    # def __repr__(self):
    #     return f"{self.first}{self.last}\n{self.email}\n{self.pas}\n{self.stutes}"       

    def display(self,):
        print(f"Frist Name: {self.first}")
        print(f"Last Name: {self.last} ")
        print(f"Email: {self.email}")
        print(f"Password: {self.pas}")
        print(f"Stutes: {self.stutes}")
        print("*"*20)

def add():
    f_name=input("Enter your first name: ")        
    l_name=input("Enter your last name: ")
    email=input("Enter your email: ")
    password=input("Enter your password")       

    return User(f_name,l_name,email,password)







all_user=[]
while True :
    print("Welcom to user management ")
    print("choose an action:\n1.Add new user\n2.Display all users\n3. Exit ")
    choose=int(input("Enter your choice: "))

    if choose==1:
        # print("+++++++++++++")
        all_user.append(add())
        print("user added seccesfully ")
        time.sleep(2)

    elif choose==2:
        clear_secreen()#لحذف الموجود في شاشه الاخراج سابقا
        # نعمل شرط هل القائمه فارغه ام فيها عناصر
        if  all_user:    #==>len(all_user) > 0      
            print("Display all users .....")
            time.sleep(1)
            for i in all_user:              
               i.display()
            time.sleep(2)
        else:
            print("Sorry didn't find eny user to display ")
            time.sleep(2)
    elif choose==3:
        print("Exiting.......")
        break
    else:
        print("plase Choose 1 or 2 or 3 ")
    print(all_user)    