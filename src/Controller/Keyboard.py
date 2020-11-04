'''
File: Keyboard.py
Created Date: Tuesday, November 2nd 2020, 6:08:10 pm
Author: Zentetsu

----

Last Modified: Wed Nov 04 2020
Modified By: Zentetsu

----

Project: HCore
Copyright (c) 2020 Zentetsu

----

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

----

HISTORY:
2020-11-04	Zen	Adding Keybard class with key listener
'''


from getkey import getkey, keys
import time
from pynput.keyboard import Listener, Key

class Keyboard:
    def __new__(cls, verbose=False):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.Keyboard(verbose)

        return cls.instance

    def Keyboard(self, verbose):
        self.verbose = verbose

        self.command = {'z': False, 'q': False, 's': False, 'd': False, 'p': False, 'esc': False}

    def readInput(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        try:
            if key.char in self.command:
                self.command[key.char] = True
        except:
            if key == Key.esc:
                self.command['esc'] = True
                return False

    def on_release(self, key):
        try:
            if key.char in self.command:
                self.command[key.char] = False
        except:
            pass

    def getInput(self):
        return self.command