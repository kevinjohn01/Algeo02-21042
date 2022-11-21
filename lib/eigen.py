import numpy as np


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


def eigens(A):
    Ak = upper_hessenberg(A)
    Q, _ = qr(Ak)
    E = Q.T @ Ak @ Q
    U = Q
    for _ in range(1000):
        Q, _ = qr(E)
        E = Q.T @ E @ Q
        U = U @ Q
    return np.diag(E), U
