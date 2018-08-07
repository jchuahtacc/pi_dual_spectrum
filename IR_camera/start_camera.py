#!/usr/bin/env python3

import picamera

def take_screenshot(filename):
    '''
    Take screenshot and save the image in jpg
    '''

    camera = picamera.PiCamera()
    camera.capture('{}/{}'.format(filename))

if __name__ == '__main__':
    take_screenshot()
