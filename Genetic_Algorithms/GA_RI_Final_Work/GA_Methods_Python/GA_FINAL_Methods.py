import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import time
import math

"""
Ad-hoc suposition: Since queens can't collide between rows and columns, we can reinterpret the queen positions on board 
as an array, where index of the array is the board row and the values are the column positions.
Then, we only need to obtain the correct arrangements (solutions of N queens)
"""

start_time0 = time.time() # Init global time counter
N = 8  # Number of queens

class GAQueen:
    def __init__(self, population, iteration):
        self.population = population
        self.iteration = iteration
        self.boards = np.zeros((population, N))
        self.childBoards = np.zeros((population, N))
        self.fitness = np.empty(population)
        self.fitness.fill(-N * (N - 1) / 2)# Maximum number of collisions


    def initParent(self, a):
        """
            Assign range(N) elements randomly ordered to parent and child a
            :param i: Index of parent
        """

        numbers=list(range(N)) #Generate N numbers from 0 to N-1 (the N values for N positions)
        random.shuffle(numbers) #Reorder numbers list randomly
        self.boards[a,:]=numbers #Assign to board
        self.childBoards[a, :] = numbers #Assign to children

    def assessFitness(self, a):
        """
            Check the number of collisions between queens. We only have to check diagonal collisions
            since queens are in different rows and columns every time. Less collisions means best
            fitness, with maximum fitness of 0
            :param a: Index of parent
        """

        collisions=0 #Reset collisions
        board= self.boards[a,:] # Get board parent

        # check diagonal collisions
        for i in range(N):
            for j in range(N):
                if(i!=j):
                    deltaRow= abs(i - j)
                    deltaCol= abs(board[i]-board[j])
                    if deltaRow == deltaCol: collisions+=1

        self.fitness[a]=collisions*(-1)

    def selectWithReplacement(self,method):
        """
            Returns Parent in population according to the chosen method
            :param method: Method selected
            :return: Index of parent selected
        """

        if method == 'fitness-proportionate':
            fitness = self.fitness.copy()
            n = random.randrange(0, self.population)
            best=-1
            for i in range (1,self.population):
                fitness[i]=self.fitness[i]+self.fitness[i-1] #CDF of fitnesses. Fitness[population] = the sum of fitnesses
                if fitness[i-1] < n <= fitness[i]:
                    best=i
            if best==-1 : best=self.population-1 #If best was not modified, it will be last index

        elif method == 'tournament':
            t=2 #Tournament size, most popular size is 2
            best = random.randrange(0, self.population)
            for j in range (1,t):
                next = random.randrange(0, self.population)
                if self.fitness[next] >  self.fitness[best]:
                    best = next

        else:  # default: Complete random selection, no selection by fitness
            best = random.randrange(0, self.population)

        return best

    def crossover(self,method,a,b):
        """
            Crossover two parents of boards population and update childBoards according to the chosen method
            Index of childBoards = index of boards (parent)
            :param method: Method selected
            :param a: Index of first parent
            :param b: Index of second parent
        """

        self.childBoards[a] = self.boards[a] # Copy parent to child
        self.childBoards[b] = self.boards[b] # Copy parent to child

        if method == 'position-based':
            #Note order-based is the inverse of position-based, and it's done also in this method to get the other child

            for z in range(0, 2): # For the two children
                fixedValues = random.sample(list(range(N)), int(N / 2))  # Fixed values
                nonFixedList = list()  # Init "long" substring (in case N uneven) from parent2
                for j in range(0, N):
                    if self.boards[b][j] not in fixedValues:
                        nonFixedList.append(self.boards[b][j])  # Get non fixed elements from parent2
                for j in range(0, N):
                    if self.childBoards[a][j] not in fixedValues:
                        self.childBoards[a][j] = nonFixedList.pop(0)  # Get non fixed elements from parent2
                b, a = a, b  # Swap index to generate the other child

        else:  # default: order
            for z in range (0, 2):

                start = random.randrange(0, math.ceil(N / 2))  # start of fixed substring (index included)
                end = start + int(N / 2)  # End of fixed substring (index not included)

                nonFixedList = list()  # Init "long" substring (in case N uneven) from parent2
                for j in range(0, N):
                    # If element in b is not in fixed substring [from start through end-1, where maximun end is equal to N]
                    if self.boards[b][j] not in self.boards[a][start:end]:
                        nonFixedList.append(self.boards[b][j])  # Get non fixed elements from parent2

                # Assign non fixed elements to childBoards "holes"
                for i in range(0, start): self.childBoards[a][i] = nonFixedList.pop(0)
                for i in range(end, N): self.childBoards[a][i] = nonFixedList.pop(0)
                b, a = a, b #Swap index to generate the other child

    def mutate(self,method,a):
        """
            Mutate a childBoards according to the chosen method
            :param method: Method selected
            :param a: Index of a childBoards
        """
        if method == 'inversion':
            start = random.randrange(0, math.ceil(N / 2))  # start of fixed substring (index included)
            end = start + int(N / 2)  # End of fixed substring (index not included)
            substringReversed = self.childBoards[a][start:end][::-1].copy()
            j = 0
            for i in range(start, end):
                self.childBoards[a][i] = substringReversed[j]
                j += 1

        elif method == 'insertion':
            pos = random.sample(list(range(N)), 2)
            ind = self.childBoards[a][pos[1]]
            aux = np.delete(self.childBoards[a], pos[1])
            self.childBoards[a] = np.insert(aux, pos[0], ind)

        else:  # default: exchange
            pos=random.sample(list(range(N)), 2) #Select two random positions
            self.childBoards[a][pos[1]], self.childBoards[a][pos[0]] = \
                self.childBoards[a][pos[0]], self.childBoards[a][pos[1]] #Swap positions

def main():

    if len(sys.argv) < 3:
        print("Usage: {} <population> <iteration> <mutation_rate>".format(sys.argv[0]))
        population = 10
        iterations = 10000 #Maximum number of iterations
        executions = 500 #Program executions to make average later
    else:
        population = sys.argv[1]
        iterations = sys.argv[2]
        executions = sys.argv[3]

    generationList=list()
    times=list()
    sample = GAQueen(population=population, iteration=iterations)

    selectionMethod = "tournament"
    crossoverMethod = "position-based"
    mutationMethod = "exchange"

    for iter in range(executions):

        start_time = time.time() #Reset counter time
        for parent in range(population):
            sample.initParent(parent) #Init populations
        best=-N*(N-1)/2 # Maximum number of collisions

        p = 0 #Parent with best fitness, init.
        generation=0 #Count of iterations, init
        bestFromIteration=list() #Accumulate lists of best fitness for iteration, used for analysis purposes

        #Genetic algorithm main loop:
        while (best < 0) and generation<iterations : #best=0 means 0 collisions

            for i in range(int(population/2)): #Methods loop
                parentIndex1=sample.selectWithReplacement(selectionMethod)
                parentIndex2=sample.selectWithReplacement(selectionMethod)
                sample.crossover(crossoverMethod, parentIndex1, parentIndex2)
                sample.mutate(mutationMethod, parentIndex1)
                sample.mutate(mutationMethod, parentIndex2)

            sample.boards = sample.childBoards.copy()
            partialbests = -N * (N - 1) / 2 #Reset best fitness for this iteration

            for parent in range(population): #Fitness update loop
                sample.assessFitness(parent) #Calculate parent fitness

                if sample.fitness[parent] > partialbests:
                    partialbests=sample.fitness[parent] #Update best fitness for this iteration

                if sample.fitness[parent] > best:
                    best=sample.fitness[parent] #Update best total fitness
                    p = sample.boards[parent]

            bestFromIteration.append(partialbests)
            generation += 1

        generationList.append(generation) #Accumulate generation list for executions
        times.append(time.time() - start_time) #Accumulate time list for executions

    #Calculate average
    timeav=sum(times)/(float(len(times)))
    iterav = sum(generationList) / (float(len(times)))

    #Print stats
    print(timeav)
    print(iterav)
    print("Execution time: %s seconds" % (time.time() - start_time0)) #Total execution time
    print("\nPopulation:", population, " individuals")
    print("\nParent with best fitness:", p)
    generations=list(range(0,generation))
    plt.plot(generations, bestFromIteration) #Graphic of asymptotic convergence
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness for every iteration")
    plt.show()

if __name__ == '__main__':
    main()
