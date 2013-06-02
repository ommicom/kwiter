__author__ = 'ommicom'

import os
import glob

def run(files, mod_result=None):
    sett = __import__('set_kwt')
    try:
        os.chdir(sett.source_dir)
        for kwt in glob.glob(sett.mask):
            print(kwt)
    except EnvironmentError:
        pass

    return files, mod_result