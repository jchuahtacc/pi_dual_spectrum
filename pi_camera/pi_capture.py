#!/usr/bin/env python3
import picamera

def take_screenshot(filename,resolution):
    '''
    Take screenshot and save the image in jpg
    '''

    camera = picamera.PiCamera()
    camera.resolution = resolution
    camera.capture('{}/{}'.format(filename))

if __name__ == '__main__':
    take_screenshot()
