import sys

class CaseInsensitiveSet(set):
    def add(self, value):
        set.add(self, value.casefold())

    def __contains__(self, value):
        return set.__contains__(self, value.casefold())

    def discard(self, value):
        set.discard(self, value.casefold())

    def remove(self, value):
        set.remove(self, value.casefold())


s = CaseInsensitiveSet()

s.add("Rodrigo")
s.add("mathspp")
s.add("RODRIGO")

print(s)  # CaseInsensitiveSet({'rodrigo', 'mathspp'})

print("In: ", "RODRIGO" in s)  # True

s.discard("MaThSpP")  # Try to remove "mathspp"
print("Discard: ", s)  # CaseInsensitiveSet({'rodrigo'})

s.discard("mathspp")  # Try to remove "mathspp"
print(s)  # CaseInsensitiveSet({'rodrigo'})

s.add("mathspp")
s.remove("rodrigo")  # Remove "rodrigo" and error if not present
print(s)  # CaseInsensitiveSet({'mathspp'})