def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"The fact of {num} is {fac(num)}")
print("i am vaishnavi")
print("hi")
