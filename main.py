
from random import randint
count = 0
L = []
for i in range(50):
    L.append(randint(1,100))
    count+=1
print(L)
print(count)

L.sort()
print(L)
print('Two smallest: ', L[0], L[1])
print('Two largest: ', L[-1], L[-2])
#
# a = len(L)
# print(a)