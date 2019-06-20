import pickle
from utills import check_banks, print_metrics, plot_hists, gen_banks, plot_graph, save_graph, gen_banks_from_bis
from simulation import monte_carlo, monte_carlo_orig
from RandomGenerators import RandomGenerator, RandomGeneratorDistribution2
from GaiKapadiaGenerator import GaiKapadiaGenerator, GaiKapadiaGeneratorHetero, GaiKapadiaGeneratorHetero2, \
    GaiKapadiaGeneratorExtend
import math

for num in range(1, 7):
        #
        banks = gen_banks(100)
        data = {"banks": banks}

        # with open('data2.pickle', 'rb') as f:
        #     banks = pickle.load(f)

        # print(check_banks(banks))
        # hist = monte_carlo(banks, 1000, RandomGenerator)
        # hist2 = monte_carlo(banks, 100, GaiKapadiaGenerator, 0.3)
        # hist3 = monte_carlo(banks, 100, GaiKapadiaGeneratorHetero)
        # hist4 = monte_carlo(banks, 100, GaiKapadiaGeneratorHetero2, 0.3)

        # print("Gen_tree1")
        # print_metrics(hist)
        # print("Gen_tree2")
        # print_metrics(hist2)
        # print("Gen_tree3")
        # print_metrics(hist3)
        # print("Gen_tree4")
        # print_metrics(hist4)

        # plot_hists(hist, len(banks) - 1)
        # plot_hists(hist2, len(banks) - 1)
        # plot_hists(hist3, len(banks) - 1)
        # plot_hists(hist4, len(banks) - 1)

        # x = [0.2 + 0.05 * n for n in range(17)]
        # mean = []
        # var = []
        # for i in x:
        #     print(i)
        #     hist = monte_carlo(banks, 100, GaiKapadiaGeneratorHetero2, i)
        #     m = sum(hist) / len(hist)
        #     mean.append(m)
        #     var.append(math.sqrt(sum([(h - m) ** 2 for h in hist]) / len(hist)))
        #
        # plot_graph(x, mean, 'graphs\\mean0\\' + str(num) + '.png')
        # plot_graph(x, var, 'graphs\\var0\\' + str(num) + '.png')
        #
        # # 0.8
        # x = [0.01 * n for n in range(20)]
        # mean = []
        # var = []
        # for i in x:
        #     print(i)
        #     hist = monte_carlo(banks, 100, GaiKapadiaGeneratorHetero2, i)
        #     m = sum(hist) / len(hist)
        #     mean.append(m)
        #     var.append(math.sqrt(sum([(h - m) ** 2 for h in hist]) / len(hist)))
        #
        # plot_graph(x, mean, 'graphs\\mean02\\' + str(num) + '.png')
        # plot_graph(x, var, 'graphs\\var02\\' + str(num) + '.png')
        #
        # simulations = {}
        # x = [0.01 * n for n in range(100)]
        # mean = []
        # var = []
        # for i in x:
        #     print(i)
        #     simulations[i] = monte_carlo_orig(banks, 100, GaiKapadiaGeneratorHetero2, i)
        #
        # data["simulations"] = simulations
        # with open('simulation' + str(num) + '.pickle', 'wb') as f:
        #     pickle.dump(data, f)

banks = gen_banks_from_bis("data\\Europe.csv")

hist = monte_carlo(banks, 1000, RandomGenerator)
hist2 = monte_carlo(banks, 1000, GaiKapadiaGenerator, 0.3)
hist3 = monte_carlo(banks, 1000, GaiKapadiaGeneratorHetero)
hist4 = monte_carlo(banks, 1000, GaiKapadiaGeneratorHetero2, 0.3)

print("Gen_tree1")
print_metrics(hist)
print("Gen_tree2")
print_metrics(hist2)
print("Gen_tree3")
print_metrics(hist3)
print("Gen_tree4")
print_metrics(hist4)

plot_hists(hist, 30, len(banks) - 1)
plot_hists(hist2, 30, len(banks) - 1)
plot_hists(hist3, 30, len(banks) - 1)
plot_hists(hist4, 30, len(banks) - 1)
