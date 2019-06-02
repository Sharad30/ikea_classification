import fastai
from fastai import *
from fastai.vision import *
import config.config as cfg


def create_pretrained_model(data):
    if cfg.BASE_MODEL == 'densenet121':
        model = cnn_learner(data, models.densenet121, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'densenet169':
        model = cnn_learner(data, models.densenet169, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'densenet201':
        model = cnn_learner(data, models.densenet201, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'resnet50':
        model = cnn_learner(data, models.resnet50, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'resnet101':
        model = cnn_learner(data, models.resnet101, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'resnet152':
        model = cnn_learner(data, models.resnet152, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'vgg16':
        model = cnn_learner(data, models.vgg16_bn, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'vgg19':
        model = cnn_learner(data, models.vgg19_bn, pretrained=cfg.PRETRAINED, metrics=accuracy)
    elif cfg.BASE_MODEL == 'xception':
        model = cnn_learner(data, models.xception, pretrained=cfg.PRETRAINED, metrics=accuracy)
    else:
        print("fastai doesn't have the pretrained weights for it")
        print("""
        Below are the codes for Base Models:
        1. xception: Xception V1 Model (Default Input size: 299x299)
        2. vgg16: VGG16 Model (Default Input size: 224x224)
        3. vgg19: VGG19 Model (Default Input size: 224x224)
        4. resnet50, resnet101, resnet152, resnet50v2, resnet101v2, resnet152v2
           resnext50, resnext101: ResNet family of models (Default Input size: 224x224)
        5. inceptionv3: Inception Net Version 3 (Default Input size: 299x299)
        6. inceptionresnetv2: Inception ResNet v2 (Default Input size: 299x299)
        7. mobilenetv1, mobilenetv2: Mobile Net model (Default Input size: 224x224)
        8. densenet121, densenet169, densenet201: DenseNet model family (Default Input size: 224x224)
        9. nasnetlarge: NASNet model (Default Input size: 331x331)
        10. nasnetmobile: NASNet mobile model (Default Input size: 224x224)
        """)

    return model

def classifier_pretrained(data):

    pretrained_model = create_pretrained_model(data)
    return pretrained_model