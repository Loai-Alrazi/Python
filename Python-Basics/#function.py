#function

def fun():
    return "Hello python "
print(fun())
x=fun()
print(x)


def addi(n1 , n2):
    if type(n1) == int or type(n2) == int :
        print(n1 + n2) 

    else: print("Enter tow number ")       
    

a=2 
b = 7
addi(a ,b)    

def st(fr , mn , ln):
    print(f"Hello {fr.strip()} {mn.upper():.1s} {ln}")

st("Ali" , "saeed" , "ameen")


lis=[1,4,3,2,5,7]
print(lis)
print(*lis)


def say_hello(x ,*pepoles): # *pepoles => n1 , n2 , n3 , n4
    for name in pepoles:
        print(f"Hello {x}  {name}")

say_hello("enything","Loay","Ali", "Saleh", "Abdo")  


def show_info(name , age , skill="Unknown"):
    print(f"your name is=> {name} and your age {age} your skills {skill}")
show_info("loay",22)  

def show_skills(**my_skill):
    for skname, skvalue in my_skill.items():# you must use .item() with dictionary
         print(f" this is my skills=> {skname} {skvalue}")

show_skills(html="60%", java="70%" , js="77%")
#other way
print(" # " *30)
skills={
    'html':"60%",
    'java':"70%",
    'js':"77%"
}
show_skills(**skills)