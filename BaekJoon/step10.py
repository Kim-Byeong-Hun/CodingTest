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

# 2108번 ☆☆☆☆☆☆☆☆☆☆
import sys
a = int(input())
b = []
for i in range(a):
    b.append(int(sys.stdin.readline().rstrip()))

print(int(sum(b)/a)) # 산술평균

c = sorted(b)
print(c[a//2]) # 중앙값

d = []
for i in c:
    d.append(c.count(i))
e = []
for i in range(len(d)):
    if d[i] == max(d):
        e.append(c[i])
if len(e) >= 2:
    print(e[1]) # 최빈값

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