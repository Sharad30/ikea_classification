import fastai
from fastai import *
from fastai.vision import *

def predict_test(model):
    ds_type = DatasetType.Test
    predictions = model.get_preds(ds_type)
    predicted_labels = pd.Series(np.argmax(predictions[0], axis=1), name='label')
    return predicted_labels