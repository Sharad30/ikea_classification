from src.inference import predict_test
from src.architecture import classifier_pretrained
from src.datapipe import get_all_data_generators
import pandas as pd
import numpy as np
import os
import config.config as cfg


def generate_and_save_submission_csv(model_path, submission_path):
    """Generates and stores submission file

    Arguments:
        model_path -- Path to the model to be used for submission
        test_data_path -- Path to the test data file
        submission_path -- Path to store submission file
    """
    data = get_all_data_generators()
    model = classifier_pretrained(data, model_path, False)
    submission_df = generate_submission_df(model)
    save_submission_csv(submission_df, submission_path)


def generate_submission_df(model):
    """Generates submission dataframe

    Arguments:
        model -- The model to be used for submission
        test_df  -- Test csv file loaded in dataframe

    Returns:
        dataframe -- submission dataframe
    """
    submission_df = predict_test(model)
    # submission_df = pd.concat([image_name, label], axis=1)
    return submission_df


def save_submission_csv(submission_df, path):
    """save submission csv file

    Arguments:
        submission_df  -- dataframe returned from `generate_submission_df()`
        path  -- path where submission should be saved
    """

    submission_df.to_csv(path, index=False)


def validate_submission_csv(submission_df):
    test_df = pd.read_csv('../data/V2/test_actual.csv')
    merge_df = pd.merge(test_df, submission_df, on='image_name')
    class_map = {'bed': 0, 'chair': 1, 'desk': 2, 'kitchen': 3}
    merge_df = merge_df.replace({'label_x': class_map})

    accuracy = (merge_df.label_x == merge_df.label_y).sum()/ merge_df.shape[0]
    return accuracy  


if __name__=='__main__':
    generate_and_save_submission_csv('with_imagenet_pretrained_resnet50', 'submissions/with_imagenet_pretrained_resnet50.csv')
