from countries_gen import countries_generator
from persons_gen import PersonGen

countries = countries_generator()

world_inhabitants = []

for item in countries.items():
    for _ in range(item[1].population):
        world_inhabitants.append(PersonGen(item))

        
        
