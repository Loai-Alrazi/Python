print("Hello python");print("hi")

if True:
    print("yes")
    if True:
       print("no")
#fvvkd
# commend
print(type(12))
print(type("dv"))
print(3)
print(type((1,2,3,4,5)))
print(type([1,3,5]))
print(type({"one" : 1 ,"tow":2}))
print(type(2==2))
help("keywords")
x="hi"
y="loai"
z=x +" "+y
print(z)
#أخذ عنصر من المجموعة 
mystring="I love python" #12 char
print(mystring[0])#the first char
print(mystring[-1])#the last char
print(mystring[5])#the first char
# اخذ مجموعة عناصر من المجموعة 
#[start:end] end not included
#[start:end:steps]
print(mystring[3:7])
print(mystring[:7]) #it will start from indx 0
print(mystring[3:]) #it will stop to end
print(mystring[:]) #it will print all
print(mystring[:13:1]) #it will print full
print(mystring[::1]) #it will print full
print(mystring[::2]) #it will print 0 not 1 and 2 not 3
print(len(mystring))# عدد العناصر في المتغير
#لازالة الفراغات 
xx="      Hi    python    "
print(xx.strip()) #ازالة الفراغات من اليمين والشمال 
print(xx.rstrip()) #ازالة الفراغات من اليمين فقط 
print(xx.lstrip()) #ازالة الفراغات من الشمال فقط 
print(len(xx.lstrip())) #ا
print(xx.lstrip("##")) #ا
print(xx.title()) 
print(xx.upper()) 
print(xx.lower()) 
print(xx.split()) #list
print(xx.center(40,"$")) #
print(xx.count("py")) #
print(xx.count("py",0,)) #start indx 0 to end
print(xx.swapcase()) #change char state
print(xx.startswith("I"))




