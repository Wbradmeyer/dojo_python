from pet import Pet
from ninja import Ninja

pet_sprinkles = Pet('Sprinkles', 'dog', ['play dead', 'roll over'], 10, 10, 'Arf arf')
ninja_frank = Ninja('Frank', 'Cando', pet_sprinkles, 'dog biscuits', 'Alpo')

ninja_frank.walk().feed().bathe()
pet_sprinkles.sleep()