'''
Makes the necessary requests and saves images into `img/` directory

author: @abekim
'''
from pyquery import PyQuery as pq

class Page(object):
    def __init__(self, url):
        self.url = url
        self.base = url.split('//')[0] + url.split('//')[1].split('/')[0]

        self.d = pq(url = self.url)

    def extract_img(self, d_id='single_picture'):
        '''
        extract image from url via ID of the img DOM element
        '''
        try:
            url = self.d('img#' + d_id).attr('src')
            
            # get url components to get the original image
            url_comps = url.split('.')
            url_comps.pop(len(url_comps) - 2)

            return '.'.join(url_comps)
        except IndexError:
            return None

    def extract_next(self, d_id='next'):
        '''
        extract the url of the next page using the existing next button
        '''
        print self.d('a#' + d_id)
        try:
            return self.base + self.d('a#' + d_id).attr('href')
        except IndexError:
            print 'No more images left in the album'
            return None

