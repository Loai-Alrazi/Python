#for loop
#attendees=["Alise", "Bob", "Marten"]
attendees_input=input("enter the names: ")
attendees=attendees_input.split(", ")
#attendees_input=input("enter the names: ").split(", ")
yestask=[]
notask =[]
for person in attendees:
    print("\n",person)
    response=input("is this person attending ? (yes/no): ")
    if response=="yes":
        print("Attendance confirmed")
        yestask.append(person)
    else:
         print("Attendance not confirmed")
         notask.append(person)
    print("-------")  
show=input("do you show yor all task (yes/no) >>")
if show=="yes" :
    print("\n  ********your OK tasks is ********\n" ,yestask ) 
    print("\n  ********your NOT tasks is ********\n" ,notask ) 
    