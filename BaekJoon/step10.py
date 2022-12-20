# 2750번
a = int(input())

b = []
for i in range(0,a):
    b.append(int(input()))

c = sorted(b)

for i in c:
    print(i)

# 2587번
a = []
for i in range(0,5):
    a.append(int(input()))

b = sorted(a)

print(int(sum(b)/5))
print(b[2])

# 25303번
a, b = map(int, input().split())
c = list(map(int, input().split()))
d = sorted(c, reverse=True)
print(d[:b][-1])

# 2751번
import sys
a = int(input())
b = []
for i in range(0,a):
    b.append(int(sys.stdin.readline().rstrip()))

c = sorted(b)
for i in c:
    print(i)

# 10989번
import sys
a = int(input())
b = [0 for i in range(10001)]
for i in range(a):
    c = int(sys.stdin.readline().rstrip())
    b[c] += 1

for i in range(len(b)):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)

# 2108번
import sys
a = int(input())
b = []
for i in range(a):
    b.append(int(sys.stdin.readline().rstrip()))

print(round(sum(b)/a)) # 산술평균

c = sorted(b)
print(c[a//2]) # 중앙값

from collections import Counter
d = Counter(c)
if len(d) >= 2:
    if d.most_common()[0][1] == d.most_common()[1][1]:
        print(d.most_common()[1][0])
    else:
        print(d.most_common()[0][0])
else:
    print(d.most_common()[0][0])

print(c[-1]-c[0]) # 범위

# 1427번
a = input()
b = []
for i in a:
    b.append(i)
b.sort(reverse=True)
c = ""
for i in b:
    c+=i
print(c)

# 11650번
a = int(input())
b = []
for i in range(a):
    b.append(list(map(int, input().split())))
b.sort(key=lambda x:(x[0], x[1]))
for i in b:
    for j in i:
        print(j, end= ' ')
    print()
    
# 11651번
a = int(input())
b = []
for i in range(a):
    b.append(list(map(int, input().split())))
b.sort(key=lambda x:(x[1], x[0]))
for i in b:
    for j in i:
        print(j, end= ' ')
    print()

# 1181번
a = int(input())
b = []
for i in range(a):
    b.append(input())
c = list(set(b))
d = sorted(c)
d.sort(key=lambda x:(len(x)))
for i in d:
    print(i)

# 10814번
a = int(input())
b = []
for i in range(a):
    b.append(input().split())
b.sort(key=lambda x:int(x[0]))
for i in b:
    for j in i:
        print(j, end=' ')
    print()

# 18870번
import sys
a = int(input())
b = list(map(int, sys.stdin.readline().rstrip().split()))
c = list(set(b))
c.sort()
d = dict()
for i in range(len(c)):
    d[c[i]] = i

for i in b:
    print(d[i], end=' ')
    