import re
import requests
from bs4 import BeautifulSoup

site = 'https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628990-7950'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img', attrs={'class': "galleryimage gallery-items"})

urls = [img['src'] for img_tags]
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url: 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
