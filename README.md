# Enigma machine
This is python-based implementation of [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine), a kind of cipher device used by Nazi Germany in WII.

## Inspired by
This code is inspired by [How did the Enigma Machine work?](https://www.youtube.com/watch?v=ybkkiGtJmkM&t=467s). They represent complete operation of Enigma machine by really great animation. And It is very helpful for me to comprehenze.

## Required library
The only library you need to install is numpy. Using ```pip``` or ```conda``` to install it.
```sh
pip install numpy
conda install numpy
```

## Program tructure
There are totally four ```.py``` file in this implementation. "Rotor.py", "Plugboard.py", "Reflector.py" and "Enigma.py" represent different part with same name in a real Enigma machine respectively.<br>
__REMARK: Below only mention method which are designed for calling by user.__

* Rotot.py
    * ```__init__(state, seed)```: Constructor, Initialization contains the convert table of this rotor (decided by input random seed and start position).
    * ```convert(word)```: Convert input word into another word based on current state and convert table.
    * ```reverse_convert(word)```: The opposite convertion for decoding.

* Plugboard.py
    * ```__init__(amount, seed)```: Constructor, Initialization contains mapping amount and relation of this plugboard(decided by input random seed)
    * ```change(word)```: Do the word swapping based on changing table.

* Reflector.py
    * ```__init__()```: Constructor, Initialization contains reflection table. Here, I hard coded it with mapping to the reverse sort.
    * ```reflect(word)```: Do the word reflection based on reflection table.

* Enigma.py
    * ```__init__(Rotor_number=3, state_seed_list=None, Plug_pair=13, Plug_seed=None)```: Constructor, Initialization contains each parts mentioned above(Rotor, Plugboard and Reflector) based on input seed and number.
    * ```EnDecrypt(words)```: Doing Encryption or Decryption, converting text into cipher or the opposite.
    * ```re_initialization()```: Reset all Enigma machine for easy En/Decryption.

## How to use
Using below command to run each ```.py``` file and get result based on our testing. 
```sh
python Rotor.py
pyhton Plugboard.py
python Reflector.py
python Enigma.py
```
The test message is __"This is a test message"__. If you run ```Enigma.py``` by above command, you will receive cipher of __"zkaisp nnxraumctzrustn"__.
