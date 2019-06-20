import pickle

from utills import get_var, get_result_e, get_result_v, plot_graph

for num in range(1, 7):
    with open('data\\GaiKapadiaHetero\\simulation' + str(num) + '.pickle', 'rb') as f:
        simulation = pickle.load(f)
        print(simulation)
        hist_e = []
        hist_v = []
        keys = sorted(list(simulation["simulations"].keys()))
        for k in keys:
            hist_e.append(get_var(get_result_e(simulation["simulations"][k]), 0.95))
            hist_v.append(get_var(get_result_v(simulation["simulations"][k]), 0.95))
        # plot_hists(hist, len(simulation["banks"]) - 1)
        # plot_graph(keys, hist_e)
        plot_graph(keys, hist_v)
