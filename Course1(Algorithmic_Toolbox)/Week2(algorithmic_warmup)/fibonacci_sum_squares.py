# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
	arr = [0,1,1]
	arr_sq = [0,1,1]
	last_digits = [0,1,2]
	pattern = [0,1,2]
	summ = 2
	period = 0

	for _ in range(n):
		arr.append(arr[-1] + arr[-2])
		arr_sq.append(arr[-1]**2)
		last_digits.append(sum(arr_sq)%10)

		period += 1
		if last_digits[-3:] == pattern:
			break
	
	new_n = n%period if (period != 0 and n/period > 1) else n

	return last_digits[new_n]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
