# 10807번
a = int(input())
b = list(map(int, input().split()))
c = int(input())
print(b.count(c))

# 10871번
import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
c = []
for i in range(a[0]):
    if b[i] < a[1]:
        print(b[i], end=' ')
    
# 10818번
import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))
print(str(min(b)) + ' ' + str(max(b)))

# 2562번
import sys
a = []
for i in range(9):
    a += [int(sys.stdin.readline().rstrip())]
print(max(a))
print(a.index(max(a))+1)

# 5597번
import sys
a = []
for i in range(28):
    a += [int(sys.stdin.readline().rstrip())]
    a.sort()
for i in range(1, 31):
    if i not in a:
        print(i)

# 3052번
import sys
a = []
for i in range(10):
    a += [int(sys.stdin.readline().rstrip()) % 42]
print(len(list(set(a))))

# 1546번
import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))
c = []
for i in range(len(b)):
    c += [b[i]/max(b)*100]
print(sum(c) / len(c))

# 8958번
import sys
a = int(input())
for i in range(a):
    b = sys.stdin.readline().rstrip()
    