import numpy as np
import math
import string
import random
import time

class Reflector():
    def __init__(self):
        '''Simulation for a Reflector in Enigma
        :return: {Reflector object}
        '''
        temp_word_list = string.ascii_lowercase + ' '
        self._reflect_table = {}
        for word1, word2 in zip(temp_word_list, temp_word_list[::-1]):
            self._reflect_table[word1] = word2
    
    def reflect(self, word):
        '''Method for reflecting the input word
        :param word: {chac} input word
        :return: reflected word
        '''
        return self._reflect_table[word]
    
if __name__ == '__main__':
    TestReflector = Reflector()
    print(TestReflector.reflect('g'))