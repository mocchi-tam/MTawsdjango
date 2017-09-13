# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import re
import glob
import numpy as np
from PIL import Image

from chainer.datasets import tuple_dataset

class ImagePP():
    def __init__(self, x=720, y=480, n_cat=8):
        self.x = x
        self.y = y
        self.n_cat = n_cat
    
    def preprocess(self, df):
        array = df.reshape((-1, 3, self.x*self.y))
        # 前処理：画素を 0~1
        array = array.reshape((-1, 3)) / 255.0
        df = array.reshape(df.shape)
        return df
    
    # 推論モード用 逐次処理
    def process(self, img):
        xp = np
        #img = np.asarray(Image.open(fname))
        img = xp.asarray(img, dtype=xp.float32).transpose(2,0,1)
        img = img.reshape((1,3,self.y,self.x))
        img = self.preprocess(img)
        return img
    
    # 学習モード用 データセット作成
    def makedataset(self, dirnames):
        xp = np
        
        # ファイル数取得
        N_dataset = 0
        for d in dirnames:
            files = os.listdir(d)
            for file in files:
                index = re.search('.jpg', file)
                if index: N_dataset += 1
        
        # 画像
        df = xp.zeros((N_dataset,3,self.y,self.x), dtype=xp.float32)
        # 正解ラベルのカテゴリ番号
        cat = xp.zeros((N_dataset), dtype=xp.int32)
        fnames = []
        count = 0
        
        for (i, d) in enumerate(dirnames):
            files = glob.glob(d + '/*.jpg')
            for file in files:
                print(count, file)
                fnames.append(file)
                img = np.asarray(Image.open(file))
                img = xp.asarray(img, dtype=xp.float32).transpose(2,0,1)
                
                df[count] = img
                cat[count] = i
                count += 1
        
        df = self.preprocess(df)
        df = tuple_dataset.TupleDataset(df, cat)
        return df, fnames
    