# Uses python3
def calc_fib(n):
    arr = [0, 1]

    for i in range(1, n):
        arr.append(arr[-1] + arr[-2])
        
    return arr[n]

n = int(input())
print(calc_fib(n))
