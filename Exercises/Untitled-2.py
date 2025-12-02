#

def multi(x):
    for i in (range(1,11)):
        print(f"[ {x}* {i}] ={i*x}")
multi(int(input("Enter the number>>")))        


def info (name , age):
    print(f"your name is {name} and your age = {age}")
info("Ali",33) #your name is Ali and your age = 33
info(22, "Ahmed")#your name is 22 and your age = Ahmed
info(name="Ali", age=18)#your name is Ali and your age = 18
