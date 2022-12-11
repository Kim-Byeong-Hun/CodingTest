# 11654번
a = input()
print(ord(a))

# 11720번
a = int(input())
b = input()
c = 0
for i in b:
    c += int(i)
print(c)

# 10809번
a = input()
b = [chr(i) for i in range(97,123)]
for i in b:
    print(a.find(i), end=' ')

# 2675번
import sys
a = int(input())
for i in range(a):
    c = ''
    b = sys.stdin.readline().rstrip().split()
    for j in b[1]:
        c += j * int(b[0])
    print(c)

# 1157번
a = input()
b = a.upper()
c = list(set(b))
d = []
for i in c:
    d += [b.count(i)]

e = sorted(d, reverse=True)
if len(e) <= 1:
    print(c[0])
elif e[0] == e[1]:
    print('?')
else:
    print(c[d.index(max(d))])

# 1152번
a = input().split()
print(len(a))

# 2908번
a = input().split()
c = []
for i in a:
    b = ''
    for j in i:
        b += j
    c.extend(b)
c.reverse()
print(max([int(c[0]+c[1]+c[2]),int(c[3]+c[4]+c[5])]))
# -------------------------------------------------------- #
a = input().split()
c = []
for i in a:
    b = ''
    for j in range(1,len(i)+1):
        b += i[-j]
    c += [b]
max(int(c[0]), int(c[1]))

# 5622번
a = ','.join(input().upper()).split(',')
b = [chr(i) for i in range(65,91)]
c = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
d = 0
for i in a:
    d += c[b.index(i)]
print(d)

# 2941번
a = input()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = []
for i in b:
    c += [a.count(i)]
    a = a.replace(i, ' ')
d = [i for i in a.split(' ') if i not in ' ']
e = ''
for i in d:
    e += i
print(sum(c) + len(e))

# 1316번 ☆☆☆☆☆☆☆☆☆☆☆
import re
a = int(input())
b = []
e = 0
for i in range(a):
    b.append(input())

for i in b:
    d = []
    for j in range(len(i)):
        if i[j] not in d:
            d.append(i[j]) # EX) d = ['h','a','p','y']
        else:
            if (j - d.index(i[j])) == 1:
                del d[d.index(i[j])]
                d.append(i[j])
        if len(i) == len(d):
            e += 1
print(e)
