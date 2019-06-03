from src.inference import predict_test


def generate_and_save_submission_csv(model_path, submission_path):
    """Generates and stores submission file

    Arguments:
        model_path -- Path to the model to be used for submission
        test_data_path -- Path to the test data file
        submission_path -- Path to store submission file
    """
    model = load_model(model_path)
    submission_df = generate_submission_df(model)
    save_submission_csv(submission_df, submission_path)


def generate_submission_df(model, test_df):
    """Generates submission dataframe

    Arguments:
        model -- The model to be used for submission
        test_df  -- Test csv file loaded in dataframe

    Returns:
        dataframe -- submission dataframe
    """
    image_name = pd.Series(os.listdir('data/test/'), name='image_name')
    label = predict_test(model)
    submission_df = pd.concat([image_name, label], axis=1)
    return submission_df


def save_submission_csv(submission_df, path):
    """save submission csv file

    Arguments:
        submission_df  -- dataframe returned from `generate_submission_df()`
        path  -- path where submission should be saved
    """

    submission_df.to_csv(path, index=False)