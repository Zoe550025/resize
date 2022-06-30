import cv2
from matplotlib import pyplot as plt
from os import listdir

resize = int(input("which size do you want to change? "))
resize_dir = "train/chengTree/"
stored_dir = "640/" + resize_dir
pics = listdir(resize_dir)

for pic in pics:
    pic = resize_dir + pic
    print(pic)
    img = cv2.imread(pic)

    img_wight = img.shape[1]
    img_hight = img.shape[0]

    if (img_wight > img_hight):
        new_img_wight = resize
        new_img_hight = round(img_hight * resize / img_wight)
        new_img = cv2.resize(img,(new_img_wight,new_img_hight),interpolation=cv2.INTER_NEAREST)
    elif (img_hight > img_wight):
        new_img_wight = round(img_wight * resize / img_hight)
        new_img_hight = resize
        new_img = cv2.resize(img,(new_img_wight,new_img_hight),interpolation=cv2.INTER_NEAREST)
    else:
        new_img_wight = img_wight
        new_img_hight = img_hight
        new_img = img

    top = 0
    bottom = resize - new_img_hight
    left = 0
    right = resize - new_img_wight
    new_img = cv2.copyMakeBorder(new_img, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=0)


    pic_name = stored_dir + pic.replace(".png","").replace(resize_dir,"") +".png"
    print("stored in "+pic_name)
    cv2.imwrite(pic_name,new_img)