#!/usr/bin/env python3

from datetime import datetime
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
        return datetime.now().strftime('%Y%m%d%H%M%S')
    else:
        files = glob('{}/{}'.format(outputdir,pattern))
        if len(files)>0:
            return np.max(list(map(get_file_number,files)))+1
        else:
            return 0
