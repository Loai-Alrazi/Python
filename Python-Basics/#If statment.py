#If statment

name="Ali"
country="Yemen"
cname="python course" 
cprice=100

if country == "Yemen" or country=="Msr":
        print(f"Hello {name} you want rigester in {cname} ")
        print(f"becouse you are from {country} the price is ${cprice - 70} ")
elif country == "KSA":        
    print(f"Hello {name} you want rigester in {cname} ")
    print(f"becouse you are from {country} the price is ${cprice - 50} ")

else: print(f"Hello {name} you want rigester in {cname} ") 
print ("H" in {cname})

Admins=["Ali","Ahmed","Mohammed","Aroa","Sali"]
user=input("Enter the admin >").strip().capitalize()

if user in Admins:
      print(f"Ok the {user} is Admin")
      print(f"Hello {user} welcome back")
      option=(input("you want update name or deleted it ?")).strip().capitalize()
      if option == "Update":
            nwneme=(input("Enter the new name for admin ")).strip().capitalize()
            Admins[Admins.index(user)]=nwneme
            print(Admins)
else:
      print(f"The {user} not Admin")      