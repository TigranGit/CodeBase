import numpy as np


def conv(source, kernel, stride, padding, f):
    """ Convolution: https://proglib.io/p/convolution """
    if (
        len(source.shape) != 2
        or len(kernel.shape) != 2
        or kernel.shape[0] != kernel.shape[1]
        or kernel.shape[0] > min(source.shape)
    ):
        return "DimensionError"
    n, m = source.shape
    k = kernel.shape[0]
    source = np.pad(source, padding)

    n1 = ((n - k) // stride) + 1
    m1 = ((m - k) // stride) + 1
    result = np.empty((n1, m1), dtype=int)
    for i in range(n1):
        for j in range(m1):
            result[i, j] = f(
                np.sum(
                    source[i * stride : i * stride + k, j * stride : j * stride + k]
                    * kernel
                )
            )
    return result


if __name__ == "__main__":
    source = np.array([[1, 1, 2], [0, 1, 3], [1, 3, 0]])
    kernel = np.array([[1, 0], [0, 1]])
    f = lambda x: x ** 2
    result = conv(source, kernel, 1, 0, f)
    print(result)
