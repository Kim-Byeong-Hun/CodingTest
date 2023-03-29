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
    b = []
    for j in i:
        b.append(j)
    b.reverse()
    c.append(''.join(b))
print(max([int(c[0]),int(c[1])]))

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

# 1316번
a = int(input())
b = []
for i in range(a):
    b.append(input())
for i in b:
    c = []
    d = 0
    for j in i:
        if j not in c:
            c.append(j)
        else:
            if c.index(j) == (len(c)-1):
                continue
            else:
                d += 1
    if d >= 1:
        a -= 1
print(a)

# 2444번
a = int(input())
for i in range(1, a+1):
    if i == a:
        break
    else:
        print(' '*(a-i) + '*'*(2*i-1))

for i in range(1, a+1):
    print(' ' * (i-1) + '*' * (2*a-i*2+1))

# 10812번
n, m = map(int, input().split())
baguni = [i for i in range(1,n+1)]

for _ in range(m):
    i,j,k = map(int, input().split())
    a = baguni[baguni.index(k):j]
    
    for _ in range(len(a)):
        if k <= j:
            b.append(k)
            a.remove(k)
        else:
            b.extend(a)
            break
        k += 1
    
    for idx in range(len(b)):
        baguni[i+idx-1] = b[idx]
    print(baguni)


a = [5 8 9 6 1 2 3 6 7 10]


# baguni에서 인덱스 i~j까지 추출 -> k부터 시작해서 j까지 채우고, 제일 낮은수부터 채우기

# 10988번
text = input()
text0 = []
for n in text:
    text0.append(n)

text1 = text0.copy()
text1.reverse()
if text0 == text1:
    print(1)
else:
    print(0)

# 25206번
a = 0
b = 0
submit = 0

for _ in range(20):
    subj, credit, rank = input().split()
    credit = float(credit)
    score = 0
    if rank == 'A+':
        score = 4.5
        a += score * credit
        b += credit
    elif rank == 'A0':
        score = 4.0
        a += score * credit
        b += credit
    elif rank == 'B+':
        score = 3.5
        a += score * credit
        b += credit
    elif rank == 'B0':
        score = 3.0
        a += score * credit
        b += credit
    elif rank == 'C+':
        score = 2.5
        a += score * credit
        b += credit
    elif rank == 'C0':
        score = 2.0
        a += score * credit
        b += credit
    elif rank == 'D+':
        score = 1.5
        a += score * credit
        b += credit
    elif rank == 'D0':
        score = 1.0
        a += score * credit
        b += credit
    elif rank == 'F':
        score = 0.0
        a += score * credit
        b += credit
    else:
        pass

print(round(a/b, 6))