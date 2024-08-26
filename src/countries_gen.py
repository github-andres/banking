import numpy as np

class CountriesGen:
     
    def create_countries():
     
        massive_countries = np.random.triangular(1400, 1500, 1600, size=2)
        extra_large_countries = np.random.triangular(200, 280, 340, size=5)
        large_countries = np.random.triangular(75, 90, 140, size=15)
        medium_countries = np.random.triangular(30, 40, 70, size=60)
        small_countries = np.random.triangular(5, 12, 25, size=22)
        tiny_countries = np.random.triangular(2, 3, 3.5, size=5)
        xx_small_countries = np.random.triangular(.25, .45, 1, size=14)
        
        countries = np.concatenate([massive_countries, extra_large_countries, large_countries, medium_countries, small_countries, tiny_countries, xx_small_countries]) * 100
        
        return countries
    
    def __init__(self):
        self.population = round(np.random.choice(CountriesGen.create_countries()))
        self.female_perc = (round(np.random.triangular(.48, .51, .55) * self.population))/self.population
        self.life_exp = np.random.triangular(69, 74, 84)
        self.avg_age = np.random.triangular(23, 28, 41)
        self.unemployment_rate = np.random.triangular(0.05, 0.08, 0.14)
        
        
def countries_generator():
    instances = [CountriesGen() for _ in range(50)]

    countries_dict = {}

    for i, instance in enumerate(instances):
        countries_dict[f"country_{i + 1}"] = instance
        
    return countries_dict
    
if __name__ == "__main__":
    pass

