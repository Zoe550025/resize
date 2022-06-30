import xml.etree.ElementTree as ET
import os

tag_path = input("what do you want to change the path of tag? ").replace("\\","/") + "/"
path = input("which dir do u want to change").replace("\\","/")
os.chdir( path )
print("Now you are at ",os.getcwd())
tree = ET.parse('0.xml')
root = tree.getroot()

root.find("folder").text = str("train")
root.find("filename").text = str("0.png")
root.find("path").text = str(tag_path) + str("0.xml".replace("xml","png"))
root.find("size")[0].text = str(640)
root.find("size")[1].text = str(640)

tree.write('0.xml')