from autoML_train import *


def predict_probability(model, X_train, y_train, X_test):
    model.fit(X_train, y_train)

    calibrated_probabilities = model.predict_proba(X_test)

    positive_class_probabilities = calibrated_probabilities[:, 1]

    probability_list = positive_class_probabilities.tolist()

    return probability_list
