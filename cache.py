import functools
from datetime import datetime, timedelta


class memoized(object):
    """
        Simple decorator that caches the functions return value each time it's 
        called. If called later with different arguments, a new re-evaluation will 
        be done, and the return value will be cached for further reference.

        UPDATE: added timeout feature, specifying when a cache should timeout and 
            re-evaluate its value.
    """
    def __init__(self, fn, seconds=0, minutes=0, hours=1, days=0):
        self.fn = fn
        self.cache = {}
        self._timedelta = timedelta(seconds=seconds,
                                    minutes=minutes,
                                    hours=hours,
                                    days=days)

    def __call__(self, *args):
        try:
            entry = self.cache[args]
            if self.is_outdated(entry):
                # entry outdated, update cache entry
                entry = {'val' : self.fn(*args), 'time':datetime.now()}
                self.cache.update(entry)
            return entry.get('val')
        except KeyError:
            # does not exists in cache, therefor add it
            value = self.fn(*args)
            self.cache[args] = {'val' : value, 'time' : datetime.now()}
            return value
        except TypeError:
            # bad key type (*args), therefor simply evaluate and return
            return self.fn(*args)


    def is_outdated(self, entry):
        """
            Check cache entry if its invalid due to timeout.
        """
        if datetime.now() - entry.get('time') > self._timedelta:
            return True
        return False

    
    def __repr__(self):
        return self.fn.__doc__

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)
