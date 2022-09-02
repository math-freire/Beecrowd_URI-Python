# https://www.beecrowd.com.br/judge/pt/runs/code/29601063

valores = list(map(int, input().split()))

valores_c = valores.copy()  # Sem o copy iria mexer nas duas listas ao mesmo tempo
valores_c.sort()

for valor in valores_c:
    print(valor)

print("")

for valor in valores:
    print(valor)
