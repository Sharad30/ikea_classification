from src.datapipe import get_all_data_generators
import fastai
from fastai import *
from fastai.vision import *

def show_batch():
    data = get_all_data_generators()
    return data.show_batch(rows=3, figsize=(7,8))


def plot_top_losses(learn, min_val=2):
    interp = ClassificationInterpretation.from_learner(learn)
    return interp.most_confused(min_val)
