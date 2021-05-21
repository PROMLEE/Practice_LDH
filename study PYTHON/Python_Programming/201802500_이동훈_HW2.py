class Calc:
    def __init__(self, v = 0):
        self.value = v

    def print(self):
        print(self.value)

    def setvalue(self, v):
        self.value = v

    def getvalue(self):
        return self.value

    def add(self, n):
        self.value += n

    def minus(self, n):
        self.value -= n


cal1 = Calc()
cal2 = Calc(5)
cal1.setvalue(10)
cal1.add(20)
cal1.minus(5)
cal1.print()
cal2.add(cal1.getvalue())
cal2.print()