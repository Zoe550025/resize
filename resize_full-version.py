import os
import sys
import cv2
import re

import numpy as np

fileList = []
resize = 256                                                           #TODO:要改成甚麼尺寸
num = -1
dir = "0-"
rootdir = "E:\\tzuwen\\tree_segmentation2\\resize_test\\640_20220624_2-19\\202112\\crop"#"E:\\tzuwen\\tree_segmentation2\\resize_test\\original"##'E:\\tzuwen\\tree_segmentation2\data\\0\\' + dir #"E:\\tzuwen\\tree_segmentation2\\resize_test\\640_1125\\2\\2-28\crop"               #要改圖片大小的目錄
stored_dir = "E:\\tzuwen\\tree_segmentation2\\resize_test\\640_20220624_2-19\\202112\\crop\\256x256"#"E:\\tzuwen\\tree_segmentation2\\resize_test\\640_test_0413"# + dir    #"E:\\tzuwen\\tree_segmentation2\\resize_test\\640_1125\\2\\2-28\crop\\256x256"    #改完要放哪裡

def test_folder(folderpath):
    try:
        os.makedirs(folderpath)
    # 檔案已存在的例外處理
    except FileExistsError:
        print("檔案已存在。")

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),cv2.IMREAD_COLOR)
    return cv_img
def cv_imwrite(file_path,img):
    try:
        cv2.imencode('.png', img)[1].tofile(file_path)
    except:
        pass


for root, subFolders, files in os.walk(rootdir):
    for pic in files:
        #print(pic)
        if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', pic):
            picname = pic
            #print(picname)
            pic = os.path.join(root,pic)
            # try:
            #     img = cv2.imread(pic)
            # except:
            #     print("HERE")
            img = cv_imread(pic)

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

            tmp = pic.replace(rootdir,stored_dir)
            print(tmp.replace(picname,""))
            test_folder(tmp.replace(picname,""))
            cv_imwrite(tmp,new_img)
            #test_folder(stored_dir)
            # final = os.path.join(stored_dir, picname)
            # print("stored in ", final)
            # cv2.imwrite(final, new_img)


#print("Total Files ", len(fileList))