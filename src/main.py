from countries_gen import CountriesGen
from persons_gen import PersonGen

# Countries generation

def countries_generator():
    instances = [CountriesGen() for _ in range(50)]

    countries_dict = {}

    for i, instance in enumerate(instances):
        countries_dict[f"country_{i + 1}"] = instance
        
    return countries_dict


# People generatiom

def people_generator(countries_generator):
    global_inhabitants = {}
    for item in countries_generator.items():
        i = 1
        for _ in range(item[1].population):
            global_inhabitants[f"{item[0]}_{i}"] = PersonGen(item)
            i += 1
            
    return global_inhabitants
      
        
if __name__ == "__main__":
    countries = countries_generator()
    global_inhabitants = people_generator(countries)
    global_inhabitants["country_12_54"].nationality.append("country_45")
    print(global_inhabitants["country_12_54"].nationality)
