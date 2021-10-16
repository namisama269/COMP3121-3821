"""
Operation on 2 sequences A and B
A = [a0,a1,...,an], B = [b0,b1,...,bm]
"""
def add(A, B):
    pass

def pmul(A, B):
    pass

def dot(A, B):
    pass

def concat(A, B):
    pass

def convolution(A, B):
    """
    Brute force linear convolution of 2 sequences
    """
    n = len(A)
    m = len(B)
    conv = [0] * (n+m-1)
    for i in range(n):
        for k in range(m):
            conv[i+k] += A[i]*B[k]
    return conv

if __name__ == "__main__":
    A = [1,2,1]
    B = [1,2,1]
    print(convolution(A,B))
