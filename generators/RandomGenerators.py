from base import TreeGenerator
import random


class RandomGenerator(TreeGenerator):
    def _generate(self):
        banks = self.banks
        debt_loans = [[bank["debt"], bank["loans"]] for bank in banks]
        tree = []
        for bank in banks:
            bank_debts = []
            for bank_creditor in banks:
                debt = round(random.random() * min(debt_loans[bank["id"]][0], debt_loans[bank_creditor["id"]][1]))
                if bank["id"] == len(banks) - 1:
                    debt = debt_loans[bank_creditor["id"]][1]
                if bank["id"] == bank_creditor["id"]:
                    debt = 0
                if bank_creditor["id"] == len(banks) - 1:
                    debt = min(debt_loans[bank["id"]][0], debt_loans[bank_creditor["id"]][1])
                    i = 0
                    while debt != debt_loans[bank["id"]][0]:
                        add_debt = min(debt_loans[bank["id"]][0] - debt, debt_loans[i][1])
                        bank_debts[i] += add_debt
                        debt_loans[bank["id"]][0] -= add_debt
                        debt_loans[i][1] -= add_debt
                        i += 1
                debt_loans[bank["id"]][0] -= debt
                debt_loans[bank_creditor["id"]][1] -= debt
                bank_debts.append(debt)
            tree.append(bank_debts)
        return tree


class RandomGeneratorDistributionBase(TreeGenerator):
    def get_distribution_restrict(self, count, restrictions, total):
        pass

    def _generate(self):
        banks = self.banks
        debt_loans = [[bank["debt"], bank["loans"]] for bank in banks]
        tree = []
        for bank in banks:
            bank_debts = []
            dist = self.get_distribution_restrict(len(banks), [0 if e == bank["id"] else debt[1] for e, debt
                                                               in enumerate(debt_loans)], bank["debt"])
            for bank_creditor in banks:
                debt = round(bank["debt"] * dist[bank_creditor["id"]])
                if debt > debt_loans[bank["id"]][0]:
                    debt = debt_loans[bank["id"]][0]
                if bank_creditor["id"] == len(banks) - 1:
                    debt = min(debt_loans[bank["id"]][0], debt_loans[bank_creditor["id"]][1])
                    i = 0
                    while debt != debt_loans[bank["id"]][0]:
                        add_debt = min(debt_loans[bank["id"]][0] - debt, debt_loans[i][1])
                        bank_debts[i] += add_debt
                        debt_loans[bank["id"]][0] -= add_debt
                        debt_loans[i][1] -= add_debt
                        i += 1
                if bank["id"] == len(banks) - 1:
                    debt = debt_loans[bank_creditor["id"]][1]
                debt_loans[bank["id"]][0] -= debt
                debt_loans[bank_creditor["id"]][1] -= debt
                bank_debts.append(debt)
            tree.append(bank_debts)
        return tree


class RandomGeneratorDistribution(RandomGeneratorDistributionBase):
    def get_distribution_restrict(self, count, restrictions, total):
        dist = []
        for e in range(count):
            dist.append(random.random())
        s = sum(dist)
        dist_res = [d / s for d in dist]
        e = 0
        fixed = []
        while e != count - 1:
            if round(dist_res[e] * total) > restrictions[e]:
                rate = min(1, restrictions[e] / total)
                tmp = random.random() * rate
                diff = dist_res[e] - tmp
                dist_res[e] = tmp
                if e not in fixed:
                    fixed.append(e)
                l = count - len(fixed)
                for k in range(count):
                    if k not in fixed:
                        dist_res[k] += diff / l
                e = 0
            else:
                e += 1
        return dist_res


class RandomGeneratorDistribution2(RandomGeneratorDistributionBase):
    def get_distribution_restrict(self, count, restrictions, total):
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