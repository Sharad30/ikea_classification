# Various augmentation parameters
# do_flip: if True, a random flip is applied with probability 0.5
# flip_vert: requires do_flip=True. If True, the image can be flipped vertically or rotated of 90 degrees, otherwise only an horizontal flip is applied
# max_rotate: if not None, a random rotation between -max_rotate and max_rotate degrees is applied with probability p_affine
# max_zoom: if not 1. or less, a random zoom betweem 1. and max_zoom is applied with probability p_affine
# max_lighting: if not None, a random lightning and contrast change controlled by max_lighting is applied with probability p_lighting
# max_warp: if not None, a random symmetric warp of magnitude between -max_warp and maw_warp is applied with probability p_affine
# p_affine: the probability that each affine transform and symmetric warp is applied
# p_lighting: the probability that each lighting transform is applied
# xtra_tfms: a list of additional transforms you would like to be applied

train_augmentation_params = {
    
}

val_augmentation_params = {
    
}

test_augmentation_params = {
    
}
