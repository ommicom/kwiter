__author__ = 'omic'
import os
import re
import logging
import multiprocessing
from templates import Publisher, Subscriber

class KwiterScaner(Publisher):
    def __init__(self, scan_list, logger):
        super().__init__()
        self.__scan_list = scan_list
        self.__logger = logging.getLogger('.'.join(('kwiter', logger)))

    def scan(self):
        dat = {'files':(), 'actor':()}
        files = list()
        for scan_job in self.__scan_list:
            for mask in scan_job['mask']:
                files.extend([os.path.join(scan_job['scan_dir'], files) for files in os.listdir(scan_job['scan_dir']) if re.findall(mask, files)])

            self.notify({'files':files, 'actor':scan_job['actor']})


class KwiterJober(Subscriber):
    def __init__(self, modules, logger):
        self.__queuejobs = multiprocessing.Queue()
        self.__modules = modules
        self.__logger = logging.getLogger('.'.join(('kwiter', logger)))

    def notification(self, dat):
        self.__queuejobs.put(dat)
        p = multiprocessing.Process(target=self.run())
        p.start()
        p.join()

    def run(self):
        while not self.__queuejobs.empty():
            jobs = self.__queuejobs.get()
            files = jobs['files']
            module_result = None
            for actor in jobs['actor']:
                try:
                    files, module_result = self.__modules[actor].run(files, module_result)
                except KeyError:
                    self.__logger.error('Try load not define module %s' % jobs['actor'])

