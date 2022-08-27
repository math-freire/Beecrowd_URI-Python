# https://www.beecrowd.com.br/judge/pt/problems/view/1021

v = float(input())
# 576.73
n100, n50, n20, n10, n5, n2, m1, m5, m25, m10, m05, m01 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

# Notas
if v // 100 > 0:
    n100 = v // 100
    v = v - ((v // 100) * 100)
if v // 50 > 0:
    n50 = v // 50
    v = v - ((v // 50) * 50)
if v // 20 > 0:
    n20 = v // 20
    v = v - ((v // 20) * 20)
if v // 10 > 0:
    n10 = v // 10
    v = v - ((v // 10) * 10)
if v // 5 > 0:
    n5 = v // 5
    v = v - ((v // 5) * 5)
if v // 2 > 0:
    n2 = v // 2
    v = v - ((v // 2) * 2)

v *= 100
# Moedas
if v // 100 > 0:
    m1 = v // 100
    v = v - ((v // 100) * 100)
if v // 50 > 0:
    m5 = v // 50
    v = v - ((v // 50) * 50)
if v // 25 > 0:
    m25 = v // 25
    v = v - ((v // 25) * 25)
if v // 10 > 0:
    m10 = v // 10
    v = v - ((v // 10) * 10)
if v // 5 > 0:
    m05 = v // 5
    v = v - ((v // 5) * 5)
if v // 1 > 0:
    m01 = v // 1
    v = v - ((v // 1) * 1)

print("""NOTAS:
{:.0f} nota(s) de R$ 100.00
{:.0f} nota(s) de R$ 50.00
{:.0f} nota(s) de R$ 20.00
{:.0f} nota(s) de R$ 10.00
{:.0f} nota(s) de R$ 5.00
{:.0f} nota(s) de R$ 2.00
MOEDAS:
{:.0f} moeda(s) de R$ 1.00
{:.0f} moeda(s) de R$ 0.50
{:.0f} moeda(s) de R$ 0.25
{:.0f} moeda(s) de R$ 0.10
{:.0f} moeda(s) de R$ 0.05
{:.0f} moeda(s) de R$ 0.01""".format(n100, n50, n20, n10, n5, n2, m1, m5, m25, m10, m05, m01))