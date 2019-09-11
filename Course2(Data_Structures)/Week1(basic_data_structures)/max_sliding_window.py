# python3

class Stack():
	def __init__(self):
		self.s = []
		self.maximums = []

	def push(self, value):
		if self.s:
			self.maximums.append(max(self.maximums[-1], value))
		else:
			self.maximums.append(value)
		self.s.append(value)

	def pop(self):
		if self.s:
			self.maximums.pop(-1)
			return self.s.pop(-1)
		else:
			return None

	def top(self):
		return self.s[-1] if self.s else None

	def maximum(self):
		if self.maximums:
			return self.maximums[-1]
		else:
			return -1


class Queue:

	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def push(self, value):
		self.s2.push(value)

	def pop(self):
		if self.s1.top() is None:
			while self.s2.top() is not None:
				self.s1.push(self.s2.pop())
		return self.s1.pop()

	def maximum(self):
		return max(self.s1.maximum(), self.s2.maximum())


def max_sliding(seq, m):
	q = Queue()
	maximums = []

	for x in seq[:m]:
		q.push(x)
	maximums.append(q.maximum())

	for x in seq[m:]:
		q.pop()
		q.push(x)
		maximums.append(q.maximum())

	return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding(input_sequence, window_size))))
