class Pet:
    def __init__(self, name, type, tricks, health, energy, pet_sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.pet_sound = pet_sound

    def sleep(self):
        self.energy += 25
        print(f'{self.name} is sleeping.')
        print(f'{self.name} Energy: {self.energy}.')
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'{self.name} Health: {self.health}.')
        print(f'{self.name} Energy: {self.energy}.')
        return self

    def play(self):
        self.health += 5
        print(f'{self.name} Health: {self.health}.')
        return self

    def noise(self):
        print(f'{self.name} says {self.pet_sound}!')
        return self
    
