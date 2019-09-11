# Uses python3
import sys

def optimal_weight(capacity, weights):
    rows = len(weights) + 1
    columns = capacity + 1
    arr = [[0 for i in range(columns)] for j in range(rows)]
    weights.insert(0, 0)

    for row in range(1, rows):
        for column in range(1, columns):
            arr[row][column] = arr[row-1][column]
            
            if weights[row] <= column:
                new = arr[row-1][column-weights[row]] + weights[row]

                if new > arr[row][column]:
                    arr[row][column] = new

    return arr[-1][-1]

if __name__ == '__main__':
    capacity, n = map(int, input().split())
    weights = list(map(int, input().split()))
    
    print(optimal_weight(capacity, weights))
