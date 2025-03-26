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
            print(f"{self.coef[i]}x^{self.degree} + ", end='')
        print(self.coef[0])
        
if __name__ == '__main__':
    a = Poly()
    a.readPoly()
    a.printPoly()