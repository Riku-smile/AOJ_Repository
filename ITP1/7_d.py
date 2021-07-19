# n, m, l = map(int, input().split())

# a = [[0]*m for _ in range(n)]
# b = [[0]*l for _ in range(m)]
# c = [[0]*l for _ in range(n)]

# for i in range(n+m):
#     a[i] = list(map(int, input().split()))
#     if i >= (n-1):
#         b[i-n-1] = list(map(int, input().split()))


# for i in range(n):
#     for j in range(m):
#         for k in range(l):
#             c[i][j] += a[i][j] * b[j][k]
#             print(c[i][j])
#         print()
#     print()

n, m, l = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
c = [[0]*l for _ in range(n)]


for i in range(n):
    for k in range(l):
        if k != 0:
            print(' ', end='')
        for j in range(m):
            c[i][k] += a[i][j] * b[j][k]

        print(c[i][k], end='')
    print()
