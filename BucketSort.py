import math
import time
import random

def InsertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def bucketsort(A):
  code = hashing(A)
  buckets = [list() for _ in range(code[1])]
  for i in A:
    x = re_hashing(i,code)
    buck = buckets[x]
    buck.append(i)

  for bucket in buckets:
    InsertionSort(bucket)

  count = 0
  for b in range(len(buckets)):
    for v in buckets[b]:
      A[count] = v
      count += 1

def hashing(A):
  m = A[0]
  for i in range(1,len(A)):
    if (m < A[i]):
      m = A[i]
  result = [m,int(math.sqrt(len(A)))]
  return result

def re_hashing(i,code):
  return int(i / code[0] * (code[1] - 1))

print ("Best Case")

A = []
for i in range(1000):
  A.append(i)

START = time.clock()
bucketsort(A)
END = time.clock()
print((END-START)*1000)

print ("Average Case")

A = []
for i in range(1000):
  A.append(int(random.random()*1000))

START = time.clock()
bucketsort(A)
END = time.clock()
print((END-START)*1000)

print ("Worst Case")
A = []
for i in range(1000,0,-1):
  A.append(i)

START = time.clock()
bucketsort(A)
END = time.clock()
print((END-START)*1000)
