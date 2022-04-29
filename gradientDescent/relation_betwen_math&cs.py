import numpy as np
import pandas as pd

def gradient_descent(x,y,learning_rate = 0.004,iterations = 93):
    # from y = mx + b
    # ! remember for overflow if you have too many iterations
    m_ML = b_ML = 0
    n = len(x)
    for i in range(1,iterations+1):

        y_predicted = m_ML * x + b_ML


        error = (1/n) * sum(val**2 for val in (y-y_predicted))

        m_derivative = -(2/n)*sum(x*(y-y_predicted))
        b_derivative = -(2/n)*sum((y-y_predicted))

        m_ML -= learning_rate*m_derivative
        b_ML -= learning_rate*b_derivative

    return m_ML,b_ML

df = pd.read_csv('test_scores.csv',sep=',')
x = np.array(df.math)
y = np.array(df.cs)

m, b = gradient_descent(x,y)
print(int(m),int(b))

print(m*90+b)