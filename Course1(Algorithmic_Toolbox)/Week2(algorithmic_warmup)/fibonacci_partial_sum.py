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


def fibonacci_partial_sum_naive(from_, to):
    size = to-from_
    summ = 0
    sums = []
    period = 0

    for i in range(3):
        summ += get_fibonacci_huge_naive(from_+i, 10)
        sums.append(summ%10)


    for i in range(from_+3, to+1):
        summ += get_fibonacci_huge_naive(i, 10)
        sums.append(summ%10)

        period += 1
        if sums[-3:] == sums[:3]:
            break

    new_n = size%period if (period != 0  and size/(period+3) > 1) else size
    
    return sums[new_n]
        

if __name__ == '__main__':
    #input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
