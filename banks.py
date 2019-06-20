from utills import print_metrics, plot_hists, gen_banks_from_bis
from simulation import monte_carlo
from generators.RandomGenerators import RandomGeneratorDistribution2
from generators.GaiKapadiaGenerator import GaiKapadiaGenerator, GaiKapadiaGeneratorHetero2


banks = gen_banks_from_bis("data\\Europe.csv")

hist = monte_carlo(banks, 1000, RandomGeneratorDistribution2)
hist2 = monte_carlo(banks, 1000, GaiKapadiaGenerator, 0.3)
hist3 = monte_carlo(banks, 1000, GaiKapadiaGeneratorHetero2)

print("Gen_tree1")
print_metrics(hist)
print("Gen_tree2")
print_metrics(hist2)
print("Gen_tree3")
print_metrics(hist3)

plot_hists(hist, 30, len(banks) - 1)
plot_hists(hist2, 30, len(banks) - 1)
plot_hists(hist3, 30, len(banks) - 1)
