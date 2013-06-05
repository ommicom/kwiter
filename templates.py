# -*- coding: utf-8 -*-

#Collection implementation of templates
#http://ru.wikipedia.org/wiki/Наблюдатель_(шаблон_проектирования)#Python

__author__ = 'Omic'
__version__ = '0.0.1'

class Publisher():
    subscribers = None
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, Subscriber):
        self.subscribers.add(Subscriber)

    def unsubscribe(self, Subscriper):
        self.subscribers.remove(Subscriber)

    def notify(self, dat):
        for subscriber in self.subscribers:
            subscriber.notification(dat)

class Subscriber():
    def __init__(self):
        pass

    def notification(self, dat):
        pass
#Observer


#Singleton
class Singleton:
    class __impl:
        def test(self):
            return id(self)

    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__impl()
        self.__dict__['Singleton_instance'] = Singleton.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
#Singleton
