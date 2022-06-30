import os
from openpyxl import load_workbook
import random

rootdir = 'E:\\tzuwen\\tree_segmentation2\\resize_test\\640_1125'
#list所有crop目錄
crop_list = []
for root, dirs, files in os.walk(rootdir):
    if root.find("crop")>0:
        for f in files:
            full_addr = os.path.join(root,f)
            crop_list.append(full_addr)
num_crop_list = len(crop_list)
#print(num_crop_list)
# #   列出目前讀取到的路徑
#   print("path：", root)
# #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
#   print("directory：", dirs)
# #   列出在這個路徑下讀取到的所有檔案
#   print("file：", files)

#以學生為單位，每人隨機五張，每一次取出來，就刪掉
#並記錄在excel裡面

#開excel
mywb = load_workbook('E:\\tzuwen\\tree_segmentation2\labeling\\1101-210016 資料結構與演算法(一) {mlang en} Data Structures and Algorithms (1){mlang}修課名單.xlsx')
sheet = mywb['1101-210016 資料結構與演算法(一) {mlang ']
#讀excel，每一欄放隨機的五個crop_list
cellRange = sheet['C2':'G65']
# 以 for 迴圈逐一處理每個儲存格
for row in cellRange:
    for c in row:
        get = random.randint(0, num_crop_list)
        c.value = crop_list[get]
        crop_list.pop(get)
        num_crop_list = len(crop_list)

mywb.save('E:\\tzuwen\\tree_segmentation2\labeling\\1101-210016 資料結構與演算法(一) {mlang en} Data Structures and Algorithms (1){mlang}修課名單_1.xlsx')

