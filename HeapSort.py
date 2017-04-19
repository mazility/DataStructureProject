import time
import random

def Parent(i):
    return i/2
def Left(i):
    return i*2
def Right(i):
    return (i*2)+1

def max_heapify(A, i, heap_size):
  l = Left(i)
  r = Right(i)
  if l <= heap_size and A[l] > A[i]:
    largest = l
  else:
    largest = i
  if r <= heap_size and A[r] > A[largest]:
    largest = r
  if i != largest:
    A[i], A[largest] = A[largest], A[i]
    max_heapify(A, largest, heap_size)

def build_max_heap(A, heap_size):
  for i in range(int(heap_size/2) - 1, 0, -1):
    max_heapify(A, i, heap_size)

def HeapSort(A, heap_size):
  build_max_heap(A, heap_size)
  for i in range(len(A[1:]), 1, -1):
    A[1], A[i] = A[i], A[1]
    heap_size = heap_size - 1
    max_heapify(A, 1, heap_size)

print ("Worst Case")

A = []
for i in range(1000):
  A.append(i)

heap_size = len(A[1:])
START = time.clock()
HeapSort(A, heap_size)
END = time.clock()
print((END-START)*1000)

print ("Average Case")
A = []
for i in range(1000):
  A.append(int(random.random()*1000))

heap_size = len(A[1:])
START = time.clock()
HeapSort(A, heap_size)
END = time.clock()
print((END-START)*1000)

print ("Best Case")
A = []
for i in range(1000,0,-1):
  A.append(i)

heap_size = len(A[1:])
START = time.clock()
HeapSort(A, heap_size)
END = time.clock()
print((END-START)*1000)
