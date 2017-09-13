import chainer.functions as F

from aws_eb_docker_django_skeleton.mtsoft import net
from aws_eb_docker_django_skeleton.mtsoft import trainer
from aws_eb_docker_django_skeleton.mtsoft import preprocess as ip

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

imx = 224
imy = 224
n_cat = len(NAMES)

model = net.NNet(n_out=n_cat)
trainer = trainer.Trainer(model)
pp = ip.ImagePP(x=imx, y=imy, n_cat=n_cat)

def inference(upload_file):
    img = pp.process(upload_file)
    f = F.argmax(trainer.model(img)).data
    return NAMES[f]
