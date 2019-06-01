import fastai
from fastai import *
from fastai.vision import *
import config.config as cfg

def get_all_data_generators():
    """Create data_generators for train, val and test with augmentations defined in src.augmentations
    
    Returns:
        train_datagen, val_datagen, test_datagen -- three datagenerators
    """

    train_df, val_df, test_df = load_all_data()

    data = ImageDataBunch.from_folder(cfg.BASE_IMG_DIR, train= cfg.TRAIN_PATH, valid_pct= 0.1, test= cfg.TEST_PATH, bs=cfg.BATCH_SIZE,
                                  ds_tfms=get_transforms(), size=cfg.IMAGE_DIMS, num_workers=1)\
                                  .normalize(imagenet_stats)

    return data