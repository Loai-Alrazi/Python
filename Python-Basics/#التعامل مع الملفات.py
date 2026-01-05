#التعامل مع الملفات
import os
print(os.getcwd())# لمعرفة مسار البايثون وملفاته 

myfile=open("lesson1.txt")# اذا ما طلع نقوم باضافة المسار للملف
print(myfile.name) #file data project
print(myfile.mode)
print(myfile.encoding)

print(myfile.read())
print(myfile.read(5))
print(myfile.readline())
print(myfile.readline())
print(myfile.readline(4))
print(myfile.readlines())
print(type(myfile.readlines()))

for line in myfile:
    print(line)
    if line.startswith("5"):
        break

#close the file 
myfile.close() 
# myfile.write("Hi ") #deleted old and added new write
myfile1=open("lesson2.txt","w")
myfile1.write("hello\n"*1000)

mylist=["Ali\n","Ahmed","Omar"] 
myfile1.writelines(mylist)  #if list to write

myfile1=open("lesson2.txt","a")# a if you dont delete the old words in the file
myfile1.write("hello\n"*5 )
myfile1.write("hello\n" )
myfile1.write("hello\n\n\n" )
myfile1.write("testing the position" )

 #  تعمل اقتطاع للملف بحجم البت المكتوب والباقي تحذفه
#  myfile1.truncate(20)
print(myfile1.tell()) #to know the position
myfile1.seek(5) #to read after 6 byte
print(myfile1.read())
# to move file
# os.remove("C:\dsdvsvvsvvvsv.txt")
