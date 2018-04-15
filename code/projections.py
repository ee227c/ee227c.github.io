"""Common projections."""


import numpy as np


def simplex_projection(vector):
    """Projection onto the unit simplex.
    
        Source: https://gist.github.com/daien/1272551

    Parameters:
    -----------
        vector: array  
            Vector to be projected onto simplex.

    Returns:
    --------
        Vector in the unit simplex
    """
    if np.sum(vector) <=1 and np.alltrue(vector >= 0):
        return vector 
    # get the array of cumulative sums of a sorted (decreasing) copy of v
    u = np.sort(vector)[::-1]
    cssv = np.cumsum(u)
    # get the number of > 0 components of the optimal solution
    rho = np.nonzero(u * np.arange(1, len(u)+1) > (cssv - 1))[0][-1]
    # compute the Lagrange multiplier associated to the simplex constraint
    theta = (cssv[rho] - 1) / (rho + 1.0)
    # compute the projection by thresholding v using theta
    return np.maximum(s-theta, 0)


def nuclear_projection(matrix):
    """Projection onto nuclear norm unit ball.

    Parameters:
        matrix: two-dimensional array
            Matrix to be projected onto nuclear norm unit ball.

    Returns:
        Matrix in the unit ball of the nuclear norm.
    """
    U, s, V = np.linalg.svd(matrix, full_matrices=False)
    s = simplex_projection(s)
    return U.dot(np.diag(s).dot(V))
