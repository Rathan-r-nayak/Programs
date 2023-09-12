#declaring outside the main class
class student:
    def __init__(self,name,section,usn):
        self.name=name
        self.section=section
        self.usn=usn
    
    class DOB:
        def __init__(self):
            self.dd=11
            self.mm=4
            self.yyyy=2003
s1=student("RATHAN","B","4MW20CS062")
birth=student.DOB()
print("NAME:",s1.name,"\nusn:",s1.usn,"\nsection:",s1.section)
print(birth.dd,"-",birth.mm,"-",birth.yyyy)