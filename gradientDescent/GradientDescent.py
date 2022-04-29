import tqdm


def gradient_descent(x, y, learning_rate=0.001, iterations=10000):
    """
    returns the slope and the intercept of the line 
    @param x: np.array -> shape = (1,-1)
    @param y: np.array -> shape = (1,-1) 
    """
    # from y = mx + b
    m_ML = b_ML = 0
    n = len(x)
    for _ in tqdm(range(1, iterations+1)):

        y_predicted = m_ML * x + b_ML

        # cost or error -> mean squared error

        # error = (1/n) * sum(val**2 for val in (y-y_predicted))

        # partial derivative of y = mx + b
        # partial derivative of m is ∂/∂m = (2/n) * Σ -x(y - mx+b) # imp here mx+b refers to predicted
        # partial derivative of b is ∂/∂b = (2/n) * Σ - (y - mx+b) # imp here mx+b refers to predicted

        m_derivative = -(2/n)*sum(x*(y-y_predicted))
        b_derivative = -(2/n)*sum((y-y_predicted))

        # adjusting the weights

        m_ML -= learning_rate*m_derivative
        b_ML -= learning_rate*b_derivative

    return m_ML, b_ML
