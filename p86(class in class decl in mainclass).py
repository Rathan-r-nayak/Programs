#declaring inner class in main class
class student:
    def __init__(self,name,section,usn):
        self.name=name
        self.section=section
        self.usn=usn
        self.birth=self.DOB()
    
    class DOB:
        def __init__(self):
            self.dd=11
            self.mm=4
            self.yyyy=2003
s1=student("RATHAN","B","4MW20CS062")
print("NAME:",s1.name)
print(s1.birth.dd,"-",s1.birth.mm,"-",s1.birth.yyyy)