import random

def chance50(a,b):
    test = random.random()  # random float 0.0 <= x < 1.0
    if test < 0.5:
        return a
    else:
        return b