import time
initial=time.time()
i=0
while i<1000:
    print("rathan")
    i+=1
a=time.time()-initial
print("While loop:",time.time()-initial)
initial2=time.time()
for j in range(1000):
    print("rathan")
print("For loop:",time.time()-initial2)
print("while loop:",a)
print(time.time())


#year (including century, e.g. 1998) month (1-12) day (1-31) hours (0-23) 
# minutes (0-59) seconds (0-59)  weekday (0-6, Monday is 0) 
# Julian day (day in the year, 1-366) DST (Daylight Savings Time) flag (-1, 0 or 1)