def generate_test_csv():
    image_name = pd.Series(os.listdir('data/test/'), name='image_name')
    test_labels = image_name.apply(lambda x: x.split('_')[1].split('.')[0])
    test_df = pd.concat([image_name, test_labels], axis=1)
    test_df.columns = ['image_name', 'label']
    test_df.to_csv('data/test.csv', index=False)