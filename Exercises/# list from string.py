# list from string
import random

# lis=[]

# names=input("welcom to 'whose wallet?'\nYou will give me a list of names, " \
# "and I will pick a person to pay \n If you'r ready, enter the names separated by comm\n>>")
# lis=names.split(", ")
# print (lis)
# ## x=len(lis)
# ## print(x, type(x))

# rand=lis[random.randint(0,len(lis)-1)]
# print(f"Plese ask '{rand}' to take his wallet out. Dinner is on him " )

print("welcom to 'whose wallet?'\nYou will give me a list of names, " \
 "and I will pick a person to pay \n")
names=input("If you'r ready, enter the names separated by comm\n>>").split(", ")
print(f"Plese ask '{random.choice(names)}' to take his wallet out. Dinner is on him " )