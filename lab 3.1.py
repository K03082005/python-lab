def is_disarium(n):
    # Convert the number to a string to easily access each digit
    num_str = str(n)
    # Initialize sum of powered digits
    sum_of_digits = 0
    # Loop through each digit with its position
    for i, digit in enumerate(num_str):
        # Convert the digit back to an integer and raise it to the power of its position +1
        sum_of_digits += int(digit) ** (i + 1)
    # Check if the sum of powered digits equals the original number
    return sum_of_digits == n

# Example usage
number = 89
if is_disarium(number):
    print(f"{number} is a Disarium number")
else:
    print(f"{number} is not a Disarium number")
