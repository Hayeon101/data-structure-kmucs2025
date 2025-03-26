class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
    
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self):
        return self.size == self.capacity
        
    def __str__(self):
        return str(self.array[0:self.size])
        
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False
        
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] =  e
            self.size += 1
        
    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1]
                self.size -= 1
                return
            
    def union(self, setB):
        setC = ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
                
        return setC
        
    def intersect(self,setB):
        setC = ArraySet()
        
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
                
        return setC
        
    def difference(self, setB):
        setC = ArraySet()
        
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        
        return setC
        
if __name__ == '__main__':
    S = ArraySet(20)
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(30)
    S.insert(40)
    
    T = ArraySet(20)
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(10)
    T.insert(60)
    
    T.delete(10)
    
    print('S =',S)
    print('T =',T)
    
    print('union(S, T) =', S.union(T))
    print('intersect(S, T) =', S.intersect(T))
    print('difference(S, T) =', S.difference(T))