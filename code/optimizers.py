"""Common optimizers."""


def gradient_descent(init, steps, grad, proj=lambda x: x, num_to_keep=None):
    """Projected gradient descent.
    
    Parameters
    ----------
        initial : array
            starting point
        steps : list of floats
            step size schedule for the algorithm
        grad : function
            mapping arrays to arrays of same shape
        proj : function, optional
            mapping arrays to arrays of same shape
        num_to_keep : integer, optional
            number of points to keep
        
    Returns
    -------
        List of points computed by projected gradient descent. Length of the
        list is determined by `num_to_keep`.
    """
    xs = [init]
    for step in steps:
        xs.append(proj(xs[-1] - step * grad(xs[-1])))
        if num_to_keep:
          xs = xs[-num_to_keep:]
    return xs


def conditional_gradient(initial, steps, oracle, num_to_keep=None):
    """Conditional gradient.
    
        Conditional grdient (Frank-Wolfe) for first-order optimization.
    
    Parameters:
    -----------
        initial: array,
            initial starting point
        steps: list of numbers,
            step size schedule
        oracle: function,
            mapping points to points, implements linear optimization 
            oracle for the objective.
    
    Returns:
    --------
        List of points computed by the algorithm.
    """
    xs = [initial]
    for step in steps:
        xs.append(xs[-1] + step*(oracle(xs[-1])-xs[-1]))
        if num_to_keep:
          xs = xs[-num_to_keep:]
    return xs
