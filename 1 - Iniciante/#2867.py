# https://www.beecrowd.com.br/judge/pt/problems/view/2867

qtd = int(input())
for i in range(qtd):
    a, b = map(int, input().split())
    c = str(pow(a, b))
    print(len(c))
