import fastai
from fastai import *
from fastai.vision import *
import config.config as cfg

def random_seed(seed_value, use_cuda):
    np.random.seed(seed_value) # cpu vars
    torch.manual_seed(seed_value) # cpu  vars
    random.seed(seed_value) # Python
    if use_cuda: 
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value) # gpu vars
        torch.backends.cudnn.deterministic = True  #needed
        torch.backends.cudnn.benchmark = False

def get_all_data_generators():
        """Create data_generators for train, val and test with augmentations defined in src.augmentations

        Returns:
        train_datagen, val_datagen, test_datagen -- three datagenerators
        """
        random_seed(cfg.RANDOM_SEED, True)
        data = ImageDataBunch.from_csv(path=cfg.BASE_IMG_DIR, folder=cfg.TRAIN_PATH, 
                                      csv_labels=cfg.TRAIN_CSV_PATH, 
                                      label_col=1, bs=32, test=cfg.TEST_PATH, 
                                      ds_tfms=get_transforms(), size=224, valid_pct=0.1, num_workers=1).\
                                      normalize(imagenet_stats)

        return data