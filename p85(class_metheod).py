class cricket:
    country="INDIA"
    def __init__(self,target,wick_left):
        self.target=target
        self.wickets=wick_left
    @classmethod
    def get_team(cls):
        return cls.country
c1=cricket(378,10)
print(c1.get_team())