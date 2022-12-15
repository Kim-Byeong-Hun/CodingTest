# 2738번
a,b = map(int, input().split())
c = []
d = []
for i in range(0, 2):
    for j in range(0, a):
        if i == 1:
            c.append(list(map(int, input().split())))
        else:
            d.append(list(map(int, input().split())))

for i in range(0, a):
    for j in range(0, b):
        print(c[i][j]+d[i][j], end=' ')
    print()

# 2566번
a = []
for i in range(0,9):
    a.append(list(map(int, input().split())))

b = []
c = []
for i in a:
    b.append(max(i))
    c.append(i.index(max(i))+1)

print(max(b))
print(b.index(max(b))+1, end=' ')
print(c[b.index(max(b))])

# 2563번
a = int(input())

b = []
for i in range(0,a):
    b.append(list(map(int, input().split())))

c = []
d = []
for i in b:
    c.append(i[0])
    d.append(i[1])

e = []
for i in c:
    for j in range(0, 10):
        e.append(i+j)
c

f = []
for i in d:
    for j in range(0,11):
        f.append(i+j)
(len(e) - len(list(set(e)))-1) * (len(f) - len(list(set(f)))-1)
