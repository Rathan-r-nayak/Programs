from traceback import print_tb


class bus:
    b_name="KSRTC"
    def __init__(self):
        self.fare=2000
        self.seats=1

    def detail(self):
        print("_______________STATUS____________________")
        print(f"--------Welcome To {self.b_name}--------\n")
        print(f"bus fare       :{self.fare}")
        print(f"number of seats:{self.seats}")
        print("_________________________________________")
    def book(self):
        print("Ticket Booked")
        print("🚌HAPPY JOURNEY🚌")
        self.seats-=1


pas=bus()
pas.detail()
num=int(input("how many tickets you required:"))
i=0
while(i<num):
    if (pas.seats>0): 
        book_t=int(input("press \"1\" for BOOK TICKET:"))
        if book_t==1:
            pas.book()
    else:
        print("😞 Sorry seats are full 😔")
    pas.detail()
    i+=1
print("_________________________________________")