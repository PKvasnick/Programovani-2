# Source - https://stackoverflow.com/a/21894086
# Posted by Basj, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-12, License - CC BY-SA 4.0


class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value, []).append(key)

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key)
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value, []).append(key)

    def __delitem__(self, key):
        self.inverse.setdefault(self[key], []).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]:
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)


bd = bidict({"a": 1, "b": 2})
print(bd)  # {'a': 1, 'b': 2}
print(bd.inverse)  # {1: ['a'], 2: ['b']}
bd["c"] = 1  # Now two keys have the same value (= 1)
print(bd)  # {'a': 1, 'c': 1, 'b': 2}
print(bd.inverse)  # {1: ['a', 'c'], 2: ['b']}
del bd["c"]
print(bd)  # {'a': 1, 'b': 2}
print(bd.inverse)  # {1: ['a'], 2: ['b']}
del bd["a"]
print(bd)  # {'b': 2}
print(bd.inverse)  # {2: ['b']}
bd["b"] = 3
print(bd)  # {'b': 3}
print(bd.inverse)  # {2: [], 3: ['b']}
