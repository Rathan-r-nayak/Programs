#calling the fn. again & again
def fac_rec(a):           #fn. definition
    if (a==1):
        return 1
    else:
        ac=a*fac_rec(a-1)     #ac=5*fac_rec(5-1)     function called again and now a=4
        return ac

a=int(input("Enter a no."))        #assume a=5
c=fac_rec(a)
print(c)


"""

a=5

ac=5*{ fac_rec(5-1) }
ac=5*{ 4*(fac_rec(4-1))) }
ac=5*{ 4*(3*(fac_rec(3-1))) }
ac=5*{ 4*(3*(2*(fac_rec(2-1)))) }            fac_rec(1)   returning 1
ac=5*{ 4*(3*(2*(1))) }
ac is returned to c

"""