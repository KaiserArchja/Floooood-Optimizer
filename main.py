import random
from obj import obj_func
from funcs import get_Pk, get_best
import math

Npop = 100
iter = 200
Ne = 5
pop = [random.uniform(-10000000,100000) for i in range(Npop)]
rand = [random.random() for i in range(Npop)]
randn = [random.randrange(-1000000000,+1000000000) for i in range(Npop)]
S = [min(pop) + rand[i]*(max(pop) - min(pop)) for i in range(Npop)]
S_new = [0 for i in range(Npop)]

for i in range(1, iter+1):
    for j in range(Npop):
        mini = min(S)
        maxi = max(S)
        best = get_best(obj_func, S)
        Pei = ((obj_func(S[j]) - obj_func(mini))/(obj_func(maxi) - obj_func(mini)))**2
        if rand[j] > (rand[j] + Pei):
            S_new[j] = S[j] + (((get_Pk(i, iter)**randn[j])/i) * (rand[j]*(maxi-mini) + mini))
        else:
            S_new[j] = best + rand[j] * (random.choice(S) - S[j])
        if obj_func(S_new[j]) < obj_func(S[j]):
            S[j] = S_new[j]
        if obj_func(S[j]) < obj_func(best):
            S[S.index(best)] = S[j]
        if rand[j] < (abs(math.sin(rand[j]/i))):
            for l in range(Ne):
                S_new[l] = best + rand[j]*(rand[j]*(maxi - mini) + mini)
                if obj_func(S_new[l]) < obj_func(best):
                    S[S.index(best)] = S_new[l]
    print("X: ",best,"Y: ",obj_func(best))