__author__ = 'omic'
from templates import Publisher, Subscriber

class KwiterScaner(Publisher):
    def __init__(self, scan_list):
        super().__init__()
        self.__scan_list = scan_list

    def scan(self):
        print('scan')


class KwiterJober(Subscriber):
    pass