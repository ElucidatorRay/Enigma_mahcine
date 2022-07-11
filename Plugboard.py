import numpy as np
import math
import string
import random
import time


class Plugboard():
    def __init__(self, amount=13, seed=None):
        '''Simulation for Plugboard in Enigma
        :param amount: {int} changing pair for 26 alphabets and space (totally 27 possible input)
        :param seed: {int} seed for randomly initializing changing pair
        :return: {Plugboard object} Initialized Plugboard
        '''
        # check amount type and magitude
        if type(amount) != int:
            raise TypeError(f'amount must be an integer, but got {amount}')
        if amount > 13 or amount < 0:
            raise ValueError(f'amount of Plug must smaller than 13 and bigger than 0, but got {amount}')
        self._amount = amount
        # initialize chaning pair
        if seed is not None:
            random.seed(seed)
        else:
            random.seed(int(round(time.time(), 0)))
        including_words = random.sample(string.ascii_lowercase + ' ', self._amount*2)
        random.shuffle(including_words)
        self._changing_table1 = {}
        self._changing_table2 = {}
        for word1, word2 in zip(including_words[:self._amount], including_words[self._amount:]):
            self._changing_table1[word1] = word2
            self._changing_table2[word2] = word1
    
    def change(self, word):
        '''Method for changing input word to another word
        :param word: {chac} input word
        :return: {chac} changing result 
        '''
        if word.lower() in self._changing_table1.keys():
            return self._changing_table1[word.lower()]
        elif word.lower() in self._changing_table2.keys():
            return self._changing_table2[word.lower()]
        else:
            return word.lower()
    
    def __repr__(self):
        '''Method for pring out all changing pairs
        :return: {string} the changing pairs
        '''
        _return = ''
        for key, value in zip(self._changing_table1.keys(), self._changing_table1.values()):
            _return += f'{key} <--> {value}'
            _return += '\n'
        return _return[:-1]

if __name__ == '__main__':
    TestPlugboard = Plugboard(amount=13, seed=87)
    print(TestPlugboard)
    print('----------------------')
    print(TestPlugboard.change(' '))