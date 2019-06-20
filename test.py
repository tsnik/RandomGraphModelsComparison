import math
import random
import matplotlib.pyplot as plt

from utills import part_distr2, part_distr


def monte_carlo(num, t):
    hists = []
    for i in range(t):
        hists.append([])
    for ind in range(num):
        print(ind)
        total = 1.0
        r = []
        for e in range(t):
            debt = random.random() * total
            total = total - debt
            r.append(debt)
            hists[e].append(debt)
    return hists


def monte_carlo2(num):
    hist = []
    for ind in range(num):
        print(ind)
        dist = []
        for e in range(50):
            dist.append(random.random())
        st = sum(dist)
        dist_e = [d / st for d in dist]
        hist.append(dist_e[49])
    return hist


def get_distribution_restrict2(count, restrictions, total):
    dist = list(range(count))
    left = 1.0
    ratios = [r / total for r in restrictions]
    to_do = list(range(count))
    for e in range(count - 1):
        ind = to_do[round(random.random() * (len(to_do) - 1))]
        high = min(left, ratios[ind])
        low = min(max(0, left - sum([r for a, r in enumerate(restrictions) if a in to_do])), high)
        d = low + random.random() * (high - low)
        dist[ind] = d
        left -= d
        to_do.remove(ind)
    dist[to_do[0]] = left
    return dist


def monte_carlo3(num, t):
    hists = []
    for e in range(t):
        hists.append([])
    for ind in range(num):
        print(ind)
        dist = get_distribution_restrict2(50, [1.0 for e in range(50)], 1.0)
        for e, d in enumerate(dist):
            hists[e].append(dist[e])
    return hists


def monte_carlo4(num, t):
    hists = []
    for e in range(t):
        hists.append([])
    for ind in range(num):
        print(ind)
        dist = part_distr(t)
        for e, d in enumerate(dist):
            hists[e].append(dist[e])
    return hists


def print_metrics(hist):
    mean = sum(hist) / len(hist)
    var = sum([(h - mean) ** 2 for h in hist]) / len(hist)
    print(mean)
    print(math.sqrt(var))
    print(min(hist))
    print(max(hist))


def plot_hists(hist, hist2, bins=49):
    plt.hist((hist, hist2), bins=bins, normed=True)
    #plt.hist(hist2, bins=bins, normed=True)
    plt.show()
    plt.hist(hist, bins=bins, normed=True, cumulative=True)
    plt.hist(hist2, bins=bins, normed=True, cumulative=True)
    plt.show()


# hist = monte_carlo(1000, 50)
# # hist2 = monte_carlo2(1000)
# hist3 = monte_carlo3(1000, 50)
hist4 = monte_carlo4(1000, 10)
#hist4 = monte_carlo3(1000, 10)
#hist5 = monte_carlo3(1000, 20)
#hist6 = monte_carlo3(1000, 30)
plot_hists(hist4[0], hist4[9], 100)

# for i in range(0, 50, 10):
#     plot_hists(hist[i], hist3[i], 100)

