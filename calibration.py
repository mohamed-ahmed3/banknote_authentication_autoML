from sklearn.calibration import CalibratedClassifierCV


def calibrate(model):
    calibrated_model = CalibratedClassifierCV(model, method='sigmoid', cv='prefit')

    return calibrated_model
