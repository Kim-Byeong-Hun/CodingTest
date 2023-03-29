# 15596번
def solve(a):
    return sum(a)

# 4673번
def d():
    n = 1
    m = 1
    b = []
    while n <= 10000:
        a = str(n)
        k = 0
        for i in range(len(a)):
            k += int(a[i])
        b += [n + k]
        n += 1
    b = list(set(b))
    while m <= 10000:
        if m not in b:
            print(m)
        m += 1

d()

# 1065번
# 1000이하니깐 (첫째) - (둘째) == (둘째) - (셋째) 면 한수
a = int(input())
def hansu(n):
    a = 0
    while n >= 1:
        if len(str(n)) <= 2:
            a += 1
        else:
            if (int(str(n)[0]) - int(str(n)[1])) == (int(str(n)[1]) - int(str(n)[2])):
                a += 1
        n -= 1
    print(a)

hansu(a)

# 2743번
a = input()
print(len(a))

# 9086번
a = int(input())
for _ in range(a):
    text = input()
    print(text[0], end='')
    print(text[-1], end='')
    print()

# 11718번
while True:
    try:
        text = input()
        print(text)
    except EOFError:
        break

    