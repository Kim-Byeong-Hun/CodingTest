# 2738번
a,b = map(int, input().split())
c = []
for i in range(0, 2):
    for j in range(0, b):
        c.append(list(map(int, input().split())))

[x+y for x,y in zip(c)]
# 2566번

# 2563번