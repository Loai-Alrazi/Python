#لعبة حجر ورقة مقص
import random

rock_d='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper_d='''
    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_d='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



print("Welcom to the Rock, paper, scissors game:\n" \
"Press Enter to continue or type (Help) for the rules")
chois=input("Enter your choise (rock, paper, scissors):>")
#show the draw

if chois=="rock":
    print("Your choise is ",rock_d)
elif chois=="paper":
    print("Your choise is ",paper_d)
elif chois== "scissors":
    print("Your choise is ",scissors_d)   
#lis=["rock", "paper", "scissors"]
#if chois in lis:
cop_chois=random.choice(["rock", "paper", "scissors"])
if cop_chois=="rock":
    print("the computer chose: ",rock_d)
elif cop_chois=="paper":
    print("the computer chose: ",paper_d)
elif cop_chois== "scissors":
    print("the computer chose: ",scissors_d)   

if chois =="rock" and cop_chois=="scissors" or chois=="scissors" and cop_chois=="paper" or chois=="paper" and cop_chois=="rock":
    print (f"your choise is {chois} and the computer choise {cop_chois} you WIN")
elif chois==cop_chois : print (f"you choise the same your {chois} and the computer choise {cop_chois} try agin") 
else: print(f"your choise is {chois} and the computer choise {cop_chois} you LOST")
#else:print("plese choise (rock, paper, scissors)")    
    