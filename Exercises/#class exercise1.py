#class exercise1
#تكتب اسم الوجبه ومكوناتها والوقت اللازم وطريقة التحضير ثم تطبع كل ذالك

class Food:
    def __init__(self,name,ingredients,time,instructions):
        self.food_name=name
        self.ing=ingredients
        self.time=time
        self.inst=instructions


    def __repr__(self):
        return f"Name: {self.food_name}\nIngredients: {self.ing}\nCooking Time: {self.time}\nInstructions: {self.inst} "


def my_mael():
    name=input("Enter recipe name: ")
    ingre=input("Enter ingredients (comma-separated) : ")
    time=input("Enter cooking time: ")
    inst=input("Enter cooking instructions: ")
    print("Recipe added succfully")
    return Food(name,ingre,time,inst)

print("Welcome to Recipe Collection \n")
my_mael1=my_mael()

print("\nDisplaying recip ....\n",my_mael1)
# Spaghatti with meatballs
# pasta,sauce,salt,beef
# 20 minutes
#  1: put the pasta in aboling water. 2: wait 20 minutes. 3: Don't do that