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
        data = (ImageList.from_folder(cfg.BASE_IMG_DIR+cfg.TRAIN_PATH)
                .split_by_rand_pct(0.1)
                .label_from_folder()
                .transform(get_transforms(), size=224)
                .add_test_folder(cfg.TEST_PATH)
                .databunch())

        return data