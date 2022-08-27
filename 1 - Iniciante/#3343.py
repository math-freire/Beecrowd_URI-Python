# https://www.beecrowd.com.br/judge/pt/problems/view/3343

# 3 20
# MPG     =  2 muralhas
# 3 8 10

numT, altM = map(int, input().split())
t = input().strip().upper()  # numT = len(titans)
p, m, g = map(int, input().split())

# intT terá somente os valores da altura de cada titan, em ordem
titans = list(t)  # Separada 'MPG' em ['M', 'P', 'G']

intT = []
for t in titans:
    if t == 'P':
        intT.append(p)
    elif t == 'M':
        intT.append(m)
    elif t == 'G':
        intT.append(g)
# Para ['M', 'P', 'G'] e p,m,g=[3,8,10], teremos intT = [8, 3 , 10]

numMuralhas = 1
novasMuralhas = altM
muralhasQuebradas = [0]

for titan in intT:
    for x in muralhasQuebradas:
        if titan <= x:
            titan = 0
    if novasMuralhas >= titan:
        novasMuralhas -= titan
    else:  # Pulou a muralha
        if p <= novasMuralhas < m:
            muralhasQuebradas.append(novasMuralhas)
        numMuralhas += 1
        novasMuralhas = altM
        novasMuralhas -= titan

print(numMuralhas)
