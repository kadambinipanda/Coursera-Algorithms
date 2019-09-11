# Uses python3
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(data):
    n = len(data)

    for s in range(n):
        for i in range(n-s-1):
            j = i + s + 1
            m, M = min_and_max(i, j)
            mins[i][j] = m
            maxs[i][j] = M
            
def min_and_max(i, j):
    m = sys.maxsize
    M = -sys.maxsize

    for k in range(i, j):
        a = evalt(maxs[i][k], maxs[k+1][j], operations[k])
        b = evalt(maxs[i][k], mins[k+1][j], operations[k])
        c = evalt(mins[i][k], maxs[k+1][j], operations[k])
        d = evalt(mins[i][k], mins[k+1][j], operations[k])

        m = min(m, a, b, c, d)
        M = max(M, a, b, c, d)

    return m, M

if __name__ == "__main__":
    data = input()
    operations = [op for op in data[1::2]]
    data = [int(num) for num in data[0::2]]

    mins = [[0 for _ in range(len(data))] for _ in range(len(data))]
    maxs = [[0 for _ in range(len(data))] for _ in range(len(data))]

    for i in range(len(data)):
        mins[i][i] = data[i]
        maxs[i][i] = data[i]
    
    get_maximum_value(data)
    print(maxs[0][len(data)-1])
