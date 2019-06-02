from src.architecture import classifier_pretrained
from src.datapipe import get_all_data_generators
import config.config as cfg
import os
from fastai.utils.mod_display import *
from PIL import ImageFile
from src.monitor import get_callbacks

def do_train():
    filepath = '../../models/'+cfg.EXPERIMENT_LABEL+'_'+cfg.BASE_MODEL
    data = get_all_data_generators()
    learn = classifier_pretrained(data)
    callbacks = get_callbacks(learn)
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    with progress_disabled_ctx(learn) as learn:
      learn.fit_one_cycle(cfg.EPOCHS, 1e-3, callbacks=callbacks)
      logs_df = learn.csv_logger.read_logged_file()
      logs_df.to_csv(f'{cfg.EXPERIMENT_LABEL}_{cfg.BASE_MODEL}.csv')
      learn.save(filepath)


if __name__ == "__main__":
    do_train()