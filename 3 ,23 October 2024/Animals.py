

class Animal:
    def speak(self):
        pass
animal = Animal()
animal.speak()

class Dog(Animal):
    def speak(self):
        print('Гав-гав')
bobik = Dog()
bobik.speak()