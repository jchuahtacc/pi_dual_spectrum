#!/usr/bin/env python3

from time import time
from glob import glob
import numpy as np
from os.path import basename,splitext

def get_file_number(filepath):
    '''
    Get the number in filename in case ntp time is not working
    '''
    filename,_ = splitext(basename(filepath))
    return int(filename.split('_')[1])

def is_ntp_working():
    try:
        import ntplib
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        return True
    except:
        return False

def get_suffix(outputdir,pattern):
    '''
    Get suffix for picture name
    '''
    if is_ntp_working():
        return time()
    else:
        files = glob('{}/{}'.format(outputdir,pattern))
        return np.max(list(map(get_file_number,files)))+1

if __name__ == '__main__':
    take_screenshot()
