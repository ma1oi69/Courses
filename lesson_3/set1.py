a = set('hello')
b = {1, 2, 3, 4, 4}


print(type(b))
print(b)

b.discard(1)
print(b)

b.add(9)
print(b)

b.remove(9)
print(b)

b.copy()

e = set(range(9))
print(e)

print(len(e))

print(11 in e)

print(e & b)

print(a)

print(type(a))