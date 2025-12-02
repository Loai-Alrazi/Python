#class3


class User:
    def __init__(self, first_n,last_n,email , password,stutes="en active"):
        self.first=first_n
        self.last=last_n
        self.email=email
        self.pas=password
        self.stutes=stutes
    
    def __repr__(self):
        return f"{self.first}{self.last}\n{self.email}\n{self.pas}\n{self.stutes}"       


def info():
    f_name=input("Enter your first name: ")        
    l_name=input("Enter your last name: ")
    email=input("Enter your email: ")
    password=input("Enter your password")       

    return User(f_name,l_name,email,password)



user1=info()
print(user1)
user1=info()
print(user1)