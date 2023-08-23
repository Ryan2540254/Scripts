#!/usr/bin/env python3

import PIL
from PIL import Image

"""Python Script that Shows the various uses of the PIL module."""
name = input('Enter the name of the Image:')
im   = Image.open(name)


def rotate_image():
    new_im   = im.rotate(45)
    new_name = input('Enter the new name of the Image:')
    new_im.save(new_name)
def resize_image():
    new_imm  = im.resize((640,480))
    new_name = input('Enter the new name of the Image:')
    new_im.save(new_name)
def rotate_and_resize_image():
    new_name = input('Enter the new name of the Image:')
    im.rotate(180).resize((640,480)).save(new_name)

print('Current options:rotate,resize,both')
ans = input('Which operation would you like to do on the image:')
if ans.lower() == 'rotate':
   rotate_image()
elif ans.lower() == 'resize':
   resize_image()
elif ans.lower() == 'both':
   rotate_and_resize_image()
else:
    print('Enter a valid input')
