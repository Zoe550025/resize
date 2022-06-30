import cv2
from matplotlib import pyplot as plt
from os import listdir

resize = int(input("which size do you want to change? "))
resize_dir = "test/"
stored_dir = "640/" + resize_dir
pics = listdir(resize_dir)
print(stored_dir)

for pic in pics:
    if (pic[-3:] == "png"):
        print(pic)
        resize_pic = resize_dir + pic
        img = cv2.imread(resize_pic)

        img_wight = img.shape[1]
        img_hight = img.shape[0]

        if (img_wight > img_hight):
            new_wight = resize
            new_hight = round(img_hight * resize / img_wight)
            
            top = 0
            bottom = resize - new_hight
            left = 0
            right = 0

        elif(img_hight > img_wight):
            new_wight = round(img_wight * resize / img_hight)
            new_hight = resize

            top = 0
            bottom = 0
            left = 0
            right = resize - new_wight
            
        else:
            new_wight = resize
            new_hight = resize

            top = 0
            bottom = resize - new_hight
            left = 0
            right = resize - new_wight

        resize_img = cv2.resize(img,(new_wight,new_hight),interpolation=cv2.INTER_AREA)
        new_img = cv2.copyMakeBorder(resize_img, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=0)


        pic_name = stored_dir + pic
        cv2.imwrite(pic_name,new_img)
        print("stored in "+ pic_name)