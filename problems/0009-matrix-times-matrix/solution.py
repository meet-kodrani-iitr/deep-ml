def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    m,n,l,p = len(a),len(a[0]),len(b),len(b[0])
    if n!=l:
        return -1
    c = [[0 for i in range(p)] for j in range(m)]
    for i in range(m):
        for k in range(p):
            for j in range(n):
                c[i][k]+=a[i][j]*b[j][k]
    return c