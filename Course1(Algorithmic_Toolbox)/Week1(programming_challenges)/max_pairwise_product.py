# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    
    m1 = 0
    for i in range(n):
        if numbers[i] > numbers[m1]:
            m1 = i

    m2 = m1-1
    for i in range(n):
    	if i != m1 and numbers[i] > numbers[m2]:
    		m2 = i

    return numbers[m1]*numbers[m2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
        
