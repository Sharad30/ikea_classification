from src.datapipe import get_all_data_generators
import fastai
from fastai import *
from fastai.vision import *
from src.datapipe import get_all_data_generators
from src.architecture import classifier_pretrained

def show_batch():
    data = get_all_data_generators()
    return data.show_batch(rows=3, figsize=(7,8))


def plot_top_losses(pretrained_model, min_val=2):
    data = get_all_data_generators()
    learn = classifier_pretrained(data, pretrained_model, True)
    interp = ClassificationInterpretation.from_learner(learn)
    return interp
