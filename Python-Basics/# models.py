# models

from datetime import datetime

import termcolor
import pyfiglet
# لطباعة اي تنسيق للتاريخ في بايثون ادحل على الموقع التالي
# python's strftime directives


# print(dir(termcolor))
# print(dir(pyfiglet))
print(pyfiglet.figlet_format("Loay"))
print(termcolor.colored("Loay",color="red"))
print(termcolor.colored(pyfiglet.figlet_format("Loay"),color="yellow"))

# print the current time
print(datetime.now())
# print the current time with out date
print(datetime.now().time())
print(" $ "*5)
# print the current time hour
print(datetime.now().time().hour)
print(" $ "*5)
# print the current year
print(datetime.now().year)
print(" # "*10)
# print start and end of date
print(datetime.min)
print(datetime.max)
print(" # "*10)
print(dir(datetime.now()))
# print start and end of date
# print(datetime.time.min)
# print(datetime.time.max)
print(" # "*10)
print(datetime(1998,10,11))