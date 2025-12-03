#Coin Game  
import random

#print("chois method to toss the coin >\n1- by random()\n2- by randint()")
chode_method=input("chois method to toss the coin >\n1- by random()\n2- by randint()\n> ")
if chode_method=="1":
    compu_rund=random.random()
    if compu_rund >=0.5:
        compu_choise="heads"
    else :
        compu_choise="tails"
elif chode_method=="2":
    compu_rund=random.randint(0,1)
    if compu_rund ==1:
        compu_choise="heads"
    else :
        compu_choise="tails"        
else :
    print("Plese enter (1 or 2)")        

choise=input("enter your guess (Heads or Tails): ").lower()  
if choise ==  "Heads" and compu_choise=="heads":
    print("You win")
elif choise==compu_choise:
    print("You win")
else :
    print("You lose")
 #   print("Plese enter (Heads or Tails) ")  
print(f"the computer choise is {compu_choise}")      