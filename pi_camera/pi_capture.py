#!/usr/bin/env python3
import picamera

def take_screenshot(filename,resolution):
    '''
    Take screenshot and save the image in jpg
    '''

    camera = picamera.PiCamera()

    if resolution is not None:
        camera.resolution = resolution

    camera.capture('{}'.format(filename))
    camera.close()
