from DataStructure.ArrayStack import ArrayStack

def order(op):
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    else: return 2

def infixToPostfix(expr):
    S = ArrayStack()
    postfix = []

    for term in expr:
        if term in '(':
            S.push('(')
        elif term in ')':
            while not S.isEmpty():
                op = S.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not S.isEmpty():
                op = S.peek()
                if (order(term) <= order(op)):
                    postfix.append(op)
                    S.pop()
                else: break
            S.push(term)
        else:
            postfix.append(term)

    while not S.isEmpty():
        postfix.append(S.pop())

    return postfix

if __name__ == "__main__":
    infix = input("수식을 입력하세요 : ")
    expr = infix.split()
    postfix = infixToPostfix(expr)

    print(postfix)