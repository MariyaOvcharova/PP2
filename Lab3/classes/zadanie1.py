class Stroka:
    def getStr(self):
        self.str = input()
    def printStr(self):
        print(self.str.upper())

obj = Stroka()
obj.getStr()
obj.printStr()