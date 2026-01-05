#جدول الضرب+ join
# num=int(input("Enter the number >> "))
# for i in range (1,11):
#     print(num ," * " ,i ," = ", num*i ,"\n")

# name= "Ibrahim"

# print(name[::-1]) # outpot is=> miharbI عكس

santance=input("Enter sentance ")
word=santance.split()
reversed_word = word[::-1] 
print(reversed_word)

reversed_sentanse =" ".join(reversed_word)

print(reversed_sentanse)
