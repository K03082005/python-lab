# Given list of bases
bases = [2, 3, 4, 5]

powers = list(map(lambda base, index: base ** index, bases, range(len(bases))))


print(powers)
