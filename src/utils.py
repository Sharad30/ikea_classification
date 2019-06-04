import os
import pandas as pd

def generate_test_csv():
    image_name = pd.Series(os.listdir('data/test/'), name='image_name')
    test_labels = image_name.apply(lambda x: x.split('_')[1].split('.')[0])
    test_df = pd.concat([image_name, test_labels], axis=1)
    test_df.columns = ['image_name', 'label']
    test_df.to_csv('data/test.csv', index=False)


def rename_image_files():
    for directory in os.listdir('data/train'):
        for image in os.listdir(f'data/train/{directory}'):
            os.rename(f'data/train/{directory}/{image}', f'data/train/{directory}/{directory}_{image}')


def generate_train_csv():
    image_name = pd.Series(name='image_name')
    for directory in os.listdir('data/train'):
            image_name = image_name.append(pd.Series(os.listdir(f'data/train/{directory}'), name='image_name'))
    train_df = pd.DataFrame(image_name)
    train_df['label'] = ''
    train_df.label = train_df.image_name.apply(lambda x: x.split('_')[0])
    train_df.to_csv('data/train/train.csv', index=False)


if __name__=='__main__':
    generate_train_csv()