#5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    # - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    # нужно использовать методы get и set
class Pet:
    def __init__(self, name, owner):
        self.name=name
        self.__owner=owner

    def __str__(self):
        return f'My name is {self.name}'

    def owner(self):
        print(f'Now my owner is {self.__owner}')

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner=owner

    def change_owner(self,newname):
        print (f'You would like to change owner from {self.__owner} to {newname}?')
        self.set_owner(newname)
        print(f' My new owner is {self.get_owner()}')

    def sound(self):
        pass

    def action(self):
        pass

class Dog(Pet):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed
        self.__kind = "dog"

    def sound(self):
        return "I can bark!"

    def __str__(self):
        return f'My name is {self.name}. I am a {self.breed} {self.__kind}'

    def action(self):
        print("I like run!")

    def run(self):
        print("I can run fast and long!")


class Cat(Pet):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed
        self.__kind = "cat"

    def __str__(self):
        return f'My name is {self.name}. I am a {self.breed} {self.__kind}'

    def sound(self):
        return "I can mew!"

    def action(self):
        print ("I like to sleep!")

    def purr(self):
        print("I can purr if you pet me")

class Parrot(Pet):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed
        self.__kind = "parrot"

    def __str__(self):
        return f'My name is {self.name}. I am a {self.breed} {self.__kind}'

    def sound(self):
        return "I can talk!"

    def action(self):
        print("I can fly!")

    def fly(self):
        print ("I like to fly very high!")

def detector(pet):
    print(pet)
    pet.owner()
    print(pet.sound())
    pet.action()
    if isinstance(pet,Dog):
        pet.run()
    elif isinstance(pet,Cat):
        pet.purr()
    elif isinstance(pet, Parrot):
        pet.fly()
    else:
        print ("I am not sure what kind I am.")
pet1=Pet("Du", "Henry")
dog1=Dog("Bobik","Misha","golden retriver")
cat1=Cat("Barsik", "Lusya","domestic")
parrot1=Parrot("Kirusha","Petya","cokatoo")
detector(dog1)
detector(cat1)
detector(parrot1)
detector(pet1)
# checking properties of  attributes
print(pet1)
pet1.owner()
pet1.name="Lu"
print(pet1)
# pet1.owner="Bob"  # ! can't change this attribute
pet1.change_owner("Bob") # changing owner's name
print(dog1.__dict__)
