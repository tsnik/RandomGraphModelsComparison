from utills import get_var


def simulate(tree, banks, defaulted=None):
    rounds = 1
    isNewDefaults = False
    if defaulted is None:
        defaulted = []
    for bank in [bank_t for bank_t in banks if bank_t["id"] not in defaulted]:
        capital = bank["capital"]
        for default in defaulted:
            capital -= tree[default][bank["id"]]
        if capital < 0:
            defaulted.append(bank["id"])
            isNewDefaults = True
    if isNewDefaults:
        rounds_t, defaulted = simulate(tree, banks, defaulted)
        rounds += rounds_t
    return rounds, defaulted


def full_simulation(tree, banks):
    result = []
    for bank in banks:
        result.append({"hazard": 0, "induced_defaults": 0, "hazard_rate": 0.0, "rounds": 0})
    for bank in banks:
        rounds, defaulted = simulate(tree, banks, [bank["id"]])
        result[bank["id"]]["induced_defaults"] = len(defaulted) - 1
        result[bank["id"]]["rounds"] = rounds
        for default in defaulted:
            if default != bank["id"]:
                result[default]["hazard"] += 1
    for res in result:
        res["hazard_rate"] = res["hazard"] / (len(banks) - 1)
    return result


def monte_carlo_orig(banks, num, tree_generator_class, *args):
    tree_generator = tree_generator_class(banks, *args)
    res = []
    for i in range(num):
        tree = tree_generator.generate()
        print(tree_generator.check_tree())
        result = full_simulation(tree, banks)
        res.append(result)
        print(i)
        print(result)
    return res


def monte_carlo(banks, num, tree_generator_class, *args):
    res = monte_carlo_orig(banks, num, tree_generator_class, *args)
    hist = []
    for result in res:
        tmp = [res["induced_defaults"] for res in result]
        hist.append(get_var(tmp, 0.95))
        # hist.append(round(sum(tmp)/len(tmp)))
        # hist.append(result[0]["hazard"])
    return hist
