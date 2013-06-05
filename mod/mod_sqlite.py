__author__ = 'ommicom'
import sqlite3

def run(files, mod_result=None):
    sett = __import__('set_sqlite')
    try:
        db = sqlite3.connect(sett.db,  check_same_thread=False)
    finally:
        db.close()
    return files, mod_result