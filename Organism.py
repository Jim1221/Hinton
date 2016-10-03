# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# import pylab as plot


class organ:
    def __init__(self, net_size):
        self.net = np.zeros(net_size)
        self.geno = []
        self.n_learn = 0.0  # counter for learning attempts
        self.prob = 0.0
        self.evolved = False
        rand = np.random.randint(1, 5, size=(20) )
        for i in range(net_size):
            if rand[i] == 3:
                self.net[i] = 1
                self.geno.append(False)  # to be learnt
            elif rand[i] == 4:
                self.net[i] = 0
                self.geno.append(False)  # to be learnt
            else:
                self.net[i] = np.random.randint(2)
                self.geno.append(True)  # Genotype

    def learn(self, attempts):
        if self.evolved == True:
            self.prob = 20.0
            return
        else:
            for i in range(attempts):
                for i in range(net_size):
                    if self.geno[i] is False:
                        #  we need to learn
                        self.net[i] = np.random.randint(2)
                self.n_learn = self.n_learn + 1
                self.prob = 1.0 + 19*(learn_span-self.n_learn)/learn_span
                if (self.net == good_net).all():
                    self.evolved = True
                    return


class result:
    def __init__(self, pop):
        self.correct = 0
        self.incorrect = 0
        self.undi = 0
        for org in pop:
            for i in range(len(org.net)):
                if org.geno[i]:
                    if org.net[i] == good_net[i]:
                        self.correct = self.correct + 1
                    else:
                        self.incorrect = self.incorrect + 1
                else:
                    self.undi = self.undi + 1
        self.correct = self.correct/(net_size*pop_size)
        self.incorrect = self.incorrect/(net_size*pop_size)
        self.undi = self.undi/(net_size*pop_size)


def reproduce(current, repro_times, net_len):
    probability = [obj.prob for obj in current]
    prob2 = [i/sum(probability) for i in probability]
    new_pop = []
    for i in range(repro_times):
        new_pop.append(organ(net_len))
        parents = np.random.choice(current, 2, p=prob2)  # chose parents
    #  choose gene split location
        split = np.random.randint(net_len)
        for j in range(net_len):
            if j <= split:
                new_pop[i].net[j] = parents[0].net[j]
                new_pop[i].geno[j] = parents[0].geno[j]
            else:
                new_pop[i].net[j] = parents[1].net[j]
                new_pop[i].geno[j] = parents[1].geno[j]
        if (new_pop[i].net == good_net).all():
            new_pop[i].evolved = True
    return new_pop


def goal(net_size):
    """"Generates the good net"""
    return np.random.randint(2, size=net_size)


net_size = 20
pop_size = 1000
reproductions = 1000
learn_span = 1000
generate = 30

current_pop = []


good_net = goal(net_size)

# Genertate the population
for l in range(pop_size):
    current_pop.append(organ(net_size))

# print the current frequency ratio

ans = []
ans.append(result(current_pop))

f = open("evo.dat", 'w')
for k in range(generate):
    print("Evolution: {}".format(k))
    for pop in current_pop:
        pop.learn(learn_span)
    nxt_gen = reproduce(current_pop, reproductions, net_size)
    current_pop = nxt_gen
    ans.append(result(current_pop))
    f.write(str(k) + " " +
            str(ans[k].correct) + " " +
            str(ans[k].incorrect) + " " +
            str(ans[k].undi) + "\n")
    print(str(k) + " " +
        str(ans[k].correct) + " " +
        str(ans[k].incorrect) + " " +
        str(ans[k].undi))

f.close()
