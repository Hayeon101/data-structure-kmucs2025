def iFact(n):
    print("iFact(%d) called..." % n)
    result = 1
    
    for i in range(1,n+1):
        result *= i
        
    return result
    
def rFact(n):
    print("rFact(%d) called..." % n)
    if n == 1:
        return 1  # base case
    else:
        return n * rFact(n-1)

print("iFact(5) = %d\n" % (iFact(5)))
print("rFact(5) = %d" % (rFact(5)))