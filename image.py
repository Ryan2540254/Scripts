#!/usr/bin/env python3

import PIL
from PIL import Image

"""Python Script that Shows the various uses of the PIL module."""
name = input('Enter the name of the Image:')
im   = Image.open(name)
im.rotate(45).show
