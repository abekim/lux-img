'''
Utilities using OS module

author: @abekim
'''
import os

def count_img(dir_path='.'):
    img_exts = ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff', 'raw', 'svg']

    return len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.split('.')[-1].lower() in img_exts])
