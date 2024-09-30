import math

def get_Pk(iter, max_iter):
    return (1.2/max_iter)*((math.sqrt(max_iter*(iter**2) + 1) + ((4/(max_iter*iter))*math.log(math.sqrt(max_iter*(iter**2)+1)+(max_iter/4))))**(-2/3))

def get_best(func, pop):
    best = func(pop[0])
    ans = 0
    for i in pop:
        if func(i) <= best:
            best = func(i)
            ans = i
    return ans