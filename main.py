#!/usr/bin/env python3

from preprocessing import get_suffix

from s3push.s3push import  s3_upload

from pi_camera.pi_capture import take_screenshot
# from lepton_camera.lepton_capture import capture_image

def main(resolution=(1296, 972,)):
    outputdir = 'img'

    suffix_picamera = get_suffix(outputdir,'picamera')
    # suffix_lepton = get_suffix(outputdir,'lepton')
    filename = '{}/picamera_{}.jpg'.format(outputdir,suffix_picamera)

    take_screenshot(filename,resolution)
    # capture_image('{}/lepton_{}.jpg'.format(outputdir,suffix_lepton), resolution)

    s3_upload(filename)

if __name__ == '__main__':
    main()
