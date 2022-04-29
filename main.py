import math
StartingPopulation = input("What is the starting population?: ")
StartingPopulation = int(StartingPopulation)
Year = input("How often will the population increase?: ")
Year = int(Year)
Year2 = Year
HowManyYears = input("How many years do you want to simulate?: ")
Year = int(HowManyYears)/Year
Year = math.floor(Year)
PopulationMultiplier = input("How much will the population increase each " + str(Year2) + " year(s)?: ")
PopulationMultiplier = float(PopulationMultiplier)
Population = StartingPopulation
while Year > 0:
    Population = Population*PopulationMultiplier
    print(Population)
    Year -= 1
print("In " + str(HowManyYears) + " years, a population of " + str(StartingPopulation) + " entities grew to a population of " + str(Population) + " entities.")
