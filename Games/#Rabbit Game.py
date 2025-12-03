#Rabbit Game
shap = [ ["  #  ","  #  ","  #  "],["  #  ","  #  ","  #  "],["  #  ","  #  ","  #  "]]
print(f"{shap[0]} \n{shap[1]} \n{shap[2]}")
print("\n@@")
x=(input("where do you want to move @@"))
w=int(x[0])
r=int(x[1])
shap[w-1][r-1]=" @@ "
print(f"{shap[0]} \n{shap[1]} \n{shap[2]}")


