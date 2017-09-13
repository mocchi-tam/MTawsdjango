# -*- coding: utf-8 -*-
from __future__ import print_function

import chainer
from chainer.dataset import convert

class Trainer():
    def __init__(self, model, flag_train=False, flag_resum=True):
        self.model = model
        
        if flag_train:
            self.optimizer = chainer.optimizers.Adam()
            self.optimizer.setup(self.model)
            
        if flag_resum:
            self.load()
            
    def train(self, batch):
        x, t, m = convert.concat_examples(batch, self.gpu)
        
        self.model.cleargrads()
        _, loss = self.model.loss(x, t, m)
        loss.backward()
        self.optimizer.update()
        
        return loss.data, self.model.accuracy.data, len(m)
        
    def test(self, batch):
        x, t, m = convert.concat_examples(batch, self.gpu)
        
        with chainer.using_config('train', False), chainer.no_backprop_mode():
            _, loss = self.model.loss(x, t, m)
        
        return loss.data, self.model.accuracy.data, len(m)
    
    def load(self):
        try: 
            chainer.serializers.load_npz('net.model', self.model)
            print('Successfully resumed model')
        except:
            print('could not resume model or optimizer')
    
    def save(self):
        try:
            chainer.serializers.save_npz('net.model', self.model)
            print('Successfully saved model')
        except:
            print('saving model ignored')