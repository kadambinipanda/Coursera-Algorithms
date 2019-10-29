# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  string = pattern + '$' + text
  prefixes = [0] * len(string)

  for i in range(1, len(string)):
    prev = prefixes[i-1]

    while prev > 0 and string[prev] != string[i]:
      prev = prefixes[prev-1]
    else:
      if string[prev] == string[i]:
        prefixes[i] = prev + 1
      else:
        prefixes[i] = 0

  for j in range(len(pattern), len(prefixes)):
    if prefixes[j] == len(pattern):
      result.append(j-2*len(pattern))

  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

