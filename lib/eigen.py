import numpy as np


def real_eigenvals(A):
    Ak = np.copy(A)
    n = Ak.shape[0]
    for _ in range(2000):
        s = Ak[-1, -1]
        si = s * np.eye(n)
        Q, R = qr(np.subtract(Ak, si))
        Ak = np.add(R @ Q, si)
    eigens = []
    i = 0
    while i < n - 1:
        if np.isclose(Ak[i + 1, i], 0, atol=1e-6):
            eigens.append(Ak[i, i])
            i += 1
        else:
            i += 2
    if len(eigens) != n:
        eigens.append(Ak[-1, -1])
    return np.array(eigens)


def upper_hessenberg(A):
    Ak = np.copy(A)
    n = Ak.shape[0]
    for j in range(n - 2):
        for i in range(n - 1, j + 1, -1):
            G = np.eye(n)
            theta = np.arctan2(Ak[i, j], Ak[i - 1, j])
            G[i - 1, i - 1] = np.cos(theta)
            G[i, i - 1] = -np.sin(theta)
            G[i - 1, i] = np.sin(theta)
            G[i, i] = np.cos(theta)
            Ak = G @ Ak @ G.T
    return Ak


def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = householder(A[i:, i])
        Q = Q @ H
        A = H @ A
    return Q, A


def householder(a):
    u = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    u[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / (u @ u)) * u[:, None] @ u[None, :]
    return H


def eigval2x2(A):
    a = 1
    b = (-A[0, 0]) + (-A[1, 1])
    c = (-A[0, 0]) * (-A[1, 1]) - A[1, 0] * A[0, 1]
    return np.roots([a, b, c])


# if __name__ == '__main__':
#     A = np.random.rand(20, 20) * 100
#     print(np.sort_complex(eigenvals(A)))
#     print(np.sort_complex(np.linalg.eig(A)[0]))
