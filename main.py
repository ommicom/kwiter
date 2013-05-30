__author__ = 'omic'
__version__ = '0.0.2'

import sys
import argparse
import logging
import settings
from kwitter import KwiterJober, KwiterScaner
from mtimer import Timer

#LOG_HANDLER = {'FILE': logging.FileHandler(flog_name), 'CON': logging.StreamHandler(sys.stdout),
#               'TMROTATE': logging.handlers.TimedRotatingFileHandler(flog_name, when='midnight'),
#               'SZROTATE': logging.handlers.RotatingFileHandler(flog_name, maxBytes=1024)}
LOG_FORMAT = logging.Formatter('%(asctime)s\t%(levelname)s\t%(lineno)d\t%(message)s')
# LOG_HANDLER = {'FILE':logging.FileHandler(args.log_file),'CON':logging.StreamHandler(sys.stdout)}
LOG_LEVEL = {'DEBUG':logging.DEBUG,'INFO':logging.INFO,'WARNING':logging.WARNING,'ERROR':logging.ERROR,'CRITICAL':logging.CRITICAL,
             'NOTSET':logging.NOTSET}


def main():
    parser = argparse.ArgumentParser(prog='kwiter', usage='%(prog)s [options]')
    parser.add_argument('-v', '--version', action='version', help='print version', version='kwiter %s' % __version__)
    parser.add_argument('-s', '--settings', action='store', default='settings', help='define settings name')

    args = parser.parse_args()
    try:
        sett = __import__(args.settings)
    except ImportError:
        log = logging.getLogger()
        log.setLevel(LOG_LEVEL['ERROR'])
        log.addHandler(logging.StreamHandler(sys.stdout))
        log.handlers[0].setFormatter(LOG_FORMAT)
        log.exception('Settings %s not load' % args.settings)
        return 1

    logger_name = sett.log_settings.get('name', 'kwiter')
    log_level = LOG_LEVEL[sett.log_settings.get('level').upper()] if sett.log_settings.get('level').upper() in LOG_LEVEL.keys() else LOG_LEVEL['ERROR']
    try:
        log_out = {'FILE':logging.FileHandler('.'.join((logger_name, 'log'))),
                   'CON':logging.StreamHandler(sys.stdout)}[sett.log_settings.get('out', 'FILE').upper()]
    except KeyError:
        log_out = logging.FileHandler('.'.join((logger_name, 'log')))

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.addHandler(log_out)
    logger.handlers[0].setFormatter(LOG_FORMAT)

    try:
        cycle = sett.cycle if isinstance(sett.cycle, int) else 60
    except AttributeError:
        cycle = 60

    scaner = KwiterScaner()
    jober = KwiterJober()
    tm = Timer(scaner.scan, cycle)
    tm.start()

    scaner.subscribe(jober)

if __name__ == '__main__':
    sys.exit(main())