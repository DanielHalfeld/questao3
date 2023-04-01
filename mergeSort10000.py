import random
import time
import copy
import sys
sys.setrecursionlimit(10000)
size2 = 10000
span = 1000000
threshold = 20

def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
	if last-first < threshold and first < last:
		quick_selection(A, first, last)
	elif first < last:
		middle = (first + last)//2
		merge_sort2(A, first, middle)
		merge_sort2(A, middle+1, last)
		merge(A, first, middle, last)

def merge(A, first, middle, last):
	L = A[first:middle]
	R = A[middle:last+1]
	L.append(999999999)
	R.append(999999999)
	i = j = 0

	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]

#PARTE DE TESTE
print("")
start_time = time.time()
print("Aleatório 1\n---------------------------------")

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
merge_sort(w)
print("Merge Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nAleatório 2\n---------------------------------")

start_time = time.time()
x = [random.randint(0, span) for a in range(0, size2)]
merge_sort(x)
print("Merge Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nOrdenado\n---------------------------------")

start_time = time.time()
merge_sort(w)
print("Merge Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nOrdenado Reverso\n---------------------------------")

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
merge_sort(w)
print("Merge Sort(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))