# Reduce

from functools import reduce



def sumNm(num1,num2):
    return num1 +num2

myNumbers=[1,3,4,6,33,2]

resulte=reduce(sumNm,myNumbers)
print(resulte)
print("#"*5)
# Example with lambda
result1= reduce(lambda num1,num2 : num1 +num2,myNumbers)
print(resulte)
print("#"*5)