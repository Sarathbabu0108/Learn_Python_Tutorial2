'''def name(name, age):
     print("Hello")
     print(f"Hai {name} . Your age is {age}")


print("Start")
name("Syam", 30)
name(age=27, name="sarath")
print('Stop')'''

# Return statement


'''def square(number):
    print(number * number)

square(3)'''


'''def emogi_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = " "
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


message = input(">")

print(emogi_converter(message))'''

# Exception
try:
  age = int(input("Age : "))
  income = 20000
  risk = income / age
  print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value")





