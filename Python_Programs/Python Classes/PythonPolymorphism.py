class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

choice = input("Enter animal (dog/cat): ").lower()
animal = Dog() if choice == "dog" else Cat()
print(animal.sound())
