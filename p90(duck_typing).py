class laptop:
    def code(self,ide):
        ide.execute()
class VS_code:
    def execute(self):
        print("Compiling\nRunning")
        
a=laptop()
ide=VS_code()
a.code(ide)