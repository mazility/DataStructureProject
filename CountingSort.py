import time
import random


def sort(array, maxValue=None):
  if maxValue is None:
    maxValue = 0
    for i in range(0, len(array)):
      if array[i] > maxValue:
        maxValue = array[i]

  buckets = [0] * (maxValue + 1)
  sortedIndex = 0

  for i in range(0, len(array)):
    buckets[array[i]] += 1

  for i in range(0, len(buckets)):
    while (buckets[i] > 0):
      array[sortedIndex] = i
      sortedIndex += 1
      buckets[i] -= 1

  return array

print ("Best Case")

A = []
for i in range(1000):
  A.append(i)
START = time.clock()
sort(A)
END = time.clock()
print((END-START)*1000)

print ("Average Case")
A = []
for i in range(1000):
  A.append(int(random.random()*1000))
START = time.clock()
sort(A)
END = time.clock()
print((END-START)*1000)


print ("Worst Case")
A = []
for i in range(1000,0,-1):
  A.append(int(random.random()*2000))
START = time.clock()
sort(A)
END = time.clock()
print((END-START)*1000)
