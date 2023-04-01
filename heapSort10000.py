import random
import time
import copy
import sys
sys.setrecursionlimit(10000)
size2 = 10000
span = 1000000
threshold = 20

def heapsort(a):
    heapify(a, len(a))
    end = len(a)-1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        sift_down(a, 0, end)

def heapify(a, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(a, start, count-1)
        start -= 1

def sift_down(a, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#PARTE DE TESTE
print("")
start_time = time.time()
print("Aleatório 1\n---------------------------------")

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
heapsort(w)
print("Heap Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nAleatório 2\n---------------------------------")

start_time = time.time()
x = [random.randint(0, span) for a in range(0, size2)]
heapsort(x)
print("Heap Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nOrdenado\n---------------------------------")

start_time = time.time()
heapsort(w)
print("Heap Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nOrdenado Reverso\n---------------------------------")

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
heapsort(w)
print("Heap Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))