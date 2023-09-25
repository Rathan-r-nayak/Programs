#a=open("sample_e44.txt","r")
with open("sample_e44.txt") as a:
    p=a.read()
if "Twinkle" in p:
    print("yes Twinkle is present")
else:
   print("not present")
