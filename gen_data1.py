import pickle

from generators.GaiKapadiaGenerator import GaiKapadiaGeneratorHetero2, GaiKapadiaGenerator
from simulation import monte_carlo_orig
from utills import gen_banks

for num in range(20, 21):
    print("simulation" + str(num))
    banks = gen_banks(100)
    data = {"banks": banks}

    simulations_homo = {}
    simulations_hetero = {}
    x = [0.25, 0.5, 0.75]
    mean = []
    var = []
    for i in x:
        print(i)
        simulations_homo[i] = monte_carlo_orig(banks, 100, GaiKapadiaGenerator, i)
        simulations_hetero[i] = monte_carlo_orig(banks, 100, GaiKapadiaGeneratorHetero2, i)

    data["simulations_homo"] = simulations_homo
    data["simulations_hetero"] = simulations_hetero

    with open('data\\HomoVsHetero\\simulation' + str(num) + '.pickle', 'wb') as f:
        pickle.dump(data, f)
