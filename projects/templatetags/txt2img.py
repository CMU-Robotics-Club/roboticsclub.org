#
# Obtained from:
# https://djangosnippets.org/snippets/2737/
#

# TODO: move this out of projects app

from django.conf import settings
from django.template import Library

from PIL import Image, ImageDraw, ImageFont
from os import path
import hashlib
import os

register = Library()

@register.filter
def txt2img(text,font_size=14,bg="#ffffff",fg="#000000",font="Roboto-Light.ttf"):
    '''
    txt2img tag shows on the web text as images, helping to avoid get
    indexed email address and     some other information you don't want
    to be on search engines. Fonts should reside in the same folder of txt2img.
    
    Usage:
    {{worker.email|txt2img:18|safe}}
    '''

    image_dir = settings.MEDIA_ROOT+"/txt2img/"   # Set the directory to store the images

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    img_name="{}.jpg".format(hashlib.md5(text.encode('utf8')).hexdigest())

    if path.exists(image_dir+img_name): # Make sure img doesn't exist already
        pass
    else:
        font_path = "{}/fonts/{}".format(settings.STATIC_ROOT, font)
        font = ImageFont.truetype(font_path, font_size)

        w, h = font.getsize(text)
        img = Image.new('RGBA', (w, int(1.2*h)), bg)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), text, font=font, fill=fg)
        img.save(image_dir+img_name,"JPEG",quality=100)  
    
    imgtag = '<img src="'+settings.MEDIA_URL+'txt2img/'+img_name+'" alt="'+text+'" />'
    return imgtag
