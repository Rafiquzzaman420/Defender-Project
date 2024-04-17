from linecache import getline

from file_scanner import length, LetterFinder
from info_store_class import info_store


class info_storer:
    @staticmethod
    def opener():  # before calling this function, the "storer()" function from 'file_scanner.py' must be called
        letter_length = range(length)
        for number in letter_length:
            info = (getline('letters.def', number + 1))[0:1]
            info = info + ':\\'
            info_store.info_store(info)


LetterFinder.storer()
info_storer.opener()
