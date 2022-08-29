# https://www.beecrowd.com.br/judge/pt/problems/view/1019

s = int(input())
x = s - (s//3600) * 3600
print('{}:{}:{}'.format(s//3600, x // 60, s % 60))
