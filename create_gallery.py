from dominate import document
from dominate.tags import *
import os, yaml, json, requests

with open('./keys.yml') as f:
    keys = yaml.safe_load(f)

API_KEY = keys['cloudinary_api']
SECRET_KEY = keys['cloudinary_secret']

req = ''
req += 'https://'
req += API_KEY
req += ':'
req += SECRET_KEY
req += '@'
req += 'api.cloudinary.com/v1_1/itko/resources/image/upload/?prefix=eventu/posters&max_results=50'
res = requests.get(req)

images = json.loads(res.content)['resources']

d = document()

head = d.head
d.title = 'Eventu'

with head:
    meta(charset='utf-8')
    link(href='gallery.css', type = 'text/css', rel='stylesheet')
    script(src="https://code.jquery.com/jquery-3.2.1.min.js")
    script(src="lazysizes.min.js")


with d:
    gallery = div(id='content').add(div(cls='gallery'))
    script(src='shuffle.js')

with gallery:
    root = 'https://res.cloudinary.com/itko/image/upload/'
    for i,im in enumerate(images):
        data_src = root + 't_prog2560/' + im['public_id']
        src = root + 't_blur32/' + im['public_id']
        fig = figure(cls='photo-figure')
        with fig:
            a(href='LINK').add(img(cls='lazyload',id=im['public_id'].replace('/','-'),src=src,data_src=data_src))


with open('./index.html', 'w+') as f:
    f.write(str(d))
