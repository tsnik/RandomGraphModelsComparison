import pickle

from generators.GaiKapadiaGenerator import GaiKapadiaGeneratorHetero2, GaiKapadiaGenerator
from generators.RandomGenerators import RandomGeneratorDistribution2
from simulation import monte_carlo_orig
from utills import gen_banks

for num in range(1, 21):
    print("simulation" + str(num))
    banks = gen_banks(100)
    data = {"banks": banks}

    simulations_homo = {}
    simulations_hetero = {}
    simulations_random = {}
    x = [0.25]
    mean = []
    var = []
    for i in x:
        print(i)
        simulations_homo[i] = monte_carlo_orig(banks, 100, GaiKapadiaGenerator, i)
        simulations_hetero[i] = monte_carlo_orig(banks, 100, GaiKapadiaGeneratorHetero2, i)
        simulations_random[i] = monte_carlo_orig(banks, 100, RandomGeneratorDistribution2)

    data["simulations_homo"] = simulations_homo
    data["simulations_hetero"] = simulations_hetero
    data["simulations_random"] = simulations_random

    with open('data\\HomoVsHeteroVsRandom\\simulation' + str(num) + '.pickle', 'wb') as f:
        pickle.dump(data, f)
