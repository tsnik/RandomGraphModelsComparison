import math
import pickle

from GaiKapadiaGenerator import GaiKapadiaGeneratorHetero2, GaiKapadiaGenerator
from simulation import monte_carlo, monte_carlo_orig
from utills import gen_banks, get_var, plot_graph, get_result_e, get_result_v, print_metrics, plot_hists

# for num in range(20, 21):
# #     print("simulation" + str(num))
# #     banks = gen_banks(100)
# #     data = {"banks": banks}
# #
# #     simulations_homo = {}
# #     simulations_hetero = {}
# #     x = [0.25, 0.5, 0.75]
# #     mean = []
# #     var = []
# #     for i in x:
# #         print(i)
# #         simulations_homo[i] = monte_carlo_orig(banks, 100, GaiKapadiaGenerator, i)
# #         simulations_hetero[i] = monte_carlo_orig(banks, 100, GaiKapadiaGeneratorHetero2, i)
# #
# #     data["simulations_homo"] = simulations_homo
# #     data["simulations_hetero"] = simulations_hetero
# #
# #     with open('simulation' + str(num) + '.pickle', 'wb') as f:
# #         pickle.dump(data, f)

abs_e = []
perc_e = []
abs_v = []
perc_v = []
homo_e = []
hetero_e = []
homo_v = []
hetero_v = []

for num in range(1, 21):
    with open('data\\HomoVsHetero\\simulation' + str(num) + '.pickle', 'rb') as f:
        simulation = pickle.load(f)
    k = 0.75
    var1_e = get_var(get_result_e(simulation["simulations_homo"][k]), 0.95)
    var2_e = get_var(get_result_e(simulation["simulations_hetero"][k]), 0.95)
    var1_v = get_var(get_result_v(simulation["simulations_homo"][k]), 0.95)
    var2_v = get_var(get_result_v(simulation["simulations_hetero"][k]), 0.95)
    homo_e.append(var1_e)
    hetero_e.append(var2_e)
    homo_v.append(var1_v)
    hetero_v.append(var2_v)
    abs_e.append(var2_e - var1_e)
    if var1_e == 0:
        var1_e += 1
    if var1_v == 0:
        var1_v += 1
    perc_e.append(round((var2_e/var1_e), 2))
    abs_v.append(var2_v - var1_v)
    perc_v.append(round((var2_v / var1_v), 2))

x = list(range(20))
plot_graph(x, [homo_e, hetero_e], labels=["Homogeneous", "Heterogeneous"])
plot_graph(x, [homo_v, hetero_v], labels=["Homogeneous", "Heterogeneous"])
plot_graph(x, abs_e)
plot_graph(x, perc_e)
plot_graph(x, abs_v)
plot_graph(x, perc_v)

print("abs_e")
print_metrics(abs_e)
print("Perc_e")
print_metrics(perc_e)
print("abs_v")
print_metrics(abs_v)
print("Perc_v")
print_metrics(perc_v)

# with open('data\\HomoVsHetero\\simulation2.pickle', 'rb') as f:
#     simulation = pickle.load(f)
#     k = 0.25
#     hist_homo_e = get_result_e(simulation["simulations_homo"][k])
#     hist_homo_v = get_result_v(simulation["simulations_homo"][k])
#     hist_hetero_e = get_result_e(simulation["simulations_hetero"][k])
#     hist_hetero_v = get_result_v(simulation["simulations_hetero"][k])
#
#     # plot_hists(hist_homo_e, len(simulation["banks"]) - 1)
#     # plot_hists(hist_hetero_e, len(simulation["banks"]) - 1)
#     #
#     # print_metrics(hist_homo_e)
#     # print("Hetero")
#     # print_metrics(hist_hetero_e)
#
#     plot_hists(hist_homo_v, len(simulation["banks"]) - 1)
#     plot_hists(hist_hetero_v, len(simulation["banks"]) - 1)
#
#     print_metrics(hist_homo_v)
#     print("Hetero")
#     print_metrics(hist_hetero_v)