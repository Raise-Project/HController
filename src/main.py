'''
File: main.py
Created Date: Wednesday, October 3rd 2020, 11:06:09 pm
Author: Zentetsu

----

Last Modified: Sat Nov 07 2020
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
2020-11-07	Zen	Refactoring KB name
2020-11-06	Zen	Test for SM and Module
'''


from Controller.ControllerKB import ControllerKB

from CorState import StateMachine
from SharedMemory import Client
from IRONbark import Module

import threading
import time

if __name__ == "__main__":
    state_machine = StateMachine("HController")
    state_machine.loadJSON("./data/HController_SM.json")

    state_machine.start()

    ###########
    # k = ControllerKB()

    # thread = threading.Thread(target=k.readInput, args=())
    # thread.start()

    # while not k.getInput()['esc']:
    #     print(k.getInput(), len(k.getInput()))
    #     time.sleep(0.1)


    #########################################################

    # cK = ControllerKB()
    # thread = threading.Thread(target=cK.readInput, args=())
    # thread.start()


    # m = Module(file="./data/HController_Modules.json")
    # print(m, m["HController"])

    # while True :
    #     m["HController"]["Keyboard"] = cK.getInput()

    #     print(m["HController"])
    #     time.sleep(0.1)

    #     if m["HController"]["Keyboard"]["esc"]:
    #         break

    # m.stopModule()

    #########################################################

    # cK = ControllerKB()
    # thread = threading.Thread(target=cK.readInput, args=())
    # thread.start()

    # # while True:
    # #     print(cK.getInput())
    # #     time.sleep(0.1)


    # c = Client("test", {"z": False, "q": False, "s": False, "d": False, "p": False, "esc": False})

    # while not cK.getInput()["esc"]:
    #     for k in cK.getInput().keys():
    #         c[k] = cK.getInput()[k]
    #     print(c)
    #     time.sleep(0.1)