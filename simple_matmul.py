import numpy as np
import time


def f(A, B):
    """
    Given two matrices A and B, compute their matrix-product, AB.

    Args:
        A (np.ndarray): The first matrix, 
        B (np.ndarray): The second matrix. B.shape[0] must be identical to A.shape[1] 

    Returns:
        C (np.ndarray): The matrix-product AB. shape = (A.shape[0], B.shape[1])
    """
    return A @ B