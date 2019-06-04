from fastai.callbacks import CSVLogger, MixUpCallback
from PIL import ImageFile
from src.datapipe import get_all_data_generators
from src.architecture import classifier_pretrained

def get_callbacks(model, alpha):
    csv_logger = CSVLogger(model, 'logs')

    mixup = MixUpCallback(model, alpha)
    callbacks = [csv_logger, mixup]
    return callbacks

def get_lr_plot(pretrained_model=False, start_lr=1e-7):
    if pretrained_model==False:
        data = get_all_data_generators()
        learn = classifier_pretrained(data, pretrained_model, False)
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        learn.lr_find()
        return learn
    else:
        data = get_all_data_generators()
        model = classifier_pretrained(data, pretrained_model, True)
        learn = model.load(f'../../models/{pretrained_model}')
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        learn.lr_find(start_lr)
        return learn