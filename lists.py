a = [2,-9,5,6,11,-55,-63,-7,15,17]
min_1 = min(a)
a.remove(min_1)
min_2 = min(a)
print(min_1, min_2)


from random import randint
N = 15
b = [randint(-50, 250) for j in range(N)]
print(b)
c = -6
d = 7
i = 0
m = N
while i < m:
    if c <= b[i] <= d:
        b.pop(i)
        m -= 1
    else:
        i += 1
for i in range(m,N):
    b.append(0)
print(b)
