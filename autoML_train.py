from tpot import TPOTClassifier
from sklearn.metrics import f1_score
from joblib import dump

from data_prebaration import *
from load_dataset import *
from calibration import *


def autoML_fit():
    X, y = load_dataset("./Train_Split.csv")
    automl = TPOTClassifier(generations=5, population_size=50, scoring='f1', verbosity=2, random_state=1, n_jobs=-1)
    automl.fit(X, y)

    automl.export('tpot_data.py')

    best_model = automl.fitted_pipeline_

    calibrated_model = calibrate(best_model)

    serialized_model = dump(calibrated_model, filename="serialized_model")

    return serialized_model
