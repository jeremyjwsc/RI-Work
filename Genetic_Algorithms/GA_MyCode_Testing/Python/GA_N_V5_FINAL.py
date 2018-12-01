import numpy as np
import os
import sys
import random
import matplotlib.pyplot as plt
import time
import math

#import datetime
start_time = time.time()

"""
Ad-hoc suposition: Since queens can't collide between rows and columns, 
we can reinterpret the queen positions on board as an array, 
where index of the array is the board row and the values are the column positions.
Then, we only need to obtain the correct arrangements (solutions of N queens)
"""

N = 50 # for number of queens
xdata = []
ydata = []
#plt.show()
axes = plt.gca()
line, = axes.plot(xdata, ydata, 'r-')

csv_x_index = 0

if os.path.exists('time_evolution_Ngraph.csv'):
    os.remove('time_evolution_Ngraph.csv')

def draw_plot(data):
    if len(xdata) >= 1000:
        xdata.clear()
        ydata.clear()
    xdata.append(len(xdata))
    ydata.append(data)
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.xlabel("generation")
    plt.ylabel("cost value")
    plt.title("cost per each generation")
    plt.draw()

    # write to csv file
    with open("time_evolution_Ngraph.csv", "a") as graph:
        global csv_x_index
        graph.write("{},{}\n".format(csv_x_index+1, data))
        csv_x_index += 1
        graph.close()

    plt.pause(1e-17)


class GAQueen:
    def __init__(self, population, iteration, mutation):
        self.population = population
        self.iteration = iteration
        self.mutation = mutation
        self.boardlength = N
        self.chromosome_matrix = np.zeros((N, population))
        self.cost_matrix = np.zeros(population)
        self.crossovermatrix = np.zeros((N, population))
        self.area = np.zeros((N, N))
        self.solutions = 0
        #GA variables
        self.boards = np.zeros((population, N))
        self.childBoards = np.zeros((population, N))
        self.fitness = np.empty(population)
        self.fitness.fill(-N * (N - 1) / 2)# Maximum number of collisions

    def clear(self):
        self.area = np.zeros((N, N))

    def find_solution(self):
        positions = [-1] * self.boardlength
        self.put_queen(positions, 0)
        print("Number of total solutions: {}".format(self.solutions))
        print("Number of queens: {}".format(self.boardlength))

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.boardlength:
            # self.show_full_board(positions)
            self.show_short_board(positions)
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.boardlength):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or positions[i] - i == column - ocuppied_rows or positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def show_short_board(self, positions):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the corresponding row.
        """
        line = "_".join(str(positions[i]) for i in range(self.boardlength))

        #print(line)

        with open("final_Nsolution.csv", "a") as result:
            result.write(line + "\n")
            result.close()

    def cost_func(self, idx):
        cost_value = 0
        for i in range(self.boardlength):
            j = int(self.chromosome_matrix[i][idx])
            m = i + 1
            n = j - 1
            while m < self.boardlength and n >= 0:
                if int(self.area[m][n]) == 1:
                    cost_value += 1  # there is a queen that takes the other one
                m += 1
                n -= 1

            m = i + 1
            n = j + 1
            while m < self.boardlength and n < self.boardlength:
                if int(self.area[m][n]) == 1:
                    cost_value += 1
                m += 1
                n += 1

            m = i - 1
            n = j - 1
            while m >= 0 and n >= 0:
                if int(self.area[m][n]) == 1:
                    cost_value += 1
                m -= 1
                n -= 1

            m = i - 1
            n = j + 1
            while m >= 0 and n < self.boardlength:
                if int(self.area[m][n]) == 1:
                    cost_value += 1
                m -= 1
                n += 1

        return cost_value

    def population_sort(self):
        k = 1
        while k:
            k = 0
            for i in range(self.population-1):
                if int(self.cost_matrix[i]) > int(self.cost_matrix[i+1]):
                    temp = int(self.cost_matrix[i])
                    self.cost_matrix[i] = int(self.cost_matrix[i+1])
                    self.cost_matrix[i+1] = temp

                    for j in range(self.boardlength):
                        temp = int(self.chromosome_matrix[j][i])
                        self.chromosome_matrix[j][i] = int(self.chromosome_matrix[j][i+1])
                        self.chromosome_matrix[j][i+1] = temp

                    k = 1

    def mating(self):
        temp_matrix = np.zeros((self.boardlength, 2))
        temp_matrix0 = np.zeros(self.boardlength)
        temp_matrix1 = np.zeros(self.boardlength)

        for index in range(self.population//4):
            for t in range(2):
                for i in range(self.boardlength):
                    temp_matrix0[i] = int(self.chromosome_matrix[i][2 * index])
                    temp_matrix1[i] = int(self.chromosome_matrix[i][2 * index + 1])

                for i in range(self.boardlength):
                    if int(self.crossovermatrix[i][2*index+t]) == 0:
                        for j in range(self.boardlength):
                            if int(temp_matrix0[j]) != 100:
                                temp_matrix[i][t] = temp_matrix0[j]
                                temp = temp_matrix0[j]
                                temp_matrix0[j] = 100

                                for k in range(self.boardlength):
                                    if int(temp_matrix1[k]) == temp:
                                        temp_matrix1[k] = 100
                                        break
                                break
                    else:
                        for j in range(self.boardlength):
                            if int(temp_matrix1[j]) != 100:
                                temp_matrix[i][t] = temp_matrix1[j]
                                temp = temp_matrix1[j]
                                temp_matrix1[j] = 100

                                for k in range(self.boardlength):
                                    if int(temp_matrix0[k]) == int(temp):
                                        temp_matrix0[k] = 100
                                        break
                                break

                for i in range(self.boardlength):
                    self.chromosome_matrix[i][2*index+self.population//2+t] = temp_matrix[i][t]

    def generate_crossovermatrix(self):
        for index in range(self.population):
            for a in range(self.boardlength):
                self.crossovermatrix[a][index] = random.randrange(32768) % 2

    def apply_mutation(self):
        number_mutation = int(self.mutation*(self.population-1)*self.boardlength)
        global rand_chromesome
        for k in range(number_mutation+1):
            rand_chromesome = 0
            while True:
                rand_chromesome = int(random.randrange(32768) % self.population)
                if rand_chromesome != 0:
                    break
            rand_gen0 = random.randrange(32768) % self.boardlength
            while True:
                rand_gen1 = random.randrange(32768) % self.boardlength
                if rand_gen1 != rand_gen0:
                    break

            temp = self.chromosome_matrix[rand_gen0][rand_chromesome]
            self.chromosome_matrix[rand_gen0][rand_chromesome] = self.chromosome_matrix[rand_gen1][rand_chromesome]
            self.chromosome_matrix[rand_gen0][rand_chromesome] = temp

    def fill_area(self, index):
        self.clear()
        for i in range(self.boardlength):
            self.area[i][int(self.chromosome_matrix[i][index])] = 1

    def initial_population(self):

        #Generate range(N) elements randomly ordered per M populations
        numbers=list(range(N)) #Generate N numbers from 0 to N-1
        for i in range(self.population):  # For every population
            random.shuffle(numbers) #Reorder numbers list randomly
            for j in range (self.boardlength):
                self.chromosome_matrix[j][i]=numbers[j]

    def initParent(self, a):
        """
            Assign range(N) elements randomly ordered to parent and child a
            :param i: Index of parent
        """

        numbers=list(range(N)) #Generate N numbers from 0 to N-1 (the N values for N positions)
        random.shuffle(numbers) #Reorder numbers list randomly
        self.boards[a,:]=numbers #Assign to board
        self.childBoards[a, :] = numbers

    def assessFitness(self, a):
        """
            Check the number of collisions between queens. Less collisions smeans best fitness,
            then: fitness=collisions*(-1), with maximum of 0
            :param a: Index of parent
        """

        collisions=0
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

        if method is 'fitness-proportionate':
            fitness = self.fitness.copy()
            n = random.randrange(0, self.population)
            best=-1
            for i in range (1,self.population):
                fitness[i]=self.fitness[i]+self.fitness[i-1] #CDF of fitnesses. Fitness[population] = the sum of fitnesses
                if fitness[i-1] < n <= fitness[i]:
                    best=i
            if best==-1 : best=self.population-1 #If best was not modified, it will be last index

        elif method is 'tournament':
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

        if method is 'position-based':
            #Note order-based is the inverse of position-based, and it's done also in this method to get the other child

            for z in range(0, 2):
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
        if method is 'inversion':
            start = random.randrange(0, math.ceil(N / 2))  # start of fixed substring (index included)
            end = start + int(N / 2)  # End of fixed substring (index not included)
            substringReversed = self.childBoards[a][start:end][::-1].copy()
            j = 0
            for i in range(start, end):
                self.childBoards[a][i] = substringReversed[j]
                j += 1

        elif method is 'insertion':
            pos = random.sample(list(range(N)), 2)
            ind = self.childBoards[a][pos[1]]
            aux = np.delete(self.childBoards[a], pos[1])
            self.childBoards[a] = np.insert(aux, pos[0], ind)

        else:  # default: exchange
            pos=random.sample(list(range(N)), 2) #Select two random positions
            self.childBoards[a][pos[1]], self.childBoards[a][pos[0]] = \
                self.childBoards[a][pos[0]], self.childBoards[a][pos[1]] #Swap positions

def main():
    global mutation

    if len(sys.argv) < 4:
        print("Usage: {} <population> <iteration> <mutation_rate>".format(sys.argv[0]))
        population = 20
        iterations = 1000 #Maximum number of iterations
        mutation = 0.5 # 1/N Often probability of mutation
    else:
        population = sys.argv[1]
        iterations = sys.argv[2]
        mutation = sys.argv[3]

    sample = GAQueen(population=population, iteration=iterations, mutation=mutation) #Create class


    selectionMethod="fitness-proportionate";
    crossoverMethod = "position-based";
    mutationMethod = "inversion";

    for parent in range(population):
        sample.initParent(parent) #Init populations
    best=-N*(N-1)/2 # Maximum number of collisions

    p=0
    generation=0

    bestFromIteration=list()
    while (best < 0) and generation<iterations : #best=0 means 0 collisions

        for i in range(int(population/2)):
            parentIndex1=sample.selectWithReplacement(selectionMethod)
            parentIndex2=sample.selectWithReplacement(selectionMethod)
            sample.crossover(crossoverMethod, parentIndex1, parentIndex2)
            sample.mutate(mutationMethod, parentIndex1)
            sample.mutate(mutationMethod, parentIndex2)

        sample.boards = sample.childBoards.copy()

        partialbests = -N * (N - 1) / 2
        for parent in range(population):
            sample.assessFitness(parent) #Calculate parent fitness

            if sample.fitness[parent] > partialbests:
                partialbests=sample.fitness[parent]

            if sample.fitness[parent] > best:
                best=sample.fitness[parent] #Update best fitness
                p=sample.boards[parent]
        bestFromIteration.append(partialbests)

        generation += 1

    #print("\n",p)
    print("\nBest fitness:", best)
    print("\nNumber of generations:", generation)
    print("\nPopulation:", population, " individuals")
    print("\nParent with best fitness:", p)
    generations=list(range(0,generation))
    print("Execution time: %s seconds" % (time.time() - start_time))
    plt.plot(generations, bestFromIteration) #Graphic of asymptotic convergence
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness for every iteration")
    plt.show()


    """
    axes.set_xlim(0, 1000)
    axes.set_ylim(0, 30)
    g = 0
    num = 0 
    sample.initial_population() #Init population class
    while g == 0 and num < sample.iteration:
        num += 1
        g = 0
        for k in range(sample.population):
            sample.fill_area(k)
            cost = sample.cost_func(k)
            sample.cost_matrix[k] = cost

            draw_plot(cost)

        sample.population_sort()

        if int(sample.cost_matrix[0]) == 0:
           g = 1

        sample.generate_crossovermatrix()
        sample.mating()
        sample.apply_mutation()

    res = '_'.join(str(int(sample.chromosome_matrix[i][0])) for i in range(N))
    print("Final result: {}".format(res))

    with open("final_Nsolution.csv", "w") as result:
        result.write("Final result: \n\t{}\n".format(res))
        result.write("\nAll solutions:\n")
        result.close()
    #plt.show()

    sample.find_solution()

    with open("final_Nsolution.csv", "a") as result:
        result.write("\n\tTotal: {} solutions\n".format(sample.solutions))
        result.write("\n\tTotal number of queens: {}\n".format(N))
        result.write("\n\tDONE!!!\n")
        result.write("\n\tExecution time: %s seconds\n" % (time.time() - start_time))
        result.write("\n\tDate: {}". format(time.ctime()))
        result.close()
    print("DONE!!!")
    print("Execution time: %s seconds" % (time.time() - start_time))
    """

if __name__ == '__main__':
    main()
    
    #print("Execution time: %s seconds" % (time.time() - start_time))
    #print(time.ctime())



