'''
File: ControllerPS3.py
Created Date: Wednesday, October 3rd 2020, 11:08:15 pm
Author: Zentetsu

----

Last Modified: Mon Nov 02 2020
Modified By: Zentetsu

----

Project: HController
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
'''


import time
import os.path


class ControllerPS3:
    def __new__(cls, path, verbose=False):
        if not os.path.isfile(path):
            return -1

        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.ControllerPS3(path, verbose)

        return cls.instance

    def ControllerPS3(self, path, verbose):
        self.verbose = verbose

        if self.verbose:
            print("-------- CREATE CONTROLLER ---------")

        self.verbose = verbose

        self.joy = { 'leftx': 0.0, 'lefty': 0.0, 'rightx': 0.0, 'righty': 0.0,
                     'trig0': False, 'trig1': False, 'trig2': False, 'trig3': False,
                     'buttonup': False, 'buttondown': False, 'buttonleft': False, 'buttonright': False,
                     'triangle': False, 'circle': False, 'cross': False, 'square': False,
                     'select': False, 'start': False, 'ps': False}

        self.path = path
        self.action = []

        self.setStatus(2)
        # self.pairing(self.path)

    def pairing(self, path):
        self.printMessage(3)
        search = True
        wait = 0

        while search:
            try:
                self.pipe = open(path, 'rb')

                self.readInput()
                self.setStatus(1)

                search = False
            except:
                time.sleep(1)
                wait += 1

                if wait > 5:
                    self.setStatus(2)
                    cont = input("WARNING: Controller disconnected. Do you want to continue ?(yes/no): ")
                    wait = 0

                    if cont == "no":
                        search = False
                    else:
                        self.printMessage(3)

    def readInput(self):
        global reading
        self.printMessage(1)

        reading = True

        try:
            while reading:
                for character in self.pipe.read(1):
                    self.action += ['%02X' % character]
                    if len(self.action) == 8:

                        num = int(self.action[5], 16)
                        percent254 = str(((float(num)-128.0)/126.0)-100)[4:6]
                        percent128 = str((float(num)/127.0))[2:4]

                        if percent254 == '.0':
                            percent254 = '100'
                        if percent128 == '0':
                            percent128 = '100'

                        if self.action[6] == '01':
                            if self.action[4] == '01':
                                if self.action[7] == '04':
                                    self.joy['trig0'] = True
                                    if self.verbose:
                                        print("trig0")
                                if self.action[7] == '05':
                                    self.joy['trig1'] = True
                                    if self.verbose:
                                        print("trig1")
                                # if self.action[7] == '08':
                                #     self.joy['trig2'] = True
                                #     if self.verbose:
                                #         print("trig2")
                                # if self.action[7] == '09':
                                #     self.joy['trig3'] = True
                                #     if self.verbose:
                                #         print("trig3")
                                if self.action[7] == '0D':
                                    self.joy['buttonup'] = True
                                    if self.verbose:
                                        print("buttonup")
                                if self.action[7] == '10':
                                    self.joy['buttonright'] = True
                                    if self.verbose:
                                        print("buttonright")
                                if self.action[7] == '0E':
                                    self.joy['buttondown'] = True
                                    if self.verbose:
                                        print("buttondown")
                                if self.action[7] == '0F':
                                    self.joy['buttonleft'] = True
                                    if self.verbose:
                                        print("buttonleft")
                                if self.action[7] == '02':
                                    self.joy['triangle'] = True
                                    if self.verbose:
                                        print("triangle")
                                if self.action[7] == '01':
                                    self.joy['circle'] = True
                                    if self.verbose:
                                        print("circle")
                                if self.action[7] == '00':
                                    self.joy['cross'] = True
                                    if self.verbose:
                                        print("cross")
                                if self.action[7] == '03':
                                    self.joy['square'] = True
                                    if self.verbose:
                                        print("square")
                                if self.action[7] == '08':
                                    self.joy['select'] = True
                                    if self.verbose:
                                        print("select")
                                if self.action[7] == '09':
                                    self.joy['start'] = True
                                    if self.verbose:
                                        print("start")
                                if self.action[7] == '0A':
                                    self.joy['ps'] = True
                                    if self.verbose:
                                        print("ps")
                                # state = self.action[7]

                            else:
                                if self.action[7] == '04':
                                    self.joy['trig0'] = False
                                if self.action[7] == '05':
                                    self.joy['trig1'] = False
                                # if self.action[7] == '06':
                                #     self.joy['trig2'] = False
                                # if self.action[7] == '07':
                                #     self.joy['trig3'] = False
                                if self.action[7] == '0D':
                                    self.joy['buttonup'] = False
                                if self.action[7] == '10':
                                    self.joy['buttonright'] = False
                                if self.action[7] == '0E':
                                    self.joy['buttondown'] = False
                                if self.action[7] == '0F':
                                    self.joy['buttonleft'] = False
                                if self.action[7] == '02':
                                    self.joy['triangle'] = False
                                if self.action[7] == '01':
                                    self.joy['circle'] = False
                                if self.action[7] == '04':
                                    self.joy['cross'] = False
                                if self.action[7] == '00':
                                    self.joy['square'] = False
                                if self.action[7] == '08':
                                    self.joy['select'] = False
                                if self.action[7] == '09':
                                    self.joy['start'] = False
                                if self.action[7] == '0A':
                                    self.joy['ps'] = False

                        elif self.action[7] == '00':
                            num = int(self.action[5], 16)
                            if num >= 128:
                                self.joy['leftx'] = -int(percent254)
                            elif num <= 127 \
                            and num != 0:
                                self.joy['leftx'] = int(percent128)
                            else:
                                self.joy['leftx'] = 0

                        elif self.action[7] == '01':
                            num = int(self.action[5], 16)
                            if num >= 128:
                                self.joy['lefty'] = int(percent254)
                            elif num <= 127 \
                            and num != 0:
                                self.joy['lefty'] = -int(percent128)
                            else:
                                self.joy['lefty'] = 0

                        elif self.action[7] == '02':
                            if self.action[4] == '01':
                                self.joy['trig2'] = False
                            else:
                                self.joy['trig2'] = True
                                if self.verbose:
                                    print("trig2")

                        elif self.action[7] == '03':
                            num = int(self.action[5], 16)
                            if num >= 128:
                                self.joy['rightx'] = -int(percent254)
                            elif num <= 127 \
                            and num != 0:
                                self.joy['rightx'] = int(percent128)
                            else:
                                self.joy['rightx'] = 0

                        elif self.action[7] == '04':
                            num = int(self.action[5], 16)
                            if num >= 128:
                                self.joy['righty'] = int(percent254)
                            elif num <= 127 \
                            and num != 0:
                                self.joy['righty'] = -int(percent128)
                            else:
                                self.joy['righty'] = 0

                        elif self.action[7] == '05':
                            if self.action[4] == '01':
                                self.joy['trig3'] = False
                            else:
                                self.joy['trig3'] = True
                                if self.verbose:
                                    print("trig3")

                        self.action = []
        except IOError:
            self.printMessage(2)
            self.setStatus(2)
            self.pairing(self.path)

    def setStatus(self, value):
        if value == 1:
            self.status = "Controller connected."
        else:
            self.status = "Controller Disconnected."

    def printMessage(self, value):
        if value == 1:
            print("INFO: Controller connected.")
        elif value == 2:
            print("INFO: Controller disconnected.")
        elif value == 3:
            print("INFO: Connecting to the controller.")

    def getPath(self):
        return self.path

    def getInput(self):
        return self.joy

    def stop(self):
        global reading

        reading = False

        self.setStatus(2)
        self.printMessage(2)

    def __repr__(self):
        return str(self.status)