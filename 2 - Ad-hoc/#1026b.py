while True:
    try:
        a, b = map(int, input().split())
        print(a ^ b)
    except EOFError:
        break
# This method uses a binary operator with a exclusive or calculation.
# It isn't enough to make proper calculations, but it's enough (and actually what we need) to this exercise
