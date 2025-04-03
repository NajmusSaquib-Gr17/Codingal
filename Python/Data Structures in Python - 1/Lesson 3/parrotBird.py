class Parrot:
    species = 'bird'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
parrot1 = Parrot('Mithu', 3)
parrot2 = Parrot('Moni', 4)

print(f'Mithu is of {parrot1.species} species')
print('{} is {} years old and from {} species'.format(parrot2.name, parrot2.age, parrot2.species))