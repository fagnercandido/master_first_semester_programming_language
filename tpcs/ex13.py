import random
import time

lista = []
for i in range(10000):
    lista.append(random.randint(-100000,99999))

start_time = time.time()
lista.sort()
print("--- %s seconds ---" % (time.time() - start_time))

lista2 = []
for i in range(10000):
    lista2.append(random.randint(-100000,99999))

start_time2 = time.time()
for i in lista2:
    pass
print("--- %s seconds ---" % (time.time() - start_time2))