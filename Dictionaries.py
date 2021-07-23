# Dictionaries are key value pairs
'''customer = {
    "name": "sarath babu",
    "age": 27,
    "is_verified": True
    }
customer["date_of_birth"] = "30 march 1994"
print(customer["date_of_birth"])'''

'''number = input("Phone : ")
dict = { "1": "One",
         "2": "Two",
         "3": "Three",
         "4": "Four",
         "5": "Five",
         "6": "Six",
         "7": "Seven",
         "8": "Eight",
         "9": "Nine",
         "0": "Zero"
         }
output = ""
for ch in number:
    output = output + dict.get(ch, " ") + " "
print(output)'''

# Emoji converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒"
     }
output = " "
for word in words:
    output = output + emojis.get(word, word)
print(output)









