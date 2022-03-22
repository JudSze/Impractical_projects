import random
import statistics

class Population(object):
    def __init__(self, id, num_rats, min_wt, max_wt, mode_wt, mutate_odds, mutate_min, mutate_max, litter_size, litter_per_year, generation_limit):
        self.id = id
        self.num_rats = num_rats
        self.min_wt = min_wt
        self.max_wt = max_wt
        self.mode_wt = mode_wt
        self.mutate_odds = mutate_odds
        self.mutate_min = mutate_min
        self.mutate_max = mutate_max
        self.litter_size = litter_size
        self.litter_per_year = litter_per_year
        self.generation_limit = generation_limit
        
        #ensure even number for breeding pairs
        if num_rats % 2 != 0:
            num_rats += 1
        
    def populate(self):
        return [int(random.triangular(self.min_wt, self.max_wt, self.mode_wt))\
            for i in range(self.num_rats)]
        
    def select(self, population, to_retain):
        """Choose a population to retain a specified number of members"""
        sorted_population = sorted(population)
        to_retain_by_sex = to_retain//2
        member_per_sex = len(sorted_population)
        
        females = sorted_population[:member_per_sex]
        males = sorted_population[:member_per_sex]
        selected_females = females[-to_retain_by_sex:]
        selected_males = males[-to_retain_by_sex:] 
        
        return selected_females, selected_males

    def fitness(self, population, goal):
        """Measure population fitness"""
        ave=statistics.mean(population)
        return ave / goal
    
        
class NewPopulation(Population):
    def breed(self, males, females, litter_size):
        """Breeding a new generation"""
        random.shuffle(males)
        random.shuffle(females)
        
        children = []
        
        for male, female in zip(males, females):
            for child in range(litter_size):
                child=random.randint(female, male)
                children.append(child)
        return children
    
    def mutate(self, children, mutate_odds, mutate_min, mutate_max):
        """Randomly alter  rat mutation"""
        for index, rat in enumerate(children):
            if mutate_odds >= random.random():
                children[index] = round(rat * random.uniform(mutate_min, mutate_max))
       
i52 = Population("i52", 501, 23, 53, 44, 55, 55, 55, 55, 55, 55)
pop = i52.populate()
print(i52.select(pop, 23))
print(i52.fitness(pop, 100))
        
a75 = NewPopulation("a75", 14, 2, 5, 4, 33, 44, 23, 78, 92, 100)
pop_a75 = a75.populate()
print(a75.breed(pop, pop_a75, 14))        
        

print(Population.fitness.__doc__)
    
        