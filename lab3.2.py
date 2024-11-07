def is_harshad(n):
    # Convert the number to a string to easily access each digit
    num_str = str(n)
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in num_str)
    # Check if the number is divisible by the sum of its digits
    return n % sum_of_digits == 0

# Example usage
number = 18
if is_harshad(number):
    print(f"{number} is a Harshad number")
else:
    print(f"{number} is not a Harshad number")
