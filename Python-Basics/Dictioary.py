#Dictioary

dic={
    "id":1,
    "name":"Ali",
    "age":27

}
print(dic)
print(dic.keys())
print(dic.values())
print(dic["age"])
dic.update({"age":33})
print(dic)
dic.setdefault("country","Yemen")
print(dic)
print(dic.popitem())
print(dic.items())


laguge={
    "one":{
        "name":"english",
        "how" :20,
        "wer" :"taiz"

    },
    "tow":{
        "name":"franch",
        "how" :10,
        "wer" :"Sanaa"

    },



}
print(laguge)
print(laguge["one"]['name'])
a=("w","e","r")
b="x"
print(dict.fromkeys(a,b))