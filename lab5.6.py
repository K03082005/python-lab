# Given sequence
sequence = "HelloWorld"


def process_characters(char):
    return (char.upper(), char.lower())


processed_characters = set(map(process_characters, sequence))


print(processed_characters)
