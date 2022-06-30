import xml.etree.ElementTree as ET
import glob
import os

tag_path = input("what do you want to change the path of tag? ").replace("\\","/") + "/"
path = input("which dir do u want to change? ").replace("\\","/")
os.chdir( path )
print("Now you are at ",os.getcwd())

for xml_file in glob.glob(path + '/*.xml'):
    xml_file = xml_file.replace("\\","/")
    print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_name = xml_file.replace(".xml","").replace(path,"").replace("/","")
    print(xml_name)
    root.find("folder").text = str("test")
    root.find("filename").text = str(xml_name) + ".png"
    root.find("path").text = str(tag_path) + str(root.find("filename").text)
    root.find("size")[0].text = str(640)
    root.find("size")[1].text = str(640)

    tree.write(xml_file)

print("done")