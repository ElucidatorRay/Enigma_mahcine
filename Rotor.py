import numpy as np
import math
import string
import random
import time

class Rotor():
    def __init__(self, state=0, seed=None):
        '''Simulation for a Rotor in Enigma
        :param state: {int} current state of this rotor, default is 0
        :param seed: {int} seed for randomly initializing convert table
        :return: {Rotor object} Initialized Rotor
        '''
        # initialize the converting table
        self._initialize_LETTER_NUMBER_dict()
        
        # initialize starting state
        self._init_state = state
        self._state = state
        
        # initialize a non-overlapping convert table
        while True:
            # set random seed for shuffling relation of Rotor
            if seed is not None:
                random.seed(seed)
            else:
                random.seed(int(round(time.time(), 0)))
            I = list(range(27))
            O = list(range(27))
            random.shuffle(O)
            # checking if there are overlapping term
            if self._same_position(I, O):
                # if so, changing random seed and do the initialization again
                seed += 1
                time.sleep(0.5)
                continue
            else:
                # if not, break
                break
        self._convert_table = dict(zip(I, O))
        self._reverse_convert_table = dict(zip(O, I))
    
    def convert(self, word):
        '''Method for converting message based on current state and convert table
        :param word: {chac} input word
        :return: {chac} convert result
        '''
        # convert word to number first
        word_init_number = self.LETTER_TO_NUMBER[word.lower()]
        # add state to number for simulating Rotor
        word_number = (word_init_number + self._state) % 27
        # convert word number by Rotor convert table
        word_number = self._convert_table[word_number]
        
        return self.NUMBER_TO_LETTER[word_number]
       
    def reverse_convert(self, word):
        '''Method for reverse converting message based on current state and convert
        :param word: {chac} input word
        :return: {chac} convert result
        '''
        # convert word to number first
        word_init_number = self.LETTER_TO_NUMBER[word]
        # convert word number by Rotor convert table
        word_number = self._reverse_convert_table[word_init_number]
        # reverse the state change effect
        word_number -= self._state
        if word_number < 0:
            word_number += 27
        
        return self.NUMBER_TO_LETTER[word_number]
    
    def _initialize_LETTER_NUMBER_dict(self):
        '''Method for generate mapping tables between letters and numbers
        '''
        self.LETTER_TO_NUMBER = {}
        self.NUMBER_TO_LETTER = {}
        
        for word, number in zip((string.ascii_lowercase + ' '), range(27)):
            self.LETTER_TO_NUMBER[word] = number
            self.NUMBER_TO_LETTER[number] = word
    
    def _same_position(self, I, O):
        '''Method for checking relation between input and output has overlapping
        :param I: {List} generated input List 
        :param O: {List} generated output List 
        :return: {bool} True for overlapping and False for non-overlapping
        '''
        for term1, term2 in zip(I, O):
            if term1 == term2:
                return True
        return False
    
    def _shift_state(self):
        '''Method for shifting current state to next position
        :return: {int} new state for this Rotor
        '''
        self._state = (self._state + 1) % 27
        return self._state
    
    def _re_initialization(self):
        '''Method for setting the Rotor to the original state (Easy for experiment)'''
        self._state = self._init_state

if __name__ == '__main__':
    TestRotor = Rotor(state=10, seed=87)
    print(TestRotor._convert_table)
    print(TestRotor._state)