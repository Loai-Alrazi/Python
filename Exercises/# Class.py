# Class

from datetime import date

class Profile:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.language=language
    def __repr__(self):
        return f"profile(name is  '{self.name}' , email = '{self.email}' , language = '{self.language} )"

class Messge:
    def __init__(self,sender,recive,messg,date):
        self.sender=sender
        self.recive=recive
        self.messg=messg
        self.date=date
    
    def __repr__(self):
        return f"The Sender is '{self.sender}', The recive is '{self.recive}', Message is('{self.messg}', Date is {self.date})"

class Prodact:
    def __init__(self,pro_name,price,desc,eval):
        self.pro_name=pro_name
        self.price=price
        self.desc=desc
        self.eva=eval
    def __repr__(self):
            return f"the name of produdt {self.pro_name} and the price is {self.price} and the evaiution is {self.eva}"

# for User profile class
profile1= Profile(name="Loai Abdullah",email="loayalrazi@gmail.com",language="Python")        
profile2=Profile("Ahmed Hatem","ahmedh@gmail.com","PHP")
profile3=Profile("Mohammed","moha@gmail.com","Dart")
print(profile1)
# print(profile2.name,profile2.email,profile2.language)
print(profile2)
print(profile3)

# Message Class
messg1=Messge("Ali","Omar","Hi Omer how are you ? please call me",date.today())
print(messg1)

# Produdt 

product1=Prodact("Shampo","$7","its's very nice for hear",'****')
print(product1)



