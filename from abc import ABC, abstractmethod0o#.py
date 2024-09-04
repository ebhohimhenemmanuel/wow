# AnimalInfo.py

class Cat:
    def display_info(self):
        return "This is a cat from Country A."

    def sound(self):
        return "Meow"

    def favorite_food(self):
        return "Fish"


class Dog:
    def display_info(self):
        return "This is a dog from Country A."

    def sound(self):
        return "Bark"

    def favorite_food(self):
        return "Meat"


class CountryB_Cat:
    def display_info(self):
        return "This is a cat from Country B."

    def sound(self):
        return "Meow"

    def favorite_food(self):
        return "Chicken"


class CountryB_Dog:
    def display_info(self):
        return "This is a dog from Country B."

    def sound(self):
        return "Bark"

    def favorite_food(self):
        return "Bone"


def animal_info(animal):
    print(animal.display_info())
    print("Sound:", animal.sound())
    print("Favorite Food:", animal.favorite_food())


# Example usage
country_a_cat = Cat()
country_a_dog = Dog()
country_b_cat = CountryB_Cat()
country_b_dog = CountryB_Dog()

animal_info(country_a_cat)
animal_info(country_a_dog)
animal_info(country_b_cat)
animal_info(country_b_dog)
