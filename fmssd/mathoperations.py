import numpy as np


# calculate the Euclidean distance
def euclidean_distance(list_ref, list_comp, vectors):
    distances = np.zeros(len(list_ref))
    for i in range(len(list_ref)):
        distances[i] = np.linalg.norm(vectors[list_comp[i]] - vectors[list_ref[i]])
    return distances


# drop insignificant columns from numpy array
def check_if_significant_np(data_in, thresh):
    """
    takes: numpy array, threshold
    returns: numpy array with insignificant columns removed
    """
    indices = np.nonzero(np.var(data_in, axis=1) > thresh)
    data_out = data_in[indices]
    return data_out, indices


# discrete fourier transform
def discrete_fourier_transform(y, time_step):
    """
    contains numpy's fft funtion numpy.fft.fft()
    takes: vector y, time step
    returns: fourier transformed y, frequency vector
    """
    y_ft = np.fft.fft(y).real
    freq = np.fft.fftfreq(len(y), d=time_step)
    return y_ft, freq


# correct data representation:
# the real part of each matrix column is contained in numpy array column 0, 2, 4, 6, ...
# the imaginary part of each matrix column is contained in numpy array column 1, 3, 5, 7, ...
# convert the array that was read as dtype=float into a dtype=complex array
def real_to_complex_matrix(matrix):
    """
    takes: matrix with real and imaginary parts in separate columns (m x n)
    returns: matrix with complex numbers (m/2 x n)
    """
    columns = matrix.shape[0] // 2
    rows = matrix.shape[1]
    matrix_new = np.zeros([columns, rows], dtype=complex)
    for i in range(0, columns):
        matrix_new[i] = matrix[2 * i] + 1j * matrix[2 * i + 1]
    return matrix_new


# autocorrelation of complex matrix containing psi(t)
def autocorrelation(matrix):
    """
    takes: complex matrix containing
           subsequent versions of a vector psi(t) (mxn)
    returns: autocorrelation of psi(t) (n)
    """
    n = matrix.shape[1]
    autocorr = np.zeros(n, dtype=complex)
    for t in range(n):
        autocorr[t] = np.sum(np.conj(matrix[:, 0]) * matrix[:, t])
    return autocorr
