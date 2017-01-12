'''
Makes the necessary requests and saves images into `img/` directory

author: @abekim
'''
from pyquery import PyQuery as pq
import re

class Page(object):
    def __init__(self, url, selectors={}):
        self.url = url
        self.base = url.split('//')[1].split('/')[0]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12'
        }
        self.image_selector = selectors.get('image', 'img#single_picture') or 'img#single_picture'
        self.next_selector = selectors.get('next', 'a#next') or 'a#next'

        self.d = pq(self.url, headers=self.headers)

    def extract_img(self):
        '''
        extract image from url via ID of the img DOM element
        '''
        try:
            url = self.d(self.image_selector).attr('src')

            # get url components to get the original image
            url_comps = url.split('.')
            if len(url_comps) > 4:
                url_comps.pop(len(url_comps) - 2)

            return '.'.join(url_comps)
        except (IndexError, AttributeError):
            return None

    def extract_next(self):
        '''
        extract the url of the next page using the existing next button
        '''
        next_url = self.d(self.next_selector).attr('href')
        if not next_url:
            print 'No more images left in the album'
            return ''
        else:
            if re.match('^https*://', next_url):
                return next_url
            elif re.match('^#\d+$', next_url):
                return self.url.replace(self.url[self.url.rfind('#'):], next_url)
            else:
                return 'http://' + self.base + next_url

