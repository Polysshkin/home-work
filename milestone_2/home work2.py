number = int(input("Enter an integer: "))
sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number //= 10

print("The sum of the digits is:", sum_of_digits)

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i

    print(f"The factorial of {number} is: {factorial}")

    number = int(input("Enter a number: "))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

    terms = int(input("Enter the number of terms: "))


def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


fib_sequence = fibonacci(terms)
print("The Fibonacci sequence is:", ', '.join(map(str, fib_sequence)))
