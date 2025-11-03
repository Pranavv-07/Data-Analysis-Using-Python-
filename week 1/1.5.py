# 1.5) Calculate the nth Fibonacci number using a function
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))
print("The", n, "th Fibonacci number is:", fibonacci(n))