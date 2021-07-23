'''class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)
point2 = Point()
point2.x = 1
print(point2.x)'''

# constructors
'''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Draw")

    def move(self):
        print("Move")


point = Point(10, 100)
point.y = 11
print(point.y)'''


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


a = Person("Sarath Babu")
print(a.name)
a.talk()

syam = Person("Syam Babu")
syam.talk()

