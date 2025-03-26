class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed
    
    def speedUp(self):
        self.speed += 10
    
    def speedDown(self):
        self.speed -= 10
        
    def __str__(self):
        return f"Color : {self.color}, Speed : {self.speed}"
        
if __name__ == '__main__':
    car1 = Car('Black', 0)
    car2 = Car('Red', 100)
    car3 = Car('Yellow')
    
    print(car1)
    print(car2)
    car3.speedUp()
    print(car3)