l=10                   #global declaration
m=66                   #global declaration
#-------------------------------------------------------
def rat():
    k=5                #local declaration
    print("k=",k)
    #to change l value globally we have to use global fn.
    global l
    l=l+6            #change 'l' value globally

    print("l=",l)
#-------------------------------------------------------
rat()
print(l)