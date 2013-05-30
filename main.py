__author__ = 'omic'
__version__ = '0.0.2'

import sys
import argparse
import logging
import settings

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
    subparser = parser.add_subparsers(dest='command_name', help='command')

    init_parser = subparser.add_parser('init', help='init db')

    log_parser = subparser.add_parser('logger', help='loging setings')
    log_parser.add_argument('-n', '--name', default='kwiter', help='define logger name')
    log_parser.add_argument('-l', '--level', default='error', choices=['debug', 'info', 'error', 'critical', 'notset'], help='define logger name')
    log_parser.add_argument('-o', '--output', default='file', help='define logger name')

    args = parser.parse_args()

    print(vars(args))

    # try:
    #     sett = __import__(args.settings)
    # except ImportError:
    #     log = logging.getLogger()
    #     log.setLevel(LOG_LEVEL['ERROR'])
    #     log.addHandler(logging.StreamHandler(sys.stdout))
    #     log.handlers[0].setFormatter(LOG_FORMAT)
    #     log.exception('Settings %s not load' % args.settings)


if __name__ == '__main__':
    sys.exit(main())