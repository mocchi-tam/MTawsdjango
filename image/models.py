from django.db import models

class Image(models.Model):     
    file = models.ImageField('画像', upload_to='img/')
    names = models.CharField('メンバー名', max_length=255)
    
    def __str__(self):
        return self.names
    