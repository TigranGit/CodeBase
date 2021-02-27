import numpy as np


def padding(a, n1, m1):
    """
        Given a 2D numpy array 'a' of sizes n×m.
        You need to pad the matrix with 0s
        so that the dimensions of the matrix become (n+2n1)×(m+2m1)
    """
    if len(a.shape) != 2:
        return "DimensionError"
    n, m = a.shape
    new_arr = np.zeros((n + 2*n1, m + 2*m1))
    new_arr[n1 : n+n1, m1 : m+m1] = a
    return new_arr


def rand_split(a, k):
    """
        Given a numpy matrix 'a' of sizes m×n and a number 'k' in range [0,1].
        The rows of 'a' should be randomly divided into parts in the ratio k:(1-k).
        (If the parts are not integers, round them)
    """
    if len(a.shape) != 2:
        return "DimensionError"
    b = a.copy()
    np.random.shuffle(b)
    nrows = round(b.shape[0] * k)
    return b[:nrows], b[nrows:]


def rand_rows_cols(a, k, q):
    """
        Given a numpy matrix 'a' of sizes m×n and the numbers 'k' and 'q' in the range [0,1].
        You need to randomly select the 'k' part of the rows of 'a' (can be repeated)
        and the 'q' part of their columns (should not be repeated).
    """
    if len(a.shape) != 2:
        return "DimensionError"
    idx = np.random.randint(len(a), size=round(len(a)*k))
    result = a[idx, :]
    idx = np.random.default_rng().choice(result.shape[1], size=round(result.shape[1]*q))
    return result[:, idx]


def dist_mat(a, b, p):
    """
        Given 2D numpy arrays 'a' and 'b' of sizes n×m and k×m respectively
        and one natural number 'p'. You need to find the distance(Euclidean)
        of the rows of the matrices 'a' and 'b'. Fill the results in the k×n matrix.
    """
    if len(a.shape) != 2 or len(b.shape) != 2 or a.shape[1] != b.shape[1]:
        return "DimensionError"
    return np.power(np.power(np.abs(b[:,np.newaxis]-a), p).sum(axis=2), 1/p)
