class CaseInsensitiveSet:

    def __init__(self):
        self.set_ = set()

    def add(self, item):
        self.set.add(item.casefold())

    def __contains__(self, item):
        return item.casefold() in self.set

    def remove(self, item):
        self.set.remove(item.casefold())

    def discard(self, item):
        self.set.discard(item.casefold())

    def __str__(self):
        return str(self.set)

    

print("Vytvoř:")
s = CaseInsensitiveSet()

s.add("Rodrigo")
s.add("mathspp")
s.add("RODRIGO")

print(s)  # CaseInsensitiveSet({'rodrigo', 'mathspp'})

print("Contains: ")
print("RODRIGO" in s)  # True

print("Discard")
s.discard("MaThSpP")  # Try to remove "mathspp"
print(s)  # CaseInsensitiveSet({'rodrigo'})

s.discard("mathspp")  # Try to remove "mathspp"
print(s)  # CaseInsensitiveSet({'rodrigo'})

print("AddRemove")
s.add("mathspp")
s.remove("rodrigo")  # Remove "rodrigo" and error if not present
print(s)  # CaseInsensitiveSet({'mathspp'})