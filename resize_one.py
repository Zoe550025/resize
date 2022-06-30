import cv2
import os
from matplotlib import pyplot as plt

resize = 256#int(input("which size do you want to change? "))
pic = str(input("which picture do you want to resize? "))
resize_dir = "E:\\tzuwen\\tree_segmentation2\\resize_test\\640_sakura_20220419\\0308_shizuoka-kawazuchou\\0-52"
pic = os.path.join(resize_dir,pic)
stored_dir = resize_dir

print(pic)
print(stored_dir)
img = cv2.imread(pic)

img_wight = img.shape[1]
img_hight = img.shape[0]
#print(img_wight)
#print(img_hight)

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


pic_name = stored_dir + pic.replace(".png","_").replace(resize_dir,"") + str(new_img_wight)+ ".png"
print(pic_name)
cv2.imwrite(pic_name,new_img)