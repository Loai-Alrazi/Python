#Filters

def check_number(num):
    if num >10:
        return num
    
myNums=[1,12,10,4,24,44,3,2]

filtNums=filter(check_number,myNums)

for i in filtNums:
    print(i)

print(" &&& " *10) 
#### NOTES => if return 0 0=false  no data returned
def check_number1(num):
    if num ==0:
        return num #no return any data
   
myNums1=[0,0,1,12,10,4,24,0,44,3,2,0]

filtNums1=filter(check_number1,myNums1)

for i in filtNums1:
    print(i) #nothing in outpot

print(" &&& " *10) 
#So==>
def check_number2(num):
    if num ==0:
        return True #becuse num ==0 

filtNums2=filter(check_number2,myNums1)

for i in filtNums2:
    print(i) # outpot = 0 0 0 0

print(" &&& " *10) 
## another way 
def check_number2(num):
    
        return num >20

filtNums3=filter(check_number2,myNums1)

for i in filtNums3:
    print(i) 

print(" &&& " *10) 
#Example (2) 

def check_name(name):
    
        return name.startswith("o")

myTexts=["Saeed","oSAma","Ali","  Omar","ahMEd","orhan"] 
filtName=filter(check_name,myTexts)

for i in filtName:
    print(i)
print("#"*20)
# Example (3)
# lambda fun
for i in filter( lambda name:name.startswith("o"),myTexts):
    print(i)   