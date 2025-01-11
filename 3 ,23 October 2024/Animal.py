class Animal:
    def speak(self):
        print('Издавать звуки')

class Dog(Animal):
    def speak(self):
        print('Гав-гав!')

class BigDog(Dog):
    def speak(self):
        print('вау-вау!')

class SmallDog(Dog):
    def speak(self):
        print('Тяв-тяв!')

class Toydog(SmallDog):
    def speak(self):
        print('Я игрушка , я как Мелстрой!')

class Robotdog(Toydog):
    def speak(self):
        print('Система включается')

class AngryBigDog(Dog):
    def speak(self):
        super().speak()
        print('Очень злой взгляд!!!! ')
        print('хмурится')

class Cat(Animal):
    def _meow(self):
        print('Мяу!')
    def speak(self):
        self._meow()

class ImboviyCat(Cat):
    def _meow(self):
        print('Мур................................')



animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

BigDog = BigDog()
BigDog.speak()

SmallDog = SmallDog()
SmallDog.speak()

Toydog = Toydog()
Toydog.speak()

Robotdog = Robotdog()
Robotdog.speak()

AngryBigDog = AngryBigDog()
AngryBigDog.speak()

cat = Cat()
cat.speak()

ImboviyCat = ImboviyCat()
ImboviyCat.speak()

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()

druzok = AngryBigDog
say_n_times(druzok, 3)

ImboviyCat = Cat()
say_n_times(ImboviyCat, 5)

list_of_animals = [Cat(), Dog(), ImboviyCat, AngryBigDog]

for animal in list_of_animals:
    animal.speak()
    print('--------------------------------')


