# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    arr = [0,1,1]
    reminders = [0,1,1]
    pattern = [0,1,1]
    period = 0

    for _ in range(n):
        arr.append(arr[-1] + arr[-2])
        reminders.append(arr[-1]%m)

        period += 1
        if reminders[-3:] == pattern:
            break

    new_n = n%period if (period != 0 and n/period > 1) else n

    return arr[new_n]%m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
