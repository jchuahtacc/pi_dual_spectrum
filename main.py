#!/usr/bin/env python3

from time import time

from preprocessing import get_suffix

from pi_camera.pi_capture import take_screenshot
from lepton_camera.lepton_capture import capture_image

def main():
    outputdir = './'

    suffix_picamera = get_suffix(outputdir,'picamera')
    suffix_lepton = get_suffix(outputdir,'lepton')

    take_screenshot('{}/picamera_{}.jpg'.format(outputdir,suffix_picamera))
    capture_image('{}/lepton_{}.jpg'.format(outputdir,suffix_lepton))


if __name__ == '__main__':
    main()
