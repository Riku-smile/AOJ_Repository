while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    sum = m + f
    if m == -1 or f == -1:
        print('F')
    elif sum >= 80:
        print('A')
    elif 80 > sum >= 65:
        print('B')
    elif 65 > sum >= 50:
        print('C')
    elif 50 > sum >= 30:
        if r >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')
