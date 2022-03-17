from collections import defaultdict


class BirthStat:
    def __init__(self):
        self.counters = defaultdict(int)

    def count(self, users):
        for u in users:
            self.counters[u.birth] += 1

    def num_occurences(self, birth):
        return self.counters[birth]
