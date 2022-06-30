import os
import cv2
import xml.etree.ElementTree as ET
from os import listdir

path = input("which dir do u want to check? ").replace("\\","/")
os.chdir( path )
print("Now you are at ",os.getcwd())
#file = input("which file do u want to check? ")
files = listdir(path)

for file in files:
    if file[-3:] == "png":
        img = cv2.imread(file)

        img_wight = img.shape[1]
        img_hight = img.shape[0]

        if (img_wight != 640 and img_hight != 640):
            print(file)

    elif (file[-3:] == "xml"):
        #print(file)
        tree = ET.parse(file)
        root = tree.getroot()
        if (root.find("path").text != str(path)+"/"+ str(file.replace("xml","png"))):
            print("path is wrong")
            print(root.find("path").text)

        if(root.find("size")[0].text != str(640) and root.find("size")[1].text != str(640)):
            print("size is wrong")
            print(file)
        
        if (root.find("folder").text != "test"):
            print("folder is wrong")
            print(file)
