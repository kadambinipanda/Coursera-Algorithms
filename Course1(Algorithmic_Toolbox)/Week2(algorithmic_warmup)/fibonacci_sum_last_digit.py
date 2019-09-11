# Uses python3
import sys

def fibonacci_sum_naive(n):
	arr = [0,1,1]
	last_digits = [0,1,2]
	pattern = [0,1,2]
	period = 0

	for _ in range(n):
		arr.append(arr[-1] + arr[-2])
		last_digits.append(sum(arr)%10)

		period += 1
		if last_digits[-3:] == pattern:
			break
	
	new_n = n%period if (period != 0 and n/period > 1) else n

	return last_digits[new_n]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))
