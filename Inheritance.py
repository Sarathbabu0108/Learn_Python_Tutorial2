# Inheritance
class Mammal:
    def walk(self):
        print("Walk")

    def jump(self):
        print("jump")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()