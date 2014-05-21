'''
Models used in the requester

author: @abekim
'''
import os, os_utils
from PIL import Image

class Album(object):
    '''
    An album of images
    '''
    def __init__(self, name, dir_name=''):
        self.name = name
        if not dir_name:
            self.dir = 'img/' + name + '/'
        else:
            self.dir = 'img/' + dir_name + '/'
        self.ext = '.jpg'

        # create directory if it doesn't exist
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        # aliases
        self.save = self.save_img_from_url

    def save_img_from_url(self, img_url):
        try:
            import urllib2 as urllib
        except ImportError:
            import urllib
        from StringIO import StringIO

        # save image
        content = StringIO(urllib.urlopen(img_url).read())
        img = Image.open(content)
        img.save(self.dir + str(self.count + 1) + self.ext)

    def get_img(self, img_name='1'):
        return Image.open(self.dir + str(img_name) + self.ext).show()

    @property
    def count(self):
        return os_utils.count_img(self.dir)

