class details:
    def __init__(self):
        self.name="Rathan R Nayak"
        self.age=18
        self.birth=self.DOB()
    class DOB:
        def __init__(self):
            self.dd=11
            self.mm=4
            self.yyyy=2003
a=details()
print(a.birth.dd)