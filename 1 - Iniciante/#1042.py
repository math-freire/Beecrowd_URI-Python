# https://www.beecrowd.com.br/judge/pt/problems/view/1042

a, b, c = map(int, input().split())
valores = [a, b, c]
maior, menor, central = a, a, 0

for i in range(3):
    for j in range(3):
        if valores[i] > valores[j]:
            maior = valores[i]
        if valores[i] < valores[j]:
            menor = valores[i]

