# while True:
#     a = list(map(int, input().split()))
#     if a == 0:
#         break
#     print(sum(a for i in range(a)))

while True:
    s = input()
    if s == '0':
        break
    print(sum(list(map(int, s))))
