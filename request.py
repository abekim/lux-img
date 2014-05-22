'''
Makes the necessary requests and saves images into `img/` directory

author: @abekim
'''
from pyquery import PyQuery as pq

class Page(object):
    def __init__(self, url):
        self.url = url
        self.base = url.split('//')[1].split('/')[0]

        self.d = pq(self.url)

    def extract_img(self, d_id='single_picture'):
        '''
        extract image from url via ID of the img DOM element
        '''
        try:
            url = self.d('img#' + d_id).attr('src')
            
            # get url components to get the original image
            url_comps = url.split('.')
            if len(url_comps) > 4:
                url_comps.pop(len(url_comps) - 2)

            return '.'.join(url_comps)
        except IndexError:
            return None

    def extract_next(self, d_id='next'):
        '''
        extract the url of the next page using the existing next button
        '''
        next_url = self.d('a#' + d_id).attr('href')
        if not next_url:
            print 'No more images left in the album'
            return ''
        else: 
            return 'http://' + self.base + next_url

