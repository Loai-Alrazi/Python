#class exercise 3 after clear
import os
import time


def clear_screen():
     os.system('cls' if os.name=='nt' else 'clear')



class Person():
    def __init__(self,frist_name,last_name,id,password):
        
        self.f_name=frist_name
        self.l_name=last_name
        self.id=id
        self.passw=password




class User(Person):
    def __init__(self,f_name,l_name,id,pas,status='Anactive'):
        
        self.status=status
        super().__init__(f_name,l_name,id,pas)# الخصائص التي ورثها من الكلاس ادمن


    def display(self,):
        print(f"Frist Name: {self.f_name}")
        print(f"Last Name: {self.l_name} ")
        print(f"ID: {self.id}")
        # print(f"Password: {self.pas}")
        print(f"status: {self.status}")
        print("*"*20)

def add():
    f_name=input("Enter your first name: ")        
    l_name=input("Enter your last name: ")
    
    while True:
        id_input=(input("Enter your ID > "))
        try:# you must input integer 
         id=int(id_input) 
         break # اذا نجح التحويل اخرج من الدواره 
        except ValueError:
            # 3. إذا فشل التحويل (المستخدم أدخل نصاً)، اطبع رسالة خطأ واستمر في الحلقة
            print("❌ Invalid input. Please enter a valid number for the ID.")

    password=input("Enter your password")       
    status=input("Enter the status or press Enter (anactive)")
    if not status: #if user input active
       status='anactive'#if user press enter
     
    return User(f_name,l_name,id,password,status)



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
    while True: # دواره اذا ادخل المستخدم رقم او حرف غير الاختيارات الاربعة
        choose_input=input("Enter your choice: ")
        try: # اذا كان الرقم المدخل ضمن الخيارات الاربعه 
            if int(choose_input) <5 or int(choose_input) >0:
                choose=int(choose_input)
                break
        except ValueError:
         print("❌ Invalid input. Please enter a valid number [1 , 2 , 3 ,4] for the choose.")    
    
    if choose==1:
        # clear_screen()
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
       
    elif choose==4:
        break
               