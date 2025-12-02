tpl1=(1,3,5,6,2,7)
tpl2 =(11,14,19,12,1,3,1,4)
tt=tpl1 + tpl2 
print(tt)
print(tt.count(1))
print(tt.index(4))#num 4 in indx 13
#print("the index for the element " + tt.index(4)) #error
print("the index for the element {:d}".format(tt.index(4)))
print(f"the index for the element {tt.index(4)}")

tpl3= (1,"a","f")
print(tpl1 + tpl2 + tpl3)
tple4="nostring"
print(type(tple4)) #is string
tple5="nostring",
print(type(tple5)) #is tuple

a=("A","B","C") #tuple Destruct
x , y , z =a
print(x)
print(y)
print(z)