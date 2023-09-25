
di={"name":"Rathan R Nayak",
    "age":20}

print("name:",di.get("name","rat"))
print("country",di.get("country","India"))

di.setdefault("age",99)
di.setdefault("branch","cse")
print(di)