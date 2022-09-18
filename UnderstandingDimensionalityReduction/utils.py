import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def load_wine_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the wine data from the sklearn dataset"""
    raw_data = load_wine()
    X = pd.DataFrame(data=raw_data["data"], columns=raw_data["feature_names"])
    Y = pd.DataFrame(raw_data["target"], columns=["target"])

    return (X, Y)

def logistic_reg_accuracy(X: pd.DataFrame, Y: pd.DataFrame) -> float:
    """Calculate the accuracy of the logistic regression model"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)
    y_train, y_test = y_train.values.ravel(), y_test.values.ravel()  # convert to 1d array

    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)

    y_pred = log_reg.predict(X_test)

    score = accuracy_score(y_test, y_pred)

    return score