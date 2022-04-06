import numpy as np


def f(A, B, X):
    """
    Given three matrices A, X and B, compute their matrix-product, AX + B.

    Args:
        A (np.ndarray): The first matrix,
        X (np.ndarray): The second matrix. X.shape[0] must be identical to A.shape[1]
        B (np.ndarray): The third matrix. B.shape[0] must be identical to A.shape[0] and B.shape[1] must be identical to X.shape[1]

    Returns:
        C (np.ndarray): The matrix-product AX + B. shape = (A.shape[0], B.shape[1])
    """
    return A @ X + B
