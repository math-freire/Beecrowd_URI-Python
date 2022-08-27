
a, b, c = map(int, input().split())

res = (a+b+abs(a-b)) / 2

if res < c:
    print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(res))
