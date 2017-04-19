import time
import random

def radixsort(A):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    buckets = [list() for _ in range(RADIX)]
    for  i in A:
      tmp = i / placement
      buckets[int(tmp%RADIX)].append(i)
      if maxLength and tmp > 0:
        maxLength = False
    a = 0
    for b in range(RADIX):
      buck = buckets[b]
      for i in buck:
        A[a] = i
        a += 1
    placement *= RADIX



print ("Best Case")
A = []
for i in range(1000):
  A.append(int(random.random()*1000))

START = time.clock()
radixsort(A)
END = time.clock()
print((END-START)*1000)

print ("Worst Case")
A = []
for i in range(0,1000,+1):
  A.append(i)

START = time.clock()
radixsort(A)
END = time.clock()
print((END-START)*1000)

print ("Average Case")

A = []
for i in range(1000,0,-1):
  A.append(i)


START = time.clock()
radixsort(A)
END = time.clock()
print((END-START)*1000)
