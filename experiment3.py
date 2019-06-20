import math
import pickle

from utills import get_var, plot_graph, get_result_e, get_result_v, print_metrics

# for num in range(1, 21):
#     print("simulation" + str(num))
#     banks = gen_banks(100)
#     data = {"banks": banks}
#
#     simulations_homo = {}
#     simulations_hetero = {}
#     simulations_random = {}
#     x = [0.25]
#     mean = []
#     var = []
#     for i in x:
#         print(i)
#         simulations_homo[i] = monte_carlo_orig(banks, 100, GaiKapadiaGenerator, i)
#         simulations_hetero[i] = monte_carlo_orig(banks, 100, GaiKapadiaGeneratorHetero2, i)
#         simulations_random[i] = monte_carlo_orig(banks, 100, RandomGeneratorDistribution2)
#
#     data["simulations_homo"] = simulations_homo
#     data["simulations_hetero"] = simulations_hetero
#     data["simulations_random"] = simulations_random
#
#     with open('simulation' + str(num) + '.pickle', 'wb') as f:
#         pickle.dump(data, f)

homo_e = []
hetero_e = []
homo_v = []
hetero_v = []
random_e = []
random_v = []
abs_e = []
abs_v = []
perc_e = []
perc_v = []

for num in range(1, 21):
    with open('data\\HomoVsHeteroVsRandom\\simulation' + str(num) + '.pickle', 'rb') as f:
        simulation = pickle.load(f)
    k = 0.25
    var1_e = get_var(get_result_e(simulation["simulations_homo"][k]), 0.95)
    var2_e = get_var(get_result_e(simulation["simulations_hetero"][k]), 0.95)
    var1_v = get_var(get_result_v(simulation["simulations_homo"][k]), 0.95)
    var2_v = get_var(get_result_v(simulation["simulations_hetero"][k]), 0.95)
    var3_e = get_var(get_result_e(simulation["simulations_random"][k]), 0.95)
    var3_v = get_var(get_result_v(simulation["simulations_random"][k]), 0.95)
    homo_e.append(var1_e)
    hetero_e.append(var2_e)
    homo_v.append(var1_v)
    hetero_v.append(var2_v)
    random_e.append(var3_e)
    random_v.append(var3_v)

    abs_e.append(var2_e - var3_e)
    perc_e.append(round((var2_e/var3_e), 2))
    abs_v.append(var2_v - var3_v)
    perc_v.append(round((var2_v / var3_v), 2))

x = list(range(20))
plot_graph(x, [hetero_e, random_e], labels=["Heterogeneous", "Random"])
plot_graph(x, [hetero_v, random_v], labels=["Heterogeneous", "Random"])
# plot_graph(x, [homo_e, random_e], labels=["Homogeneous", "Random"])
# plot_graph(x, [homo_v, random_v], labels=["Homogeneous", "Random"])
# plot_graph(x, [homo_e, hetero_e, random_e], labels=["Homogeneous", "Heterogeneous", "Random"])
# plot_graph(x, [homo_v, hetero_v, random_v], labels=["Homogeneous", "Heterogeneous", "Random"])

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