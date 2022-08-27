# https://www.beecrowd.com.br/judge/pt/problems/view/1047
# 7 8 9 10 -  O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
# 7 10 8 9 - O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
# 7 10 8 20 - 1h10
"""
hi, mi, hf, mf = map(int, input().split())

if hi == mi == hf == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hf < hi and mf < mi:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((24 + (hf-hi)), 60 + (mf-mi)))
elif hf > hi and mf > mi:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((hf-hi), (mf-mi)))
elif hf < hi and mf > mi:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((24 + (hf - hi)), mf - mi))
elif hf > hi and mf < mi:
    if hf - hi == 1:
        print('O JOGO DUROU 0 HORA(S) E {} MINUTO(S)'.format(60 + (mf-mi)))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((hf - hi), 60 + (mf-mi)))
elif hf == hi and mf > mi:
    print('O JOGO DUROU 0 HORA(S) E {} MINUTO(S)'.format((mf - mi)))
else:
    print('O JOGO DUROU 23 HORA(S) E {} MINUTO(S)'.format(60 + (mf-mi)))
"""

hi, mi, hf, mf = map(int, input().split())

hi = hi*60 + mi
hf = hf*60 + mf
t = hf - hi

if t <= 0:
    t += 24*60
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(t//60, t % 60))
else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(t // 60, t % 60))

