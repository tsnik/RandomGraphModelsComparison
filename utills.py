import csv
import random
import matplotlib.pyplot as plt
import math

SCALE = 1000


def get_distribution(count):
    dist = []
    for i in range(count):
        dist.append(random.random())
    s = sum(dist)
    return [d / s for d in dist]


def gen_banks(count):
    banks = []
    total_debt = count * SCALE * 5
    total_loans = count * SCALE * 5
    total_loans_w = total_loans
    loans_dist = get_distribution(count)
    for i in range(count):
        # actives
        actives = round(random.random() * SCALE)
        loans = round(loans_dist[i] * total_loans)  # total other banks debt  to bank
        total_loans_w -= loans
        if i == count - 1:
            loans += total_loans_w
            total_loans_w = 0

        sum_actives = actives + loans

        capital = round(random.random() * SCALE * 5)
        # passives
        debt = round(random.random() * min(total_debt, sum_actives))  # bank total debt to other banks
        total_debt -= debt
        if i == count - 1:
            debt += total_debt
            total_debt = 0
        if sum_actives < capital + debt:
            actives = round(random.random() * SCALE) + capital + debt - loans
        sum_actives = actives + loans

        deposits = round(random.random() * (sum_actives - capital - debt))
        borrowings = sum_actives - capital - debt - deposits
        banks.append({"id": i, "capital": capital, "deposits": deposits, "actives": actives,
                      "borrowings": borrowings, "debt": debt, "loans": loans})
    return banks


def gen_banks_from_bis(filename):
    banks = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            if row[0] not in banks.keys():
                banks[row[0]] = {"loans": 0, "debt": 0, "label": row[0]}
            if row[1] not in banks.keys():
                banks[row[1]] = {"loans": 0, "debt": 0, "label": row[1]}
            if row[2] != "NaN":
                amount = int(round(float(row[2])))
                banks[row[0]]["debt"] += amount
                banks[row[1]]["loans"] += amount
    for i, bank in enumerate(banks.values()):
        bank["capital"] = 0.5 * bank["loans"]
        bank["id"] = i
    return list(banks.values())


def check_banks(banks):
    debt_loans = sum([bank["loans"] for bank in banks]) == sum([bank["debt"] for bank in banks])
    balances = [bank["actives"] + bank["loans"] == bank["capital"] + bank["borrowings"]
                + bank["debt"] + bank["deposits"] for bank in banks]

    return debt_loans and all(balances)


def get_var(arr, ci):
    target = ci + (1 - ci) / 2
    target_i = len(arr) * target
    p1 = target_i - int(target_i)
    i = int(target_i)
    if p1 == 0:
        p1 = 1
    sor = sorted(arr)
    if i == len(sor) - 1:
        sor.append(sor[i])
    return sor[i] * p1 + sor[i + 1] * (1 - p1)


def print_metrics(hist):
    mean = sum(hist) / len(hist)
    var = sum([(h - mean) ** 2 for h in hist]) / len(hist)
    print(round(mean, 2))
    print(round(math.sqrt(var), 2))
    print(min(hist))
    print(max(hist))
    print(get_var(hist, 0.95))


def plot_hists(hist, bins=49, range=None):
    if range is None:
        range = bins
    plt.hist(hist, bins=bins, range=(0, range), normed=True)
    plt.show()
    plt.hist(hist, bins=bins, range=(0, range), normed=True, cumulative=True)
    plt.show()


def part_distr(n):
    dist = []
    for i in range(n):
        dist.append(random.random())
    dist.sort()
    return dist


def part_distr2(n):
    if n == 0:
        return []
    dist = []
    t = random.random()
    lower = part_distr2(int((n - 1) / 2))
    upper = part_distr2(int((n - 1) / 2) + (n - 1) % 2)
    lower = [l * t for l in lower]
    upper = [u * (1 - t) + t for u in upper]
    dist.extend(lower)
    dist.append(t)
    dist.extend(upper)
    return dist


def plot_graph(x, y, path=None, labels=None):
    if type(y[0]) != list:
        y = [y]
    for i, t in enumerate(y):
        if labels is not None:
            plt.plot(x, t, label=labels[i])
        else:
            plt.plot(x, t)
    if len(y) > 1:
        plt.legend()
    if path is None:
        plt.show()
    else:
        plt.savefig(path)
        plt.clf()


def save_graph(path):
    plt.savefig(path)


def get_result(simulation, func):
    tmp_hist = []
    for result in simulation:
        defaults = [res["induced_defaults"] for res in result]
        tmp_hist.append(func(defaults))
    return tmp_hist


def get_result_e(simulation):
    return get_result(simulation, lambda x: sum(x)/len(x))


def get_result_v(simulation):
    return get_result(simulation, lambda x: get_var(x, 0.95))
