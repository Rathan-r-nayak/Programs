a={
    "mob1":{"m1":"Poco","m2":"Redmi","m3":"oppo"},
    "mob2":("Samsung","I phone","huwai"),
    "mob3":"Realme"
}
a["mob4"]="Vivo"
print("mob1-----------",a["mob1"].keys())
print("\n\na------------",a.keys())
print("\n\na--------------",a.values())
print("\n\nmob1 value-----",a["mob1"])
del a["mob3"]
print("\n\na---(mob3 deleted)---",a)
a.update({"mob5":"htc"})
print("\n\nmob5 updated",a)
#a.get(a["mob2"])
print(a["mob1"])