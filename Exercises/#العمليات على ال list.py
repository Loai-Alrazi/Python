#العمليات على ال list

# color=[]
# add=input("enter the color > ")
# color.append(add)
# add2=(input("do you want add onther color "))
# if add2 =='yes':
#     add=input("enter the color > ")
#     color.append(add)
# else : print("ok")
# print(f"your favorite color is {color}")


#my library project
#Step (1)
mylib=[]
mywish=[]
add=input("enter the name of a book you own : ")
mylib.append(add)
add=input("enter the name of another  book you own : or press 'Enter' to skip " )
if add : # == if add != ''
    mylib.append(add)
print("Your Library : " , mylib)
# Step (2)
add =input("enter the name of book you wish to have in the future:\n ")
mywish.append(add) 
add=input("enter the name of another  book you you wish to have in the future : or press 'Enter' to skip\n" )
if add :
    mywish.append(add)
    print(f"Your Wishlist: {mywish}")
#Step (3)    
add=input("enter the name of book from your wishlist that you've  acquired (or press 'Enter' to skip):\n ")
if add in mywish:
    mylib.append(add)
    print("Update Library: ", mylib)
    mywish.remove(add)
    print(f"Update Wishlist : ", mywish)