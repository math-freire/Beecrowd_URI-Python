
x, soma, entradas = 1, 0, 0
while x > 0:
    x = int(input())
    if x > 0:
        soma += x
        entradas += 1
print('%.2f' % (soma/entradas))


