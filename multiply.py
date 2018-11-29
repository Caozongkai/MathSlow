mul_table = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
             [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
             [0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
             [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
             [0, 6, 12, 18, 24, 30, 36, 42, 48, 54],
             [0, 7, 14, 21, 28, 35, 42, 49, 56, 63],
             [0, 8, 16, 24, 32, 40, 48, 56, 64, 72],
             [0, 9, 18, 27, 36, 45, 54, 63, 72, 81]]

def multiply_naive(a, b):
	a = str(a)
    b = str(b)
    ans = 0
    for i, ac in enumerate(reversed(a)):
        for j, bc in enumerate(reversed(b)):
            ac = int(ac)
            bc = int(bc)
            ans += int(str(mul_table[ac][bc]) + ''.join(['0' for _ in range(i+j)]))
    return ans

#
def multiply_fast(a, b):
    neg = False
    if a < 0:
        neg = not neg
        a = -a
    if b < 0:
        neg = not neg
        b = -b
    if a < 10 and b < 10:
        ans = mul_table[a][b]
    elif a < 10:
        ans = sum([b for _ in range(a)])
    elif b < 10:
        ans = sum([a for _ in range(b)])
    else:
        a, b = str(a), str(b)

        m = max(int(len(a)/2), int(len(b)/2))

        a0, b0 = int(a[-m:]), int(b[-m:])

        a1, b1 = a[:-m], b[:-m]
        a1 = 0 if a1 =="" else int(a1)
        b1 = 0 if b1 == "" else int(b1)

        z0 = multiply_fast(a0, b0)
        z2 = multiply_fast(a1, b1)

        z1 = multiply_fast(a0-a1, b1-b0) + z0 + z2

        ans = int(str(z2) + ''.join(['0' for _ in range(m+m)])) + \
               int(str(z1) + ''.join(['0' for _ in range(m)])) + z0
    if neg:
        return -ans
    else:
        return ans
