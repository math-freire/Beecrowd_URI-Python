# https://www.beecrowd.com.br/judge/pt/problems/view/1042

a, b, c = map(int, input().split())
v = [a, b, c]
maior, menor, central = a, a, 0

for i in range(2):
    if v[i] > v[i+1]:
        maior = v[i]
    elif v[i] < v[i+1]:


print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(menor, central, maior, a, b, c))
