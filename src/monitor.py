from fastai.callbacks import CSVLogger

def get_callbacks(model):
    csv_logger = CSVLogger(model, 'logs')
    callbacks = [csv_logger]
    return callbacks