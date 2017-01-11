'''
lux-img main script

author @abekim
'''
import models, request, time

URL = raw_input('Enter the URL of the first image: ')
ALBUM_NAME = raw_input('Enter the album name: ')
DIR_NAME = raw_input('Enter the directory name (leave blank to use album name): ')
IMAGE_SELECTOR = raw_input('Enter the image selector to search for: ')
NEXT_SELECTOR = raw_input('Enter the next selector to search for: ')

# extract album name
URL_COMPONENTS = URL.split('/')
ALBUM_NAME = ALBUM_NAME if ALBUM_NAME else URL_COMPONENTS[URL_COMPONENTS.index('album')+1]

# instantiate album
ALBUM = models.Album(ALBUM_NAME, DIR_NAME)
current_page = request.Page(URL, {'image': IMAGE_SELECTOR, 'next': NEXT_SELECTOR})

running = True

startTime = time.time()
flushTimer = time.time()

totalCount = 0

while running:
    img_url = current_page.extract_img()

    # if for some reason, we have an error where we can't parse the image
    if not img_url:
        continue

    # save extracted img
    ALBUM.save(img_url)
    totalCount += 1

    if totalCount % 10 == 0 and totalCount != 0:
        print "Saved 10 images in %s seconds" % (round(time.time() - flushTimer, 3))
        time.sleep(3)    # Sleep for 3 seconds
        flushTimer = time.time()    # reset flushTimer

    next_page = current_page.extract_next()
    if not len(next_page):
        running = False
    else:
        current_page = request.Page(next_page, {'image': IMAGE_SELECTOR, 'next': NEXT_SELECTOR})

print "Album download complete.\nTotal number of images: %s\nTotal time: %s seconds" % (totalCount, round(time.time() - startTime, 3))

