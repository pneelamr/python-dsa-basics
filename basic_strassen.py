# Strassen's Algorithm: Divide-and-conquer matrix multiplication using 7 sub-multiplications instead of 8.
# Splits each matrix into four n/2 × n/2 quadrants; seven products (M1–M7) replace the naive eight.
# O(n^2.807) vs naive O(n³); matrices must be square with dimensions a power of 2 (pad with zeros if needed).

# Time: O(n^2) — iterates over all n×n element pairs once
# Space: O(n^2) — output matrix of same size as inputs
def matrix_add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(n)]

# Time: O(n^2) — iterates over all n×n element pairs once
# Space: O(n^2) — output matrix of same size as inputs
def matrix_sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(n)]

# Time: O(n^2) — builds four quadrant matrices each of size n/2 × n/2
# Space: O(n^2) — four output matrices together hold n^2 elements
def split(M):
    n = len(M)
    half = n // 2
    A11 = [row[:half] for row in M[:half]]
    A12 = [row[half:] for row in M[:half]]
    A21 = [row[:half] for row in M[half:]]
    A22 = [row[half:] for row in M[half:]]
    return A11, A12, A21, A22

# Time: O(n^2) — assembles n^2 elements from four n/2 × n/2 quadrants
# Space: O(n^2) — single output matrix of size n×n
def join(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom

# Time: O(n^2.807) — recurrence T(n)=7T(n/2)+O(n²); exponent log2(7) ≈ 2.807
# Space: O(n^2 log n) — O(n²) per recursion level across O(log n) levels
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)
    M1 = strassen(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen(matrix_add(A21, A22), B11)
    M3 = strassen(A11, matrix_sub(B12, B22))
    M4 = strassen(A22, matrix_sub(B21, B11))
    M5 = strassen(matrix_add(A11, A12), B22)
    M6 = strassen(matrix_sub(A21, A11), matrix_add(B11, B12))
    M7 = strassen(matrix_sub(A12, A22), matrix_add(B21, B22))
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_sub(matrix_add(M1, M3), M2), M6)
    return join(C11, C12, C21, C22)
