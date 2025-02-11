import os
import shutil

path_label = 'labels'
labels = os.listdir(path_label)
path_raw_imgs = 'out_image'
raw_imgs = os.listdir(path_raw_imgs)
path_imgs = 'images'
for folder in labels:
    labels = os.listdir(os.path.join(path_label,folder))
    for label in labels:
        filename = label[:-3]+'jpg'
        path_raw_img = os.path.join(path_raw_imgs,filename)
        path_new_img = os.path.join(path_imgs,folder)
        shutil.copy(path_raw_img,path_new_img)