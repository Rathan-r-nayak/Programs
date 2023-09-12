class mobile:
    def __init__(self,proc,rom,ram,refr):
        self.processor=proc
        self.rom=rom
        self.ram=ram
        self.refresh_rate=refr
             
    @classmethod
    def power(self,battery,charger,backup):
        return f"{self.__name__} has {battery} battery, {charger} charger & {backup} backup time"
        

poco=mobile("Snap Dragon 730G","256GB","8GB","120HZ") #OBJECT
redmi=mobile("Helio G30","128GB","6GB","60HZ")        #OBJECT

pocopower=poco.power("4500MH","27W","8hrs")

print(poco.refresh_rate,"\n",redmi.refresh_rate)
print(pocopower)