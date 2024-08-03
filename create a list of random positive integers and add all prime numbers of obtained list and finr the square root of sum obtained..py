#create a list of random positive integers and add all prime numbers of obtained list and finr the square root of sum obtained.
import random
import math

# Generate a list of random positive numbers
numbers_list = []
sum_of_primes = 0
n = int(input("Enter length of list (n > 10): "))
if n <= 10:
    print("The length of the list must be greater than 10.")
else:
    for _ in range(n):
        elem = random.randint(1, 100)
        numbers_list.append(elem)

    print("Generated list:", numbers_list)

    # Calculate the sum of prime numbers in the list
    for y in numbers_list:
        if y > 1:  # Primes are greater than 1
            is_prime = True
            for i in range(2, int(y**0.5) + 1):
                if y % i == 0:
                    is_prime = False
                    break
            if is_prime:
                sum_of_primes += y

    print("Sum of prime numbers:", sum_of_primes)

    # Calculate and print the square root of the sum of prime numbers
    if sum_of_primes > 0:
        square_root = math.sqrt(sum_of_primes)
        print("Square root of the sum of prime numbers:", square_root)
    else:
        print("No prime numbers found in the list.")
