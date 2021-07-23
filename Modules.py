'''import converters

from converters import kg_to_lbs
print(kg_to_lbs(100))

print(converters.kg_to_lbs(70))'''


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number
    return max
