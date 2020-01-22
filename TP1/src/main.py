 # Addition de deux matrices
def mat_add(a,b):
    N = len(a)

    c = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):    
        for j in range(N):
            c[i][j] = a[i][j] + b[i][j]

    return c

# Soustraction de deux matrices
def mat_sub(a,b):
    N = len(a)

    c = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):    
        for j in range(N):
            c[i][j] = a[i][j] - b[i][j]

    return c

# Multiplication conventionnelle de deux matrices
def mat_mul_conventionnal(a, b):
    
    N = len(a)
    c = [[0 for i in range(N)] for j in range(N)] 

    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += a[i][k] * b[k][j]

    return c

# Multiplication diviser-pour-regner de deux matrices
def mat_mul_strassen(a, b, threshold):
    if len(a) > threshold :
        N = len(a)/2
        a00 = [[0 for i in range(N)] for j in range(N)]
        a01 = [[0 for i in range(N)] for j in range(N)]
        a10 = [[0 for i in range(N)] for j in range(N)]
        a11 = [[0 for i in range(N)] for j in range(N)]

        b00 = [[0 for i in range(N)] for j in range(N)]
        b01 = [[0 for i in range(N)] for j in range(N)]
        b10 = [[0 for i in range(N)] for j in range(N)]
        b11 = [[0 for i in range(N)] for j in range(N)]

        for i in range(N):
            for j in range(N):
                a00[i][j] = a[i][j]
                a01[i][j] = a[i][j + N]
                a10[i][j] = a[i + N][j]
                a11[i][j] = a[i + N][j + N]

                b00[i][j] = b[i][j]
                b01[i][j] = b[i][j + N]
                b10[i][j] = b[i + N][j]
                b11[i][j] = b[i + N][j + N]

        m1 = mat_mul_strassen(mat_sub(mat_add(a10, a11), a00), mat_add(mat_sub(b11, b01), b00), threshold)
        m2 = mat_mul_strassen(a00, b00, threshold)
        m3 = mat_mul_strassen(a01, b10, threshold)
        m4 = mat_mul_strassen(mat_sub(a00, a10), mat_sub(b11, b01), threshold)
        m5 = mat_mul_strassen(mat_add(a10, a11), mat_sub(b01, b00), threshold)
        m6 = mat_mul_strassen(mat_add(mat_sub(a01, a10), mat_sub(a00, a11)), b11, threshold)
        m7 = mat_mul_strassen(a11, mat_sub(mat_add(b00, b11), mat_sub(b01, b10)), threshold)

        c00 = mat_add(m2, m3)
        c01 = mat_add(mat_add(m1, m2), mat_add(m5, m6))
        c10 = mat_add(mat_add(m1, m2), mat_sub(m4, m7))
        c11 = mat_add(mat_add(m1, m2), mat_add(m4, m5))

        c = [[0 for i in range(len(a))] for j in range(len(a))]

        for i in range(N):
            for j in range(N):
                c[i][j] = c00[i][j]
                c[i][j + N] = c01[i][j]
                c[i + N][j] = c10[i][j]
                c[i + N][j + N] = c11[i][j]
        
        return c

    else :
        m1 = (a[1][0] + a[1][1] - a[0][0]) * (b[1][1] - b[0][1] + b[0][0])
        m2 = a[0][0] * b[0][0]
        m3 = a[0][1] * b[1][0]
        m4 = (a[0][0] - a[1][0]) * (b[1][1] - b[0][1])
        m5 = (a[1][0] + a[1][1]) * (b[0][1] - b[0][0])
        m6 = (a[0][1] - a[1][0] + a[0][0] - a[1][1]) * b[1][1]
        m7 = a[1][1] * (b[0][0] + b[1][1] - b[0][1] - b[1][0])

        return [[m2 + m3, m1 + m2 + m5 + m6], [m1 + m2 + m4 - m7, m1 + m2 + m4 + m5]]
    

# matrix1 = [[5,-2, 4, 5], [7,3, 8, -3], [2, -5, 3, 10], [6, -6, 2, 1]]
matrix1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
matrix2 = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

print(mat_mul_strassen(matrix1, matrix2, 2))