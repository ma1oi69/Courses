a = 5
b = 5
c = 5

print(id(a))
print(id(b))
print(id(c))

lst_ = [1, 2, 3]
lst_1 = [1, 2, 3]

print(id(lst_))
print(id(lst_1))

a += 1
b += 2
c += 3

lst_ = lst_1

print(id(lst_))
print(id(lst_1))