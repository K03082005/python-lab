# Define a function that triples a number
def triple(n):
    return n * 3


numbers = [1, 2, 3, 4, 5]


tripled_numbers = list(map(triple, numbers))

# Print the result
print(tripled_numbers)
