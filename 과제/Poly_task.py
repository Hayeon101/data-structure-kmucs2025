class Poly:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.degree = 0
        self.coef = [None] * capacity
        
    def readPoly(self):
        self.degree = int(input("다항식의 차수를 입력 : "))
        for i in range(self.degree, -1, -1):
            coef = int(input(f" {i}차 항의 계수 : "))
            self.coef[i] = coef
            
    def printPoly(self):
        for i in range(self.degree, 0, -1):
            print(f"{self.coef[i]}x^{i} + ", end='')
        print(self.coef[0])
        
    def addPoly(self, PolyB):
        c = Poly()
        c.degree = max(self.degree, PolyB.degree)
        for i in range(c.degree, -1, -1):
            p1 = self.coef[i] if self.coef[i] else 0
            p2 = PolyB.coef[i] if PolyB.coef[i] else 0
            c.coef[i] = p1 + p2
            
        return c
    
    def evaluatePoly(self, x):
        value = 0
        for i in range(self.degree, -1, -1):
            value += self.coef[i] * (x**i)

        return value
        
if __name__ == '__main__':
    a = Poly()
    a.readPoly()
    a.printPoly()
    b = Poly()
    b.readPoly()
    b.printPoly()
    c = a.addPoly(b)
    c.printPoly()
    v = c.evaluatePoly(2)
    print(v)