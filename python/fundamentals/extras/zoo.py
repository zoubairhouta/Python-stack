class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=80, happiness=90)
        self.roar_power = 5

    def display_info(self):
        super().display_info()
        print(f"Roar Power: {self.roar_power}")


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)
        self.stripe_count = 50

    def display_info(self):
        super().display_info()
        print(f"Stripe Count: {self.stripe_count}")


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=70, happiness=70)
        self.honey_pots = 3

    def display_info(self):
        super().display_info()
        print(f"Honey Pots: {self.honey_pots}")


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


# Create the zoo and animals
zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala", 5))
zoo1.add_animal(Lion("Simba", 3))
zoo1.add_animal(Tiger("Rajah", 4))
zoo1.add_animal(Tiger("Shere Khan", 6))
zoo1.add_animal(Bear("Baloo", 8))

# Test the zoo by printing all animal info
zoo1.print_all_info()