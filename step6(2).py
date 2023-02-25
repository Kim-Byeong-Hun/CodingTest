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
