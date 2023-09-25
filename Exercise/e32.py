dict1={
    "name":"rathan",
    "sem":3,
    "usn":"4MW20CS062"
}
print(tuple(dict1.keys()))
print(tuple(dict1.values()))
print(dict1.get("rat"))   #gives none as rat is not present in dict as key
dict1.update({"age":18})
print(dict1)
print(dict1.items())