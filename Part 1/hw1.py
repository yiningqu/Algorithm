def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the digit sequences in the middle
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    ac = a * c
    bd = b * d
    abcd = (a+b)*(c+d)
    
    return ac*(10**(2*m)) + (abcd - ac - bd) * (10**m) + bd
    







x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(x,y))
