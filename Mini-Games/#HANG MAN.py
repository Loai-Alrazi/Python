#HANG MAN
import random

items=["bad", "ugly","good"]
rand=random.choice(items)
man=[""""
        +----+
         |    |             
         0    |
        /|\   |
        / \   |
          ==========          


    """ ,
    """"
        +----+
         |    |             
         0    |
        /|\   |
              |
          ==========  
       


    """,
    """"
        +----+
         |    |             
         0    |
        / \   |
              |
          ==========          


    """,
    """"
        +----+
         |    |             
         0    |
              |
              |
          ==========          


    """,
    """"
        +----+
         |    |             
              |
              |
              |
          ==========          


    """,
    """
        +----+
              |             
              |
              |
              |
          ==========          


    """]


display=["-"]*len(rand)
print("".join(display))
live=6
choseagin=[]
while "-" in display and live>0:
    guss=input("Enter your guss char>>").lower()
    if guss not in rand and guss not in choseagin:
        live-=1
        choseagin.append(guss)
        print(f"Try again you have only {live} >")
        print(man[live])
    elif guss in choseagin:
        print(f"this letter is wrong and you chose it befor ")   
    for option in range(len(rand)):
        if rand[option]==guss:
            display[option]=guss
            print(f"Your right ",(display) )
# print(display)       


if live==0:
    print(man[0]) 
else:
    print(""""

    ***********
    YOU WIN!
    ***********      
    """
    )    