#string 
import string
import random

num=[4,5,3,2,7,5,8,9,0]
ran_num=random.choices(num, k=2)
print(ran_num)
ran_char=random.choices(string.ascii_letters,k=4)
print("\n", ran_char)



sent=input("plese enter the sentanc:> ")
# sent=string.ascii_letters
# print(sent)

#the raight code is:
new_sent=""
for x in sent:
    if x not in string.punctuation:
        new_sent+=x
print(new_sent)        