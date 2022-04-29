import numpy as np
from tqdm import tqdm
from GradientDescent import gradient_descent


def test():
    x = np.array([2, 3, 4, 5, 6])
    y = []
    m = 3
    c = 8
    for val in x:
        y_ = m*val + c
        y.append(y_)
    y = np.array(y)
    print(gradient_descent(x, y))


def main():
    test()

    # df = pd.read_csv('test_scores.csv', sep=',')
    # x = np.array(df.math)
    # y = np.array(df.cs)
    # print(gradient_descent(x, y))
    # model = linear_model.LinearRegression()
    # x = x.reshape(-1, 1)
    # y = y.reshape(-1, 1)
    # print(x)
    # model.fit(x,y)
    # print(model.coef_)
    # print(model.intercept_)


if __name__ == '__main__':
    main()
