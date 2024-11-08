def is_armstrong(n):
    # Convert the number to a string to easily access each digit
    num_str = str(n)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum equals the original number
    return sum_of_powers == n

# Print all Armstrong numbers from 1 to 1000
for number in range(1, 1001):
    if is_armstrong(number):
        print(number)
