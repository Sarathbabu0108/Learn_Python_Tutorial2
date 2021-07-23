'''course = 'Python for beginners'
print(len(course))
print(course.replace('beginners', 'everyone'))
print('Python' in course)'''

'''is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print('it is a cold day')
    print('wear warm clothes')
else:
    print('it is a lovely  day')

print('ENJOY YOUR DAY')'''

'''price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down Payment : ${down_payment}')'''


'''has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print("Not eligible for loan")'''

'''temperature = int(input("Enter the temperature :"))
if temperature > 30:
    print('It is a hot day')
elif temperature < 10:
    print("It's a cold day")
else:
    print("it's neither hot nor cold")'''

'''name = input("Enter a name : ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Names looks good")'''


weight = int(input("Weight : "))
unit = input('(L)bs or (K)g : ')

if unit.upper() == "L":
    converted = weight * .45
    print(f" You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")























































