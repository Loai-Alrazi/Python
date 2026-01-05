# built in funaction

myTexts1=["Saeed","oSAma","Ali","  Omar","ahMEd"] 


for i in myTexts1:
    print(i)

print("@"*7) 

myTxtCounter= enumerate(myTexts1)
for i in myTxtCounter:
    print(i)
print("#" *7 )
#example
print ("Example")
myTxtCounter3= enumerate(myTexts1) 
for count, text in myTxtCounter3:
    print(f"{count} - {text}")
print("$"*7)


myTxtCounter1= enumerate(myTexts1,20)
for i in myTxtCounter1:
    print(i)
print("%"*7)

    