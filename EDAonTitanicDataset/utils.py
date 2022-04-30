import scipy
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score


def calc_p_val(categorical_column, df, col_name='Age'):
    """caluclate the p value for the categorical column and Age"""
    if col_name == "Age":
        data = get_table_age(categorical_column, data=df)
    else:
        data = get_table(categorical_column, col_name, data=df)
    chi2, p, dof, ex = scipy.stats.chi2_contingency(data, correction=False)

    del data, dof, ex
    return chi2, f"{p*100:.5f} %"


def get_count_age(data):
    non_null_df = data["Age"].dropna()

    cnt_20 = len(non_null_df[non_null_df < 20])
    cnt_50 = len(non_null_df[non_null_df <= 50]) - cnt_20
    cnt_100 = len(non_null_df[non_null_df >= 50])

    return cnt_20, cnt_50, cnt_100


def get_table_age(categorical_column, data):
    items = data[categorical_column].unique()

    # grouping the data
    cat_data = [
        get_count_age(data[data[categorical_column] == item])
        for item in items]

    return cat_data


def get_table(categorical_column, col_name, data):
    items = data[categorical_column].unique()

    # splitting data to groups
    cat_data = [
        data[data[categorical_column] == item][col_name]
        .value_counts()
        for item in items
    ]

    return pd.DataFrame(cat_data, index=items).fillna(0)


def fill_gaussian(df, col_name):
    temp_df = df.copy()
    idx_s = df[df[col_name].isna()].index

    # Getting gaussian distribution
    vals = np.random.normal(
        loc=temp_df[col_name].mean(),
        scale=temp_df[col_name].std(),
        size=len(idx_s))
    vals = pd.Series(vals, index=idx_s)

    # Filling null values
    temp_df[col_name].fillna(vals, inplace=True)
    return temp_df


def get_age(cols):
    """returns the median box plot of age based on the Pclass"""
    Age = cols["Age"]
    Pclass = cols["Pclass"]

    # if age isn't null
    if not pd.isna(Age):
        return Age

    # median age based on Pclass
    Pclass = int(Pclass)
    lst = [37, 29, 24]
    return lst[Pclass - 1]


def model_stats(model, x_test, y_test):
    pred = model.predict(x_test)

    cm = confusion_matrix(y_test, pred)
    print("Accuracy: ", accuracy_score(y_test, pred))

    sns.heatmap(cm, annot=True)
