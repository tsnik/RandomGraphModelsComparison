from base import TreeGenerator
from utills import part_distr, part_distr2
import random


class GaiKapadiaGenerator(TreeGenerator):
    def __init__(self, banks, n=0.75):
        super().__init__(banks)
        self.n = n

    def gen_links(self):
        self.tree = []
        for bank_e in self.banks:
            row = []
            for bank in self.banks:
                t = 0
                if bank["id"] != bank_e["id"] and random.random() < self.n:
                    t = 1
                row.append(t)
            self.tree.append(row)

    def distribute_assets(self, bank):
        s = sum([r[bank["id"]] for r in self.tree])
        a = 0
        if s != 0:
            a = round(bank["loans"] / sum([r[bank["id"]] for r in self.tree]))
        for i in range(len(self.tree)):
            self.tree[i][bank["id"]] = a * self.tree[i][bank["id"]]
        # bank["loans"] = sum([r[bank["id"]] for r in self.tree])

    def _generate(self):
        self.gen_links()
        for bank in self.banks:
            self.distribute_assets(bank)
        for bank in self.banks:
            bank["debt"] = sum(self.tree[bank["id"]])
        return self.tree


class GaiKapadiaGeneratorHetero(GaiKapadiaGenerator):
    PART_DISTR = lambda self, n: part_distr(n)

    def distribute_assets(self, bank):
        s = sum([r[bank["id"]] for r in self.tree])
        assets = bank["loans"]
        if s != 0:
            dist = self.PART_DISTR(s - 1)
            dist.append(1)
            e = 0
            prev = 0
            for i in range(len(self.tree)):
                if self.tree[i][bank["id"]] != 0:
                    curr = round(assets * dist[e])
                    self.tree[i][bank["id"]] = curr - prev
                    prev = curr
                    e += 1
        #bank["loans"] = sum([r[bank["id"]] for r in self.tree])


class GaiKapadiaGeneratorHetero2(GaiKapadiaGeneratorHetero):
    PART_DISTR = lambda self, n: part_distr2(n)


class GaiKapadiaGeneratorExtend(GaiKapadiaGenerator):
    def gen_links(self):
        self.tree = []
        for bank_e in self.banks:
            row = []
            n = random.random()
            for bank in self.banks:
                t = 0
                if bank["id"] != bank_e["id"] and random.random() < n:
                    t = 1
                row.append(t)
            self.tree.append(row)
