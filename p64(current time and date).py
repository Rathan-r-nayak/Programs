import time
ltime=time.asctime(time.localtime(time.time()))
print("current time",ltime)
i=0
while i<10:
    print("rathan")
    time.sleep(2)
    i+=1

print(time.asctime())