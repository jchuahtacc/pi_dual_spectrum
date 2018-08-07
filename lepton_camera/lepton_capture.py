import numpy as np
from pylepton import Lepton
from PIL import Image
from PIL import BICUBIC


def capture_image(filename, size):
    with Lepton() as l:
        a,_ = l.capture()

    #Create a PIL image from numpy array
    image = Image.fromarray(a.astype('uint8'), 'RGB')

    #resize PIL image to match picamera resolution
    image = image.resize(size, BICUBIC)

    image.save(filename, 'JPEG')