import pickle

from generators.GaiKapadiaGenerator import GaiKapadiaGeneratorHetero2, GaiKapadiaGenerator
from simulation import monte_carlo_orig
from utills import gen_banks

# Homogeneous
for num in range(1, 7):
        banks = gen_banks(100)
        data = {"banks": banks}

        simulations = {}
        x = [0.01 * n for n in range(100)]
        mean = []
        var = []
        for i in x:
            print(i)
            simulations[i] = monte_carlo_orig(banks, 100, GaiKapadiaGenerator, i)

        data["simulations"] = simulations
        with open('data\\GaiKapadia\\simulation' + str(num) + '.pickle', 'wb') as f:
            pickle.dump(data, f)

# Heterogeneous
for num in range(1, 7):
        banks = gen_banks(100)
        data = {"banks": banks}

        simulations = {}
        x = [0.01 * n for n in range(100)]
        mean = []
        var = []
        for i in x:
            print(i)
            simulations[i] = monte_carlo_orig(banks, 100, GaiKapadiaGeneratorHetero2, i)

        data["simulations"] = simulations
        with open('data\\GaiKapadiaHetero\\simulation' + str(num) + '.pickle', 'wb') as f:
            pickle.dump(data, f)
