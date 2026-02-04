def fibon(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


def fibosum(n):
    suma = 0
    for i in range(1, n + 1):
        suma += fibon(i)
    return suma


print("Sum of the first 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series:", fibosum(10))