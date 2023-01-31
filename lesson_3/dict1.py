dict_1 = {1: 'Moscow', 2: 'Piter', 3: 'Minsk'}
print(dict_1)

dict_2 = dict(Paris=4, Kiyv=5, Krakov=6)
print(dict_2)
print(type(dict_2))

print(dict_2.values())
print(dict_1.values())

print(dict_1.keys())

dict_2.update(Berlin=7)

print(dict_2)

print(dict_1.items())

dict_3 = dict.fromkeys([15, 20])
print(dict_3)

print(dict_2['Paris'])
