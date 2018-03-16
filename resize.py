import os
from PIL import Image

def resize(img_name, resize_ratio):
    max_height = resize_ratio
    i = Image.open(img_name)
    width, height = i.size

    factor = 1

    if width> height:
        factor = 0
        w_ratio = height/resize_ratio
    else:
        factor = 1
        w_ratio = width/resize_ratio

    crop_size = ((height/w_ratio) - max_height)/2 
    # limit image size to (x = resize_ratio, y <= max_height)
    i = i.resize((int(width/w_ratio), int(height/w_ratio)))
    #crop if height is too long
    if i.size[factor] > max_height:
        i = i.crop(
            (
                0,
                int(i.size[factor]/2) - max_height/2,
                resize_ratio,
                int(i.size[factor]/2) + max_height/2
            )
        )

    #save
    i.convert('RGB').save(img_name, dpi=(720,720))
##


name = input('folder name: ')
i = 1
for file in os.listdir(name):
    print(name+'/'+file)
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        resize(name+'/'+file, 64)
        os.rename(name+'/'+file, name+"/{}.{}.".format(name,i)+file.split('.')[-1])
        i +=1
