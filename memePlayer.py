from pynput.keyboard import Key, Listener
from playsound import playsound
import os

class myPlayer:
    def __init__(self, path_to_sounds_stock):
        self.path_to_sounds_stock = path_to_sounds_stock
        self.keys = []
        self.playing = False
        self.sounds = []

        self.cmds = {
            '&' : 0,
            'é' : 1,
            '\"' : 2,
            '\'' : 3,
            '(' : 4,
            '-' : 5,
            'è' : 6,
            '_' : 7,
            'ç' : 8,
            'à' : 9
            }

        self.load_config()
        

        with Listener(on_press = self.keypress, on_release = self.keyrelease) as listener:
            listener.join()

    def load_config(self):
        for sound in os.listdir(self.path_to_sounds_stock):
            if sound != '':
                self.sounds.append('{}/{}'.format(self.path_to_sounds_stock,sound))
        print()
        self.print_keys()
        print()

    def keypress(self, Key):
        if Key not in self.keys:
            self.keys.append(Key)
            self.check_combination()

    def keyrelease(self, Key):
        if Key in self.keys:
            self.keys.remove(Key)

    def play(self, sound):
        print('Playing {}'.format(self.sounds[sound].split('/')[-1]))
        playsound(self.sounds[sound], block=False)

    def print_keys(self):
        for key in range(len(self.sounds)):
            print('| shift + alt_l + {} | ==> {}'.format(self.method1(key),self.sounds[key].split('/')[-1]))

    def method1(self,searched_index):
        for symbol,index in self.cmds.items():
            if index == searched_index:
                return symbol

    def check_combination(self):
        if Key.shift in self.keys and Key.alt_l in self.keys and len(self.keys) > 2:
            try:
                symbol = self.keys[-1].char
                if self.cmds[symbol] < len(self.sounds):
                    self.play(self.cmds[symbol])
                else:
                    pass
            except:
                pass
            


player = myPlayer('./../../sounds')

