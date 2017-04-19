import time
import random
from random import randrange

def Partition(A,p,r):
    pivot = int((p+r)/2)
    A[pivot],A[r] = A[r],A[pivot]
    i = p
    for j in range(p,r):
        if A[j] < A[r]:
            A[j],A[i] = A[i],A[j]
            i += 1
    A[i],A[r] = A[r],A[i]
    return i

def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

print ("Best Case")
A = []
for i in range(0,10000,+1):
  A.append(i)
START = time.time()
QuickSort(A,0,len(A[1:]))
END = time.time()
print((END-START)*1000)

print ("Worst Case")

A = []
for i in range(10000):
  A.append(int(random.random()*100))
START = time.time()
QuickSort(A,0,len(A[1:]))
END = time.time()
print((END-START)*1000)

print ("Average Case")

A = []
for i in range(10000,-1,-1):
  A.append(i)
START = time.time()
QuickSort(A,0,len(A[1:]))
END = time.time()
print((END-START)*1000)
