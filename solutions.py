#1 Multiples of 3 or 5

sum = 0                           # Counter

for i in range(1000):             # loop "for" to iterate over the range "1000"
    if i % 3 == 0 or i % 5 == 0:  # For each number "i" in the range, it checks if "i" is divisible by either 3 or 5 using the modulo operator (%).
        sum += i                  # If the number is divisible by either 3 or 5, it is added to the sum variable.

print(sum)                        # Result



#2 Even Fibonacci numbers

prev_number = 1                # previous number
curr_number = 2                # current number
sum = 0                        # counter

while curr_number <= 4000000:  # loop "while" to iterate over the numbers in the Fibonacci sequence

    if curr_number % 2 == 0:   # Check if the current number is even. The loop continues as long as the current number is less than or equal to four million.
        sum += curr_number

    next_number = prev_number + curr_number  # Finally, the code calculates the next number in the sequence by adding the previous number and the current number,
    prev_number = curr_number  # and then updates the values of prev_number and curr_number for the next iteration.
    curr_number = next_number

print(sum)                     # Result


#3 Largest prime factor

def largest_prime_divisor(n):   # The function starts by checking if the input number is already prime (less than 2).
                                # If it is, it returns the number.
    if n < 2:                   # Edge case: n is already prime
        return n

    if n % 2 == 0:              # Check for divisibility by 2
        largest_divisor = 2     # Next, the function checks if the number is divisible by 2.
        while n % 2 == 0:       # If it is, it sets the largest divisor to 2 and divides the number by 2 until it is no longer divisible by 2.
            n = n // 2          # If the number is not divisible by 2, the largest divisor is set to 1.
    else:
        largest_divisor = 1

    i = 3                       # Check for divisibility by add numbers
    while i <= n ** 0.5:        # The function then iterates through odd numbers until the square root of the number,
        if n % i == 0:          # checking if each one is a divisor of the number.
            largest_divisor = i # If it is, it sets the divisor as the largest divisor and divides the number by the divisor.
            n = n // i          # If it is not a divisor, the function moves on to the next odd number.
        else:
            i += 2

    if n > largest_divisor:     # At this point, n is prime, so it is the largest divisor
        largest_divisor = n     # If the number is still prime at this point (it has no other divisors), it is set as the largest divisor.
                                # The function then returns the largest divisor.
    return largest_divisor


print(largest_prime_divisor(600851475143))  # Result



#4 Largest palindrome product
def largest_palindrome_product(lower, upper):

    largest_palindrome = lower * upper                                 # Initialize the largest palindrome to the smallest possible palindrome

    for i in range(lower, upper + 1):                                  # Iterate through the range of numbers
        for j in range(i, upper + 1):

            product = i * j                                            # Calculate the product of i and j

            if str(product) == str(product)[
                               ::-1] and product > largest_palindrome: # Convert the product to a string and check if it is a palindrome

                largest_palindrome = product                           # If the product is a palindrome and larger than the current largest palindrome, set it as the new largest palindrome

    return largest_palindrome                                          # Return the largest palindrome


print(largest_palindrome_product(100, 999))                            # Result


#5 Smallest multiple

def smallest_multiple(n):
    smallest_multiple = 1                                                       # Initialize the smallest multiple to 1

    for i in range(1, n + 1):                                                   # Iterate through the range of numbers from 1 to n

        smallest_multiple = smallest_multiple * i // gcd(smallest_multiple, i)  # Calculate the least common multiple of the smallest multiple and i

    return smallest_multiple                                                    # Return the smallest multiple


def gcd(a, b):
    while b:                                                                    # Calculate the greatest common divisor of a and b using Euclid's algorithm
        a, b = b, a % b
    return a                                                                    # return result


print(smallest_multiple(20))                                                    # Result



#6 Sum square difference

sum_of_squares = sum(i ** 2 for i in range(1, 101))     # Calculate the sum of the squares of the first hundred natural numbers


square_of_sum = sum(range(1, 101)) ** 2                 # Calculate the square of the sum of the first hundred natural numbers


difference = square_of_sum - sum_of_squares             # Calculate the difference

print(difference)                                       # Result


#7 10001st prime

def is_prime(n):
    if n < 2:                             # Check if n is a prime number
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


counter = 0                               # Initialize the counter and the current number
num = 1

while counter < 10001:                    # Keep incrementing the number until the counter reaches 10,001
    num += 1
    if is_prime(num):
        counter += 1

print(num)                                # Result



#8 Largest product in a series

s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
adjacentLength = 13                              # The number of adjacent digits that we want to consider.
largestProduct = 0                               # The largest product of the adjacent digits that we find

for i in range(0, len(s) - adjacentLength + 1):  # A loop that iterates through the indices of the digits

  product = 1                                    # The product of the adjacent digits at the current index

  for j in range(i, i + adjacentLength):         # A loop that iterates through the indices of the adjacent digits that we want to consider
    product *= int(s[j: j + 1])                  # Multiplies the value of product by the integer value of the digit at index "j" in "s"

  if product > largestProduct:                   # Сhecks if the current value of product is greater than the value of largestProduct
    largestProduct = product                     # The condition in the previous line is true, this line updates the value of largestProduct to be equal to the current value of product

print (largestProduct)                           # Result


#9 Special Pythagorean triplet

def find_pythagorean_triplet(sum):
    for a in range(1, sum // 3):           # Iterate through all possible values of a

        for b in range(a + 1, sum // 2):   # Iterate through all possible values of b

            c = sum - a - b                # Calculate c

            if a ** 2 + b ** 2 == c ** 2:  # Check if a, b, and c form a Pythagorean triplet

                return a * b * c           # Return the product of a, b, and c


product = find_pythagorean_triplet(1000)   # Find the Pythagorean triplet for which a + b + c = 1000
print(product)                             # Result



#10 Summation of primes
def sum_of_primes(n):
    numbers = [x for x in range(2, n + 1)]                                 # Initialize a list of all numbers from 2 to n (inclusive)

    sum_of_primes = 0                                                      # Initialize the sum of the prime numbers to 0

    for i in range(len(numbers)):                                          # Iterate through the numbers

        if numbers[i] != -1:                                               # If the current number is prime, add it to the sum

            sum_of_primes += numbers[i]

            for j in range(2 * numbers[i] - 2, len(numbers), numbers[i]):  # Set all multiples of the current number to -1
                numbers[j] = -1

    return sum_of_primes                                                   # Return the sum of the prime numbers


result = sum_of_primes(2000000)                                            # Calculate the sum of all prime numbers less than 2 million
print(result)                                                              # Result