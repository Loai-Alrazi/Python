email="loay_alrazi@gmail.com"
print(email)
print(email.index("@"))
print(email[:email.index("@")])

#program clucate age
age=(int(input("plese enter your age ").strip()))
month=age * 12
week= month*4
days= age*365
huors=days* 24
minut=huors*60
print(f"your age >{age}")
print(f"your age month >{month}")
print(f"your age week >{week}")
print(f"your age days >{days}")
print(f"your age huors >{huors}")
print(f"your age minut >{minut}")