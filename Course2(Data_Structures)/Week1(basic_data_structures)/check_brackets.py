# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    indexes = []
    for i, next in enumerate(text):
        if next in "([{":
        	opening_brackets_stack.append(next)
        	indexes.append(i + 1)

        if next in ")]}":
        	if len(opening_brackets_stack) == 0:
        		return i + 1
        	if not are_matching(opening_brackets_stack.pop(), next):
        		return i + 1
        	indexes.pop()

    return indexes[-1] if len(indexes) else -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print("Success" if mismatch == -1 else mismatch)


if __name__ == "__main__":
    main()
