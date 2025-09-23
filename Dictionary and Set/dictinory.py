dict={
    "name":"Sayeel Abbas",
    "age":19,
    "Gpa":[3.59,3.53]
}
#Print all dict
print(dict)
#print Seprate
print(dict["age"])
#use key to make changes
dict["age"]=18
print(dict["age"])
#add words and keys that doesnot even exist on a dictionary
dict["city"]="Hyderabad"
print(dict)
#print only they keys of a dictinoary
print(dict.keys())
#return all the values
print(dict.values())
#return key and value paris as an tuple
print(dict.items())
#return the key according to the value
print(dict.get("name"))
#update the values of dictionary
dict.update({"name":"Saim"})
print(dict)