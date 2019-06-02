from fastai.callbacks import CSVLogger
from PIL import ImageFile
from src.datapipe import get_all_data_generators
from src.architecture import classifier_pretrained

def get_callbacks(model):
    csv_logger = CSVLogger(model, 'logs')
    callbacks = [csv_logger]
    return callbacks

def get_lr_plot():
    data = get_all_data_generators()
    learn = classifier_pretrained(data)
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    learn.lr_find()
    
    return learn.recorder.plot(suggestion=True)