# finding largest number in a list
'''list = [1, 4, 300, 200, 500]
max = list[0]
for num in list:
    if num > max:
        max = num
print(max)'''
# 2D list

'''matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]
for row in matrix:
    for item in row:
        print(item)'''
# List methods

'''numbers = [1, 4, 5, 6, 7, 5]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)'''

# Removing duplicates

numbers = [1, 2, 2, 4, 5, 4, 9, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)




