def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_non_recursive(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

while True:
    n = int(input("\nEnter Fibonacci number (Enter -1 to exit): "))
    if n != -1:
        print("Recursive Fibonacci: ", fibonacci_recursive(n))
        print("Non-Recursive Fibonacci: ",fibonacci_non_recursive(n))
    else:
        break
