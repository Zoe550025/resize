import cv2
import os
from matplotlib import pyplot as plt

def resize_for_unet():
    new_imgs = []
    for pic in addr:
        img = cv2.imread(pic)

        img_wight = img.shape[1]
        img_hight = img.shape[0]

        if (img_wight > img_hight):
            new_img_wight = resize
            new_img_hight = round(img_hight * resize / img_wight)
            new_img = cv2.resize(img, (new_img_wight, new_img_hight), interpolation=cv2.INTER_NEAREST)
        elif (img_hight > img_wight):
            new_img_wight = round(img_wight * resize / img_hight)
            new_img_hight = resize
            new_img = cv2.resize(img, (new_img_wight, new_img_hight), interpolation=cv2.INTER_NEAREST)
        else:
            # new_img_wight = img_wight
            # new_img_hight = img_hight
            # new_img = img
            new_img_wight = resize
            new_img_hight = resize
            new_img = cv2.resize(img, (new_img_wight, new_img_hight), interpolation=cv2.INTER_NEAREST)

        top = 0
        bottom = resize - new_img_hight
        left = 0
        right = resize - new_img_wight
        new_img = cv2.copyMakeBorder(new_img, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=0)
        new_imgs.append(new_img)