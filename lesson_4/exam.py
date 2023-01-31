first_str = input()

a = ''

b = ''

for idx in range(len(first_str)):

    if idx % 2 == 0:

        a += first_str[idx]

    else:
        b += first_str[idx]

print(first_str.strip(), end='\n\n\n')

print(a, b, sep='   ', end='!!!')
