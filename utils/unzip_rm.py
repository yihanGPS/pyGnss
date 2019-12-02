#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:23:05 2017

@author: Sebastijan Mrak <smrak@gmail.com>
"""

import glob
import os
import subprocess
import platform

def unzip(f, timeout=5, delete=True):
    head, tail = os.path.split(f)
    if platform.system() in ('Linux', 'Darwin'):
        try:
            if delete:
                subprocess.call('gzip -d -f -q ' + f, shell=True,timeout=timeout)
            else:
                subprocess.call('gzip -f -q ' + f, shell=True,timeout=timeout)
        except:
            print ('Problems with: ',tail)
    elif platform.system() == 'Windows':
        try:
            subprocess.call('7z x "{}" -o"{}"'.format(f, head), shell=True,timeout=timeout)
            if delete:
                subprocess.call('del "{}"'.format(f), shell=True,timeout=timeout)

        except:
            print ('Problems with: ',tail)
    return

def unzipfolder(folder, timeout=5, delete=True):
    suffix = ['*.gz', '*.Z', '*.zip']
    for wlstr in suffix:
        filestr = os.path.join(folder,wlstr)
        flist = sorted(glob.glob(filestr))
        c = 1
        for file in flist:
            print('Unizipping: ' +str(c) + '/'+str(len(flist)+1))
            unzip(file, timeout, delete=delete)
            c+=1

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('folder',type=str)
    p.add_argument('-d', '--delete', help='delete after unzip. Default is True', action='store_false')
    p.add_argument('-t', '--timeout', help='timeout time, Default= 5 seconds', type=int, default=5)
    P = p.parse_args()
    
    unzipfolder(P.folder, P.timeout, delete=P.delete)
