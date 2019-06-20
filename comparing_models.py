from GaiKapadiaGenerator import GaiKapadiaGenerator, GaiKapadiaGeneratorHetero, GaiKapadiaGeneratorHetero2
from RandomGenerators import RandomGenerator, RandomGeneratorDistribution2
from simulation import monte_carlo
from utills import gen_banks, print_metrics, get_var, plot_graph, plot_hists

import pickle
#
# for num in range(1, 6):
#
#     with open('data\\GaiKapadia\\simulation' + str(num) + '.pickle', 'rb') as f:
#         simulation = pickle.load(f)
#     print(simulation)
#     hist = []
#     keys = sorted(list(simulation["simulations"].keys()))
#     for k in keys:
#         tmp_hist = []
#         for result in simulation["simulations"][k]:
#             tmp = [res["induced_defaults"] for res in result]
#             tmp_hist.append(sum(tmp)/len(tmp))
#             # tmp_hist.append(get_var(tmp, 0.95))
#         hist.append(get_var(tmp_hist, 0.95))
#     # plot_hists(hist, len(simulation["banks"]) - 1)
#     plot_graph(keys, hist)

#
banks = gen_banks(100)
hist = monte_carlo(banks, 100, RandomGeneratorDistribution2)
# hist2 = monte_carlo(banks, 1000, GaiKapadiaGenerator, 0.25)
hist3 = monte_carlo(banks, 100, GaiKapadiaGeneratorHetero2, 0.25)
hist4 = monte_carlo(banks, 100, GaiKapadiaGeneratorHetero2, 1)
#
print("Gen_tree1")
print_metrics(hist)
# print("Gen_tree2")
# print_metrics(hist2)
print("Gen_tree3")
print_metrics(hist3)
print("Gen_tree4")
print_metrics(hist4)

plot_hists(hist, len(banks) - 1)
plot_hists(hist3, len(banks) - 1)
plot_hists(hist4, len(banks) - 1)
