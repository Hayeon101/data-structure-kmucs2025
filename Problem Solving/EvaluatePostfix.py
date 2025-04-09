from DataStructure.ArrayStack import ArrayStack

def evalPostfix(expr):
    S = ArrayStack()

    for term in expr:
        if term in '+-*/':
            val2 = S.pop()
            val1 = S.pop()

            if term == '+':
                S.push(val1 + val2)
            elif term == '-':
                S.push(val1 - val2)
            elif term == '*':
                S.push(val1 * val2)
            else:
                S.push(val1 / val2)
        else:
            S.push(float(term))

    return S.pop()

if __name__ == "__main__":
    str = '8 2 / 3 - 3 2 * +'
    expr = str.split()

    print(str, '--->', evalPostfix(expr))