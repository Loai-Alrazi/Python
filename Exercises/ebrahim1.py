# x=input("enter tow num > ")
# print(type(x))
# w=int(x[0])
# y=int(x[1])
# print(w+ y)
#################################
import random 
# ran=random.randint(1000,9999)
# pin =(input("enter PIN 4 numbers > "))
# #print(len(pin))
# if len(pin) !=4:
#     print("enter 4 number for PIN ") 
# elif pin ==ran:
#     print (f"ok {pin}")
# else:
#     print("try agin")
#     print(f"becouse the computer choise {ran}")
######################################################
print("chois method to toss the coin >\n1- by random()\n2- by randint()")
ran1=random.randint(0,1)
ran2=random.random()
chois_method=int(input("Enter your choise (1 or 2) : "))

if chois_method ==1 :
    chose_gues=input("enter your guess (Heads or Tails): ").capitalize()
    if chose_gues=="Heads" and ran1==0 or chose_gues=="Tails" and ran1==1:
        print ("You succes")
    else :
        print("You lost")  
elif    chois_method ==2 :
    chose_gues1=input("enter your guess (Heads or Tails): ").capitalize()
    if chose_gues1=="Heads" and ran2>=0.5 or chose_gues1=="Tails" and ran2<0:
        print ("You succes")
    else :
        print("You lost ")       
else :"plese enter 1 or 2"
