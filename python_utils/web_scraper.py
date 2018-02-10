import collections
import urllib
import urllib2
from bs4 import BeautifulSoup
import os

FILE_PATH = '/Users/cindy/Desktop/save-the-fishes/static/fishes/'

fishes = collections.defaultdict(dict)
url = urllib2.urlopen('http://www.fishbase.org/Country/CountryChecklist.php?c_code=840&vhabitat=commercial&csub_code=US-NY').read()
soup = BeautifulSoup(url)
fish_table = soup.find('table', {'class': 'commonTable'})
rows = fish_table.findAll('tr')[1:]
for row in rows:
    td = row.findAll('td')
    family = td[1].string
    species = td[2].string
    for link in td[2].findAll('a'):
        info_url = urllib2.urlopen('http://www.fishbase.org/Country/%s' % link['href']).read()
        info = BeautifulSoup(info_url)
        headings = info.findAll('span')
        for heading in headings:
            # Add fish information to species
            if 'Max length' in heading.text:
                if not os.path.isdir('%s%s/%s' % (FILE_PATH, family, species)):
                    os.makedirs('%s%s/%s' % (FILE_PATH, family, species))

                with open('%s%s/%s/%s_size.txt' % (FILE_PATH, family, species, species), 'w') as f:
                    f.write(heading.text)

    img_url = urllib2.urlopen('http://www.fishbase.org/photos/ThumbnailsSummary.php?Genus=%s&Species=%s' % (species.split()[0], species.split()[1])).read()
    imgs = BeautifulSoup(img_url)
    for img in imgs.findAll('img'):
        print img
        if 'thumbnails' in img['src']:
            image_url = ('http://www.fishbase.org%s' % img['src'][2:])
            image_name = img['src'].rsplit('/', 1)[1]
            urllib.urlretrieve(image_url, '%s%s/%s/%s' % (FILE_PATH, family, species, image_name))
