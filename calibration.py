from sklearn.calibration import CalibratedClassifierCV


def calibrate(model):
    calibrated_model = CalibratedClassifierCV(model, method='isotonic', cv='prefit')

    return calibrated_model
