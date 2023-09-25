class car:
    company="Tesla"
    tyres=4
    @classmethod
    def changetyres(cls):
        cls.tyres=8

o=car()
print(o.tyres)
o.changetyres()
print(o.tyres)