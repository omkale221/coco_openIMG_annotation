import numpy as np
import os
from csv import DictReader
from PIL import Image


path = 'O:\daaaCEMTREX\coco_data\Traffic Light'
path2 = '\\'+'v1v'
path3 = '\\Traffic data\coco_v0'
file = os.listdir( path+path2 )
length  =  len(file)
print(file,length)
i = 0
counter = 500


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def clas(color):
    if color == "Signal":
        return 0
    if color == "Red":
        return 1
    if color == "Yellow":
        return 2
    if color == "Green":
        return 3


for file in os.listdir(path+path2):
    if file.endswith(".csv"):
        with open(path+path2+'\\'+file , 'rt') as f:
            data = DictReader(f)
            # header = next(data)
            # if header != None :

            for row in data:
                # print(row)
            #     for key, value in row.items():

                        f1 = row['file_name']
                        if os.path.isfile(path + path2 + "\\" + f1 +'.txt'):
                            nf = open(path + path2 + "\\" + f1 +'.txt', "a")
                            im = Image.open(os.path.join(path + path3, f1))
                            w = int(im.size[0])
                            h = int(im.size[1])
                            b = (int(row['xmin']), int(row['xmax']), int(row['ymin']), int(row['ymax']))
                            bb = convert((w, h), b)
                            cc = clas(row['classes'])
                            li = list(bb)
                            nf.write(str(cc)+ str(li) + '\n')
                            nf.close()
                        else:
                            nf = open(path + path2 + "\\" + f1 +'.txt', "x")
                            im = Image.open(os.path.join(path+path3, f1))
                            w = int(im.size[0])
                            h = int(im.size[1])
                            b = (int(row['xmin']), int(row['xmax']), int(row['ymin']), int(row['ymax']))
                            bb = convert((w,h), b)
                            cc = clas(row['classes'])
                            b1=str(bb[0])
                            b2=str(bb[1])
                            b3=str(bb[2])
                            b4=str(bb[3])

                            li = list(bb)
                            # print(li)
                            nf.write(str(cc)+ str(li)+ '\n')

                            # nf.write(row['classes'] +' '+ row['xmin'] +','+ row['ymin'] +','+ row['xmax'] +','+ row['ymax'] + '\n')
                            nf.close()
                            # new = os.path.join(path+'\\'+'yolo', f1 + '.txt ')
                            # file1 = open(f1, "w")
                            # file1.write('sd')
                            # if
                            # file1.write()





