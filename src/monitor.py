from fastai.callbacks import CSVLogger
from PIL import ImageFile
from src.datapipe import get_all_data_generators
from src.architecture import classifier_pretrained

def get_callbacks(model):
    csv_logger = CSVLogger(model, 'logs')
    callbacks = [csv_logger]
    return callbacks

def get_lr_plot(pretrained_model=False):
    if pretrained_model==False:
        data = get_all_data_generators()
        learn = classifier_pretrained(data, pretrained_model, False)
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        learn.lr_find()
        return learn.recorder.plot(suggestion=True)
    else:
        data = get_all_data_generators()
        model = classifier_pretrained(data, pretrained_model, True)
        learn = model.load(f'../../models/{pretrained_model}')
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        learn.lr_find()
        return learn.recorder.plot(suggestion=True)