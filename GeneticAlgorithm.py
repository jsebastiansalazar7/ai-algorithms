__author__ = 'Juan Sebastian Salazar Aguirre'

# Import the necessary packages
import math
import random

# Class to handle the InitialPopulation creation
def InitialPopulation(maxPopulation, numVars):

    # Create initial population
    population = []

    for i in range(maxPopulation):

        gen = []

        for j in range(numVars):

            if (random.random() > 0.5):

                gen.append(1)

            else:

                gen.append(0)

        population.append(gen[:])

    return population

# Class to calcule the adaptation of the gen for the 3 SAT solution
def Adaptation (gen, solution):

    # Count correct clauses
    n = 3
    count = 0
    okClause = True

    for i in range(len(gen)):

        n = n - 1

        if (gen[i] != solution[i]):

            okClause = False

        if n == 0:

            if okClause:

                count = count + 1

            n = 3

            okClause = True

    if n > 0:

        if okClause:

            count = count + 1

    return count

# Class to test the adaptation of all the population
def TestPopulation (population, solution):

    # Test all the gens of the population
    adaptation = []

    for i in range(len(population)):

        adaptation.append(Adaptation(population[i], solution))

    return adaptation

# Class to handle the selection of 2 genes for crossing and mutation
def Selection(population, solution):

    adaptation = TestPopulation(population, solution)

    # Sum the punctuations
    total = 0

    for i in range(len(adaptation)):

        total = total + adaptation[i]

    # Select two random elements
    val1 = random.randint(0, total)
    val2 = random.randint(0, total)

    sumSelection = 0

    for i in range(len(adaptation)):

        sumSelection = sumSelection + adaptation[i]

        if (sumSelection >= val1):

            gen1 = population[i]
            break

    sumSelection = 0

    for i in range(len(adaptation)):

        sumSelection = sumSelection + adaptation[i]

        if (sumSelection >= val2):

            gen2 = population[i]
            break

    return gen1, gen2

# Class to handle gen crossing.  Use 2 genes to generate 2 descendants
def Cross(gen1, gen2):

    # Creation of 2 new genes
    newGen1 = []
    newGen2 = []

    # Define a random value to make the crossing
    cut = random.randint(0, len(gen1))

    # Fill the new genes
    newGen1[0: cut] = gen1[0: cut]
    newGen1[cut: ] = gen2[cut: ]
    newGen2[0: cut] = gen2[0: cut]
    newGen2[cut: ] = gen1[cut: ]

    return newGen1, newGen2

# Class to handle gen mutation using a probability
def Mutation(probability, gen):

	if random.random < probability:

		chromosome = random.randint(0, len(gen))

		if gen[chromosome] == 0:

			gen[chromosome] = 1

		else:

			gen[chromosome] = 0

	return gen

# Class to handle worst genes elimination
def Annihilation(population, solution):

	# Evaluate the population
	adaptation = TestPopulation(population, solution)

	# Get the worst adapted gen and eliminate it
	i = adaptation.index(min(adaptation))
	del population[i]
	del adaptation[i]

	# Get the second worst adapted gen and eliminate it
	i = adaptation.index(min(adaptation))
	del population[i]
	del adaptation[i]

# Class to get the best adapted gen
def BestGen(population, solution):

	adaptation = TestPopulation(population, solution)
	return population[adaptation.index(max(adaptation))]

# Class to handle the genetic algorithm
def GeneticAlgorithm():

	# Define important values
	maxIter = 10
	maxPopulation = 50
	numVars = 10
	end = False
	solution = InitialPopulation(1, numVars)[0]
	population = InitialPopulation(maxPopulation, numVars)
	probability = 0.1
	iterations = 0

	while not end:

		iterations = iterations + 1

		for i in range((len(population))/2):

			gen1, gen2 = Selection(population, solution)
			newGen1, newGen2 = Cross(gen1, gen2)
			newGen1 = Mutation(probability, newGen1)
			newGen2 = Mutation(probability, newGen2)
			population.append(newGen1)
			population.append(newGen2)
			Annihilation(population, solution)

		if (maxIter < iterations):

			end = True

	print "Solution: " + str(solution)
	best = BestGen(population, solution)

	return best, Adaptation(best, solution)

if __name__ == "__main__":

	random.seed()
	bestGen = GeneticAlgorithm()
	print "Best gen found: " + str(bestGen[0])
	print "Adaptation function: " + str(bestGen[1])


















