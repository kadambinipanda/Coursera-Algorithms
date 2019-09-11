# Uses python3
import sys
import itertools


def get_knapsack(capacity, weights):
    rows, columns = len(weights) + 1, capacity + 1
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    weights.insert(0, 0)

    # Forward steps
    for row in range(1, rows):
        for column in range(1, columns):
            arr[row][column] = arr[row-1][column]

            if weights[row] <= column:
                new_value = arr[row-1][column-weights[row]] + weights[row]

                if new_value > arr[row][column]:
                    arr[row][column] = new_value

    # Backwards steps
    included_weights = []
    row, column = rows - 1, columns - 1
    while arr[row][column] != 0:
        if arr[row-1][column] != arr[row][column]:
            included_weights.append(weights[row])
            column -= weights[row]
            row -= 1
        else:
            row -= 1
    weights.remove(0)
    return included_weights

def shuffle(arr):
    arr = sorted(arr)

    for i in range(len(arr)//2):
        arr[i], arr[~i] = arr[~i], arr[i]

    return arr


def partition(arr, k=3):
    if sum(arr) % k != 0:
        return 0
    else:
        souveniers_per_person = sum(arr) // k

    arr = shuffle(arr)
    for _ in range(k):
        used_souveniers = get_knapsack(souveniers_per_person, arr)
        # print(arr, used_souveniers, sum(used_souveniers))

        if sum(used_souveniers) != souveniers_per_person:
            return 0

        for souvenier in used_souveniers:
            arr.remove(souvenier)

    return 1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(partition(arr))

