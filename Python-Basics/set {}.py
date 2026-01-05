# set {}
myset1={1,4,"A" , "ian",6,12}
print(myset1)
#print(myset1[1:4])#error
#myset2={1,4,"A" , "ian",6,12,[2,4,5]}#TypeError: unhashable type: 'list'
myset2={1 , "ian",6,12,(2,4,5), 8}
print(myset2)
print(myset2.union(myset1)) #==update(with add other elemants )
myset1.add(22)
myset1.remove(22)
myset1.discard(22)#==remove with out error
print("+" * 40)
print (myset1)
print (myset2)
print (myset2.difference(myset1))
#print (myset2.difference_update(myset1))
#print(myset2)
print(myset2.intersection(myset1))