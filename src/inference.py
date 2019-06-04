import fastai
from fastai import *
from fastai.vision import *
import pandas as pd
import numpy as np

def predict_test(model):
    ds_type = DatasetType.Test
    predictions = model.get_preds(ds_type)
    predicted_labels = pd.Series(np.argmax(predictions[0], axis=1), name='label')

    image_name = pd.Series(name='image_name')
    for path in model.data.test_ds.x.items:
        image_name = image_name.append(pd.Series(str(path).split('/')[-1]))

    image_df = pd.DataFrame(image_name, columns=['image_name']).reset_index(drop=True)
    test_df = pd.concat([image_df['image_name'], predicted_labels], axis=1)

    return test_df