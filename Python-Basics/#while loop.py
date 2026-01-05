#while loop
import random

secret_num=random.randint(1,10)
print(secret_num)
gusse=int(input("enter your gusse number from 1 to 10 >>"))

while gusse !=secret_num:
    if gusse < secret_num:
       gusse=int(input("No the number input is lower then  try agin>>"))
    elif gusse > secret_num :
        gusse=int( input("No the number input is higher then  try agin>>"))
print(" yes you seccusfull")    
      