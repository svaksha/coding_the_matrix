# Problem 0.8.5

def row(p, n):
    return [p + i for i in range(n)]

def next():
    cols = 15
    rows = 20
    return [[i + j for j in range(rows)] for i in range(cols)]