# https://www.beecrowd.com.br/judge/pt/problems/view/1038

cod, qtd = map(int, input().split())

if cod == 1:
    t = 4 * qtd
elif cod == 2:
    t = 4.5 * qtd
elif cod == 3:
    t = 5 * qtd
elif cod == 4:
    t = 2 * qtd
elif cod == 5:
    t = 1.5 * qtd

print('Total: R$ {:.2f}'.format(t))
