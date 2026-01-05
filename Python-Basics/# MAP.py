# MAP

def formatText(text):
    return f"- {text.strip().capitalize()} -"

myTexts=["oSAma","Ali","  Omar","ahMEd"] 

# i will use varible and 
# myfGormatedData = map(formatText,myTexts) #if you don't want use var you can use map alredy
# print(myfGormatedData)
# for name in myfGormatedData:
#     print(name)

# use map already
for name in map(formatText,myTexts):
    print(name) 


print("="*10)
# if i want return Data like List
for name in list(map(formatText,myTexts)):
    print(name) 
  
print("="*10)
# if you want use Map with lambda function  

    # return f"- {text.strip().capitalize()} -"

myTexts1=["Saeed","oSAma","Ali","  Omar","ahMEd"] 
for name in map( lambda text:f"- {text} -"  ,myTexts):
    print(name) 
print("="*10)
for name in list(map( lambda text:f"- {text} -"  ,myTexts)):
    print(name)    