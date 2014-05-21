'''
lux-img main script

author @abekim
'''
import models, request, time

URL = raw_input('Enter the URL of the first image: ')
DIR_NAME = raw_input('Enter the directory name (leave blank to use album name): ')

# extract album name
URL_COMPONENTS = URL.split('/')
ALBUM_NAME = URL_COMPONENTS[URL_COMPONENTS.index('album')+1]

# instantiate album
ALBUM = models.Album(ALBUM_NAME, DIR_NAME)

running = True

startTime = time.time()
flushTimer = time.time()

totalCount = 0

while running:
    current_page = request.Page(URL)

    img_url = current_page.extract_img()

    if not img_url:
        continue

    ALBUM.save(img_url)
    totalCount += 1

    if totalCount % 10 == 0 and totalCount != 0:
        print "Saved 10 images in %s seconds" % (round(time.time() - flushTimer, 3))
        flushTimer = time.time()    # reset flushTimer

    current_page = request.Page(current_page.extract_next())
    
    if not current_page:
        running = False

print "Album download complete.\nTotal number of images: %s\nTotal time: %s" % (totalCount, round(time.time() - startTime, 3))

