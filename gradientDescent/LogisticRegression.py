import logging
from turtle import width
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


def calc_sigmoid(z):
    """returns the sigmoid of z val btw (0-1)"""
    p = 1.0 / (1.0 + np.exp(-z))
    p = np.minimum(p, 0.999999)
    p = np.maximum(p, 0.000001)
    return p


def calc_pred_func(theta, x):
    """returns the prediction of the hypothesis function"""
    y = np.dot(theta, x)
    # print(y)
    return calc_sigmoid(y)


def calc_error(y_pred, y_actual):
    """returns the error of the prediction"""
    error = (-y_actual * np.log(y_pred) - (1 - y_actual)
             * np.log(1 - y_pred)).sum()/len(y_actual)
    return error


def gradient_descent(y_pred, y_actual, x, theta, learning_rate):
    """returns the new theta"""
    temp = np.dot(x.T, y_pred - y_actual) / len(y_actual)
    return theta - learning_rate * temp


def train(X, Y, learning_rate=0.001, iterations=10000, theta=30):
    cost_list = []

    for _ in tqdm(range(iterations)):
        y_pred = calc_pred_func(theta, X)
        cost = calc_error(y_pred, Y)

        cost_list.append(cost)
        theta = gradient_descent(y_pred, Y, X, theta, learning_rate)
        # ------------------------------------
        # if i % 50 == 0:
        #     logging.log(msg=f"Iteration: {i} Cost: {cost}, Theta: {theta}")
        # ---------------xcde5mekkh,dn.dbm,m.sd ---------------------
    return theta


def predict(ang, x):
    y = calc_pred_func(ang, x)
    return [0 if i < 0.8 else 1 for i in y]


def graph(model, ang):
    px = np.linspace(0, 200, 1000)
    py = model.predict(px.reshape(-1, 1))

    # plt.scatter_plot(px, py)
    plt.scatter(px, py)

    if ang is not None:
        plt.scatter(px, np.array([predict(ang, px)]
                                 ).reshape(-1, 1), color='red', s=1)

    plt.show()


def test():
    import pandas as pd
    df = pd.read_csv('titanic_age_survived.csv', sep=",")
    X = np.array([i for i in range(0, 200)])
    Y = np.array([0 if i < 50 else 1 for i in range(0, 200)])

    from sklearn.linear_model import LogisticRegression
    logisticRegr = LogisticRegression()
    logisticRegr.fit(X.reshape(-1, 1), Y)

    print("---------------")
    print(logisticRegr.coef_)
    print(logisticRegr.intercept_)
    print(logisticRegr.get_params())
    print("Accuracy : ", logisticRegr.score(X.reshape(-1, 1), Y))
    print("-----------")

    ang = train(X, Y)

    # graph(ang)
    graph(logisticRegr, ang)


def main():
    test()
    # X = np.array([47, 62, 27, 22, 14, 30, 26, 18, 21])
    # Y = np.array([1,  0, 0, 1, 0, 1,  0, 1, 0])
    # ang = train(X, Y)

    # px = np.linspace(0, 100, 1000)
    # py = calc_pred_func(ang, px)

    # plt.plot(px, py)
    # plt.show()


if __name__ == "__main__":
    main()
