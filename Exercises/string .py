n ="loay"
age = 26
sal=3000
print("my name is %s  I'm %d and my salary is %.2f $ "%(n,age,sal))
print("my name is {}  I'm {} and my salary is {} $ ".format(n,age,sal))
print("my name is {:s}  I'm {:d} and my salary is {:.1f} $ ".format(n,age,sal))
print(f"My name is {n}  I'm {age} and my salary is {sal} $ ")
a , b , c = "one" , "tow" , "three"
print("Hello {} , {} , {}".format(a,b,c,))#Hello one , tow , three
print("Hello {1} , {0} , {2}".format(a,b,c))#Hello tow , one , three
x , y , z = 1,2,3
print("Hello {1:d} {2:d} {0:.2f}".format(x,y,z))
print("Hello {1:d} {2:d} {0:.2f}".format(x,y,z))