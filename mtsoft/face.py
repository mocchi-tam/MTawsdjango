import io
from django.core.files.uploadedfile import InMemoryUploadedFile

import copy
import cv2
from PIL import Image
import numpy as np
from .inference import inference

NAMES=[
'浅井七海',
'播磨七海',
'本間麻衣',
'稲垣香織',
'黒須遥香',
'前田彩佳',
'道枝咲',
'武藤小麟',
'長友彩海',
'野口菜々美',
'佐藤美波',
'庄司なぎさ',
'鈴木くるみ',
'田口愛佳',
'田屋美咲',
'梅本和泉',
'山内瑞葵',
'山根涼羽',
'安田叶'
]

def detect(upload_file):
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    tmp = Image.open(upload_file)
    if tmp.mode != 'RGB':
        tmp = tmp.convert('RGB')
    image_org = np.asarray(tmp)
    image = copy.deepcopy(image_org)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.11,
                                     minNeighbors=3,
                                     minSize=(30, 30))
    
    names = []
    
    if len(faces) > 0:
        for rect in faces:
            (x, y, w, h) = rect
            cv2.rectangle(image_org, (x, y), (x+w, y+h), (255, 0, 0), 3)
            dst_img = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            dst_img = cv2.resize(dst_img, (224,224))
            name = inference(dst_img)
            names.append(name)
    
    image_org = Image.fromarray(np.uint8(image_org))
    
    image_io = io.BytesIO()
    image_org.save(image_io, format='JPEG')
    image_file = InMemoryUploadedFile(image_io, None, 'foo.jpg', 'image/jpeg',
                                      image_io.getbuffer().nbytes, None)
    
    return image_file, ','.join(names)
