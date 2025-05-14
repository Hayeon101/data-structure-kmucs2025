M = 13

class HashTable:
    def __init__(self):
        self.table = [0] * M

    def hashFn(self, key):
        return key % M

    def hashFn2(self, key):
        return 11 - (key % 11)

    def insert(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M  # Linear proving
            # bucket = (hashVal + i ** 2) % M  # Quadratic proving
            bucket = (hashVal + i * self.hashFn2(key)) % M # Double Hashing

            if self.table[bucket] == 0:
                self.table[bucket] = key
                break

    def search(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M
            # bucket = (hashVal + i ** 2) % M
            bucket = (hashVal + i * self.hashFn2(key)) % M

            if self.table[bucket] == 0:
                return -1
            elif self.table[bucket] == key:
                return bucket

    def delete(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M
            # bucket = (hashVal + i ** 2) % M
            bucket = (hashVal + i * self.hashFn2(key)) % M

            if self.table[bucket] == 0:
                print("No key to delete.")
            elif self.table[bucket] == key:
                print(f"Delete Key({key}) at bucket({bucket}).")
                HT.table[bucket] = -1  # 들어왔다 나간 방
                return bucket

    def display(self):
        print('\nBucket   key')
        print('=============')

        for i in range(M):
            print(f"HT[{i:2d}] :   {self.table[i]:2d}")

if __name__ == '__main__':
    HT = HashTable()
    data = [45,27,88,9,71,60,46,38,24]
    # data = [10,20,30,40,33,46,50,60]

    for d in data:
        print(f"h({d})={HT.hashFn(d):2d}", end=' ')
        HT.insert(d)
        print(HT.table)

    HT.display(); print()

    print('Search(46) ---> ', HT.search(46))
    HT.delete(9); HT.display(); print()

    print('Search(46) ---> ', HT.search(46))