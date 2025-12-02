#loop
a=0
while a <10:
    print(a)
    a+=1
print("loop is end")
myfrinds=["Ali","Ahmed","Mohammed","Aroa","Sali","Salah","frid","Bashar"]
x=0
while x <len(myfrinds):
    print(f"#{(x+1)} {myfrinds[x]}")
    x+=1


my_fav_web=[]
maxweb=5

while maxweb > 0:
    web=input("enter website with out https// ")
    my_fav_web.append(f"https//{web.strip().lower()}")
    maxweb-=1
    print (f"the web site is added {maxweb} places left")
    print(my_fav_web)
else:
    print("Book mark is full , you cant add more website") 

# Check if List not empty
z=0
if len(my_fav_web) > z: 
    #Sort List
    my_fav_web.sort()      
    index=0
    print("Printting the list of websites in your BookMarks ")
    while index < len(my_fav_web):
        print(my_fav_web[index])
        index+=1