import pandas as pd


def load_dataset(path):
    train = pd.read_csv(path)

    train = train.drop("variance", axis=1)

    X = train.iloc[:, :-1]
    y = train.iloc[:, -1:]

    return X, y
