#لعبة هانج مان
import random
from shlex import join
import string

from numpy import append
word=["yemen","mesr","emarate"]
rand=random.choice(word)
print(rand)
# impt =[]
# for x in rand:
#     impt.append('-')
#====>
impt =['-']*len(rand)
print(impt)

life=6
while "-" in impt and life>0:
    user_ch=input("enter your guss char >")
    if user_ch not in rand:
        life-=1
           
    #  z=rand.index(y)
    for position in range (len(rand)):
       if rand[position]==user_ch:
            impt[position]=user_ch
            # print(position)
    print(f" ".join(impt))
  
    print (f"you have only{life} try ")  
            
if life ==0: 
    print("You lose ")
    print(""""
        +----+
         |    |             
         0    |
        /|\   |
        / \   |
          ==========          


    """
    )

else:
    print(""""
    
    ***********
    YOU WIN!
    ***********      
    """
    )