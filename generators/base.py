class TreeGenerator:
    def __init__(self, banks):
        self.banks = banks
        self.tree = None

    def generate(self):
        self.tree = self._generate()
        #if not self.check_tree():
        #    raise Exception()
        return self.tree

    def _generate(self):
        return None

    def check_tree(self, banks=None, tree=None):
        if banks is None:
            banks = self.banks
        if tree is None:
            tree = self.tree
        debts_loans = []
        for bank in banks:
            debts = sum(self.tree[bank["id"]])
            loans = sum([row[bank["id"]] for row in tree])
            debts_loans.append(
                debts == bank["debt"] and loans == bank["loans"] and all(el >= 0 for el in tree[bank["id"]]))
        return all(debts_loans)
