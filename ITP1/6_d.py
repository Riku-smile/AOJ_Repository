n, m = map(int, input().split())
A = [[]for i in range(n)]
b = [0]*m

for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(m):
    b[i] = int(input())

for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j] * b[j]
    print(sum)
