W = int(input("배낭 용량을 입력 하세요 : "))

items = ["노트북","카메라","책","옷","휴대용 충전기"]
wt = [3,1,2,2,1]
value = [12,10,6,7,4]

n = len(items)
A = [[0]*(W+1) for _ in range(n+1)]

for i in range(1,n+1):
    for w in range(1,W+1):
        if wt[i-1] > w:
            A[i][w] = A[i-1][w]
        else:
            A[i][w] = max(A[i-1][w],
                          value[i-1] + A[i-1][w-wt[i-1]])

res = A[n][W]
w = W
selected = []

for i in range(n,0,-1):
    if res != A[i-1][w]:
        selected.append(items[i-1])
        res -= value[i-1]
        w -= wt[i-1]

print("총 만족도:", A[n][W])
print("선택된 물건:", selected[::-1])