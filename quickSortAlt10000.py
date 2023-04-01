import random
import time
import sys
sys.setrecursionlimit(10000)
size2 = 10000
span = 1000000
threshold = 20

def quickSort(lista, k):
    if len(lista) <= k:
        return insertion_sort(lista)
    else:
        pivo = lista[len(lista)//2]
        esquerda = []
        direita = []
        meio = []
        for x in lista:
            if x < pivo:
                esquerda.append(x)
            elif x == pivo:
                meio.append(x)
            else:
                direita.append(x)
        return quickSort(esquerda, k) + meio + quickSort(direita, k)

def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j-1] > lista[j]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
    return lista

print("")
start_time = time.time()
print("Aleatório 1\n---------------------------------")

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
quickSort(w, w[0])
print("Quick Sort Alterado(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nAleatório 2\n---------------------------------")

start_time = time.time()
x = [random.randint(0, span) for a in range(0, size2)]
quickSort(x, x[0])
print("Quick Sort Alterado(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nOrdenado\n---------------------------------")

start_time = time.time()
quickSort(w, w[0])
print("Quick Sort Alterado(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
print("\nOrdenado Reverso\n---------------------------------")

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
quickSort(w, w[0])
print("Quick Sort Alterado(tamanho="+ str(size2)+"): ", round(time.time() - start_time, 11))