from ArrayList import ArrayList

# 배열 구조의 리스트를 이용한 라인 편집기 프로그램
'''
doc = ArrayList()
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")
    
    if command == 'i':
        pos = int(input(" 입력행 번호: "))
        line = input(" 입력행 내용: ")
        doc.insert(pos, line)
    elif command == 'd':
        pos = int(input(" 삭제행 번호: "))
        doc.delete(pos)
    elif command == 'r':
        pos = int(input(" 변경행 번호: "))
        line = input(" 변경행 내용 : ")
        doc.delete(pos)
        doc.insert(pos, line)
    elif command == 'p':
        print("Line Editor")
        for i in range(doc.size):
            print(f'[ {i}] {doc.getEntry(i)}')
    elif command == 'l':
        file = open('Test.txt', 'r')
        doc.size = 0
        while True:
            line = file.readline()
            if not line:
                break
            doc.insert(doc.size, line.strip())
            doc.size += 1
        file.close()
    elif command == 's':
        file = open('Test.txt','w')
        for i in range(doc.size):
            line = doc.getEntry(i) + '\n'
            file.write(line)
        file.close()
    elif command == 'q':
        break
    else:
        print("잘못된 메뉴를 입력하셨습니다\n")
        continue
'''

class LineEditor(ArrayList):
    def __init__(self):
        super().__init__()
        self.file = 'Test.txt'
    
    def replace_line(self,pos,line):
        self.delete(pos)
        self.insert(pos, line)
        
    def print_line(self):
        print("Line Editor")
        for i in range(self.size):
            print(f"[ {i}] {self.getEntry(i)}")
        
    def load_file(self):
        with open(self.file, 'r') as f:
            self.size = 0
            while True:
                line = f.readline()
                if not line:
                    break
                self.insert(self.size, line.strip('\n'))
                # self.size += 1
        
    def save_file(self):
        with open(self.file, 'w') as f:
            for i in range(self.size):
                f.write(self.getEntry(i))
                if i != self.size-1:
                    f.write('\n')
                
if __name__ == '__main__':
    doc = LineEditor()
    
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기 s-저장, q-종료 => ")
        
        if command == 'i':
            pos = int(input(" 입력행 번호: "))
            line = input(" 입력행 내용: ")
            doc.insert(pos, line)
            
        elif command == 'd':
            pos = int(input(" 삭제행 번호: "))
            doc.delete(pos)
            
        elif command == 'r':
            pos = int(input(" 변경행 번호: "))
            line = input(" 변경행 내용: ")
            doc.replace_line(pos, line)
            
        elif command == 'p':
            doc.print_line()
            
        elif command == 'l':
            doc.load_file()
            
        elif command == 's':
            doc.save_file()
            
        elif command == 'q':
            break
            
        else:
            print("잘못된 입력입니다")