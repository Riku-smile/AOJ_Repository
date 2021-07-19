# while True:
#     r, c = map(int, input().split())
#     SS = [[]for j in range(c+1)]

#     for i in range(r+1):
#         SS[i] = list(map(int, input().split()))
#         count = 0
#         for j in range(c):
#             count += SS[i][j]
#             SS[i].append(count)

r, c = map(int, input().split())
SS = [[0]*c for _ in range(r+1)]

for i in range(r):
    SS[i] = list(map(int, input().split()))
for j in range(c):
    for i in range(r):
        SS[r][j] += SS[i][j]
for i in range(r+1):
    ans = 0
    for j in range(c):
        ans += SS[i][j]
        print(SS[i][j], end=' ')
    print(ans)
