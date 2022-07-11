import numpy as np
import math
import string
import random
import time
from Rotor import Rotor
from Plugboard import Plugboard
from Reflector import Reflector

class Enigma():
    def __init__(self, Rotor_number=3, state_seed_list=None, Plug_pair=13, Plug_seed=None):
        '''Simulation for a Enigma
        :param Rotor_number: {int} Used Rotor number (default is 3, like real Enigma)
        :param state_seed_list: {List}
            take 3 Rotors for example, state_seed_list should like
            [[state_1, seed_1], 
            [state_2, seed_2], 
            [state_3, seed_3]]
        :param Plug_pair: {int} Used Plug pairs number
        :return: {Enigma object}
        '''
        # initialize Rotors
        self.RotorList = []
        if state_seed_list is not None:
            if len(state_seed_list) != Rotor_number:
                raise ValueError(f'length of state_seed_list should equal to Rotor_number, but got {len(state_seed_list)} and {Rotor_number}')
            for i in range(Rotor_number):
                self.RotorList.append( Rotor(state=state_seed_list[i][0], seed=state_seed_list[i][1]) )
        else:
            for i in range(Rotor_number):
                self.RotorList.append( Rotor(state=0, seed=None) )
        # initialize Plugboard 
        self.plugboard = Plugboard(amount=Plug_pair, seed=Plug_seed)
        # initialize Reflector
        self.reflector = Reflector()
    
    def EnDecrypt(self, words):
        '''Method for Encryption and Decryption
        :param words: {string} input message
        :return: {string} output message
        '''
        result = ''
        for word in words:
            # Plugboard changing first
            middle_word1 = self.plugboard.change(word)
            # Rotors convertion first
            temp = middle_word1
            for rotor in self.RotorList:
                temp = rotor.convert(temp)
            middle_word2 = temp
            # Reflector
            middle_word3 = self.reflector.reflect(middle_word2)
            # Rotors convertion second
            temp = middle_word3
            for rotor in self.RotorList[::-1]:
                temp = rotor.reverse_convert(temp)
            middle_word4 = temp
            # Plugboard changing second
            result_word = self.plugboard.change(middle_word4)
            
            result += result_word
            
            # Shift rotor state
            for rotor in self.RotorList:
                if rotor._shift_state() == 0:
                    pass
                else:
                    break
        return result
    
    def re_initialization(self):
        '''Method for setting Rotors to the original state (Easy for experiment)'''
        for rotor in self.RotorList:
            rotor._re_initialization()
            
if __name__ == '__main__':
    state_seed_list = [[2, 87], [8, 187], [15, 287]]
    #state_seed_list = [[0, 87]]
    
    TestEnigma = Enigma(Rotor_number=3, state_seed_list=state_seed_list, Plug_pair=13, Plug_seed=387)
    # Encryption
    TestMessage1 = 'This is a test message'
    print(TestMessage1)
    TestMessage2 = TestEnigma.EnDecrypt(TestMessage1)
    print(TestMessage2)
    
    TestEnigma.re_initialization()
    # Decryption
    TestMessage3 = TestEnigma.EnDecrypt(TestMessage2)
    print(TestMessage3)