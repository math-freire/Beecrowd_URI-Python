# https://www.beecrowd.com.br/judge/en/problems/view/1087

while True:
    x1, y1, x2, y2 = map(int, input().split())
    # Stop condition
    if x1 == x2 == y1 == y2 == 0:
        break
    # Same position
    if x1 == x2 and y1 == y2:
        print('0')
    # Same line or column
    elif x1 == x2 or y1 == y2:
        print('1')
    # Diagonal (x1,y1) - (x2,y2) = (x3,y3) where |x3| == |y3|
    elif abs(x1-x2) == abs(y1-y2):
        print('1')
    else:
        print('2')
