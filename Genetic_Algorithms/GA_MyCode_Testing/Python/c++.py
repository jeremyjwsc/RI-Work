import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import time

xdata = []
ydata = []
plt.show()
axes = plt.gca()
axes.set_xlim(0, 1000)
axes.set_ylim(0, 40)
line, = axes.plot(xdata, ydata, 'r-')

csv_x_index = 0

def draw_plot(data):
    xdata.append(len(xdata))
    ydata.append(data)
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.xlabel("generation")
    plt.ylabel("cost value")
    plt.title("cost per each generation")
    plt.draw()

    # write to csv file
    with open("graph.csv", "a") as graph:
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
        self.boardlength = 8
        self.chromosome_matrix = np.zeros((30, 1000))
        self.cost_matrix = np.zeros(1000)
        self.crossovermatrix = np.zeros((30, 1000))
        self.area = np.zeros((30, 30))

    def clear(self):
        self.area = np.zeros((30, 30))

    def cost_func(self, idx):
        cost_value = 0
        for i in range(8):
            j = int(self.chromosome_matrix[i][idx])
            m = i + 1
            n = j - 1
            while m < 8 and n >= 0:
                if int(self.area[m][n]) == 1:
                    cost_value += 1  # there is a queen that takes the other one
                m += 1
                n -= 1

            m = i + 1
            n = j + 1
            while m < 8 and n < 8:
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
            while m >= 0 and n < 8:
                if int(self.area[m][n]) == 1:
                    cost_value += 1
                m -= 1
                n += 1

        return cost_value

    def initial_population(self):
        global check
        check = False
        for index in range(self.population):
            a = 0
            while a < 8:
                rand = random.randrange(32768)
                check = 1
                for b in range(a):
                    if rand % 8 == int(self.chromosome_matrix[b][index]):
                        check = 0
                    if check:
                        self.chromosome_matrix[a][index] = rand % 8
                    else:
                        a -= 1
                a += 1

    def population_sort(self):
        k = 1
        while k:
            k = 0
            for i in range(self.population-1):
                if int(self.cost_matrix[i]) > int(self.cost_matrix[i+1]):
                    temp = int(self.cost_matrix[i])
                    self.cost_matrix[i] = int(self.cost_matrix[i+1])
                    self.cost_matrix[i+1] = temp

                    for j in range(8):
                        temp = int(self.chromosome_matrix[j][i])
                        self.chromosome_matrix[j][i] = int(self.chromosome_matrix[j][i+1])
                        self.chromosome_matrix[j][i+1] = temp

                    k = 1

    def mating(self):
        temp_matrix = np.zeros((30, 2))
        temp_matrix0 = np.zeros(30)
        temp_matrix1 = np.zeros(30)

        for index in range(self.population//4):
            for t in range(2):
                for i in range(8):
                    temp_matrix0[i] = int(self.chromosome_matrix[i][2 * index])
                    temp_matrix1[i] = int(self.chromosome_matrix[i][2 * index + 1])

                for i in range(8):
                    if int(self.crossovermatrix[i][2*index+t]) == 0:
                        for j in range(8):
                            if int(temp_matrix0[j]) != 100:
                                temp_matrix[i][t] = temp_matrix0[j]
                                temp = temp_matrix0[j]
                                temp_matrix0[j] = 100

                                for k in range(8):
                                    if int(temp_matrix1[k]) == temp:
                                        temp_matrix1[k] = 100
                                        break
                                break
                    else:
                        for j in range(8):
                            if int(temp_matrix1[j]) != 100:
                                temp_matrix[i][t] = temp_matrix1[j]
                                temp = temp_matrix1[j]
                                temp_matrix1[j] = 100

                                for k in range(8):
                                    if int(temp_matrix0[k]) == int(temp):
                                        temp_matrix0[k] = 100
                                        break
                                break

                for i in range(8):
                    self.chromosome_matrix[i][2*index+self.population//2+t] = temp_matrix[i][t]

    def generate_crossovermatrix(self):
        for index in range(self.population):
            for a in range(8):
                self.crossovermatrix[a][index] = random.randrange(32768) % 2

    def apply_mutation(self):
        number_mutation = int(self.mutation*(self.population-1)*8)
        global rand_chromesome
        for k in range(number_mutation+1):
            rand_chromesome = 0
            while True:
                rand_chromesome = int(random.randrange(32768) % self.population)
                if rand_chromesome != 0:
                    break
            rand_gen0 = random.randrange(32768) % 8
            while True:
                rand_gen1 = random.randrange(32768) % 8
                if rand_gen1 != rand_gen0:
                    break

            temp = self.chromosome_matrix[rand_gen0][rand_chromesome]
            self.chromosome_matrix[rand_gen0][rand_chromesome] = self.chromosome_matrix[rand_gen1][rand_chromesome]
            self.chromosome_matrix[rand_gen0][rand_chromesome] = temp

    def fill_area(self, index):
        self.clear()
        for i in range(8):
            self.area[i][int(self.chromosome_matrix[i][index])] = 1


def main():
    global mutation

    if len(sys.argv) < 4:
        print("Usage: {} <population> <iteration> <mutation_rate>".format(sys.argv[0]))

        population = 100
        iteration = 10
        mutation = 0.5
    else:
        population = sys.argv[1]
        iteration = sys.argv[2]
        mutation = sys.argv[3]

    sample = GAQueen(population=population, iteration=iteration, mutation=mutation)

    sample.initial_population()

    g = 0
    num = 0

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

    res = '_'.join(str(int(sample.chromosome_matrix[i][0])) for i in range(8))
    print("result: {}".format(res))

    with open("final.csv", "w") as result:
        result.write(res)
        result.close()
    print("finished.")
    plt.show()


if __name__ == '__main__':
    main()

