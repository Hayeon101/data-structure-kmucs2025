def printStep(A, idx):
    print(f'   Step {idx} : ', end='')
    print(A)

def insertionSort(A):
    n = len(A)

    for i in range(1,n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

        printStep(A,i)

if __name__ == '__main__':
    data = [5,3,8,4,9,1,6,2,7]

    L = list(data)
    print("Before    :",L)
    insertionSort(L)
    print("Insertion :", L)