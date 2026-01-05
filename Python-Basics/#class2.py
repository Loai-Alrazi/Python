#class2 

class Movies:
    def __init__(self, titel,director,year,genre ):
        self.title=titel
        self.dir=director
        self.year=year
        self.genre=genre
    # onther way to print all atrbutes
    # def __repr__(self):
    #     return f"Titel: {self.title}\nDirector: {self.dir}\nYear: {self.year}\nGenre: {self.genre}"

    
    def display(self,):
        print(f"Titel: {self.title}")
        print(f"Director: {self.dir} ")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
    
    def update_Year(self,new_year):
        self.year=new_year
    

movie1=Movies(titel="Osman bih",director="Mohamed",year=2020,genre="Family")  
# this way with   reper function
# print(movie1)
movie1.display()
movie1.update_Year(2025)

print("\n\n++++++++++++++++++++++++\n\n")
movie2=Movies(titel="Prison break",director="John Kinidi",year=2009,genre="Crime")    
# print(movie2)
movie2.display()
movie2.update_Year(2024)
print("\n\n++++++++++++++++++++++++\n\n")
print(" The edite is \n\n")
# movie1.year=2011
# movie2.year=2015
# print(movie1,"\n")
# print(movie2)
movie1.display()
movie2.display()