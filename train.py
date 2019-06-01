from src.architecture import classifier_pretrained
from src.datapipe import get_all_data_generators
import config.config as cfg
import os

def do_train():
    filepath = os.path.join("model", cfg.EXPERIMENT_LABEL+cfg.BASE_MODEL+".h5")
    data = get_all_data_generator()
    model = classifier_pretrained(data)
    
    learn.fit_one_cycle(cfg.EPOCHS, 1e-3)
    model.save(filepath)

    return model


if __name__ == "__main__":
    do_train()
