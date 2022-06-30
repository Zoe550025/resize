
from ast import literal_eval
from pathlib import Path
import cv2
import os
import shutil
import pandas as pd
import openpyxl
path_oringnal = "E:\\tzuwen\\tree_segmentation2\\resize_test\\640_20220624_2-19\\202112"#0-2\\2021\\1\\"       #TODO
#excel_name = '202112_average.xlsx'
pic_list = []
pic_list1 = []
pic_name = []
dict_data = dict()

def test_folder(folderpath):
    try:
        os.makedirs(folderpath)
    # 檔案已存在的例外處理
    except FileExistsError:
        pass
        #print("檔案已存在。")

def average(xml_data,imgs):
    total = 0
    num = 0
    for xd, i in zip(xml_data, imgs):
        pic_list1 = literal_eval(xd)
        if pic_list1 != []:
            for num_box, box in enumerate(pic_list1):
                total = total + float(box[4])
                num = num + 1
    avg = total / (num)
    print( total, "/", (num), " = ", avg)
    return avg


for p in Path(path_oringnal).iterdir():       #E:\tzuwen\tree_segmentation2\resize_test\640_20220509\0\0-0\2021\1\
    if p.is_file():
        tmp = str(p).split("\\")    #['E:', 'tzuwen', 'tree_segmentation2', 'resize_test', '640_20220624_2-19', '202112', '2021-12-12_2115.png']
        #print(tmp)
        pic_list.append(str(p))
        pic_name.append(tmp[-1])
try:
    with open(os.path.join(path_oringnal,"results\\coordinates.json"),"r") as f:
        data = f.readlines()
except:
    pass
month_average = average(data, pic_name)
#print(month_average)
img_pass = 0
img_need = 0
for d,p in zip(data,pic_name):
   pic_list=literal_eval(d)
   #print(pic_list)
   #print(p)
   if pic_list != []:
       for num_box,box in enumerate(pic_list):
           #print(num_box,box)
           if int(box[4])> month_average:          #TODO:要crop的average準確率值
               ymin = int(box[0])
               ymax = int(box[1])
               xmin = int(box[2])
               xmax = int(box[3])
               img_path = os.path.join(str(path_oringnal),str(p))
               #print(num_box, img_path)
               img = cv2.imread(img_path)
               #print(img_path)
               crop_img = img[ymin:ymax,xmin:xmax]
               #shutil.rmtree(os.path.join(path_oringnal,"crop/"), ignore_errors=True)
               test_folder(os.path.join(path_oringnal,"crop/"))
               tmp_str = "crop/"+ p.replace(".png","") + "_" + str(num_box)+".png"
               #print(os.path.join(path_oringnal,tmp_str))
               cv2.imwrite(os.path.join(path_oringnal,tmp_str),crop_img)
               img_need += 1
           else:
               img_pass += 1
               #print(img_pass)

