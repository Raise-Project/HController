'''
File: HController_SM.py
Created Date: Monday, November 1st 2020, 10:54:34 pm
Author: Zentetsu

----

Last Modified: Fri Nov 06 2020
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
2020-11-06	Zen	Adding state to clean before exit
2020-11-04	Zen	First step in implementation of SM HController
'''

import IRONbark
from Controller.ControllerPS3 import ControllerPS3
from Controller.Keyboard import Keyboard
import threading
import time

global init_ended, cPS3, HController_Modules, thread

HController_Modules = None
init_ended = False
cPS3 = None
cK = None
thread = None

def a_initController():
	global init_ended, cPS3, cK, HController_Modules, thread

	HController_Modules = IRONbark.Module(file="./data/HController_Modules.json")

	cPS3 = ControllerPS3("/dev/input/js0")

	if cPS3 != -1:
		del HController_Modules["HController"]["Keyboard"]
	else:
		cK = Keyboard()
		del HController_Modules["HController"]["PS3"]
		HController_Modules
		thread = threading.Thread(target=cK.readInput, args=())

	thread.start()

	init_ended = True

def a_Main():
	global cK

	time.sleep(0.1)

def a_SendControl():
	global cK, HController_Modules

	HController_Modules["HController"]["Keyboard"] =  cK.getInput()

def a_stopController():
	global HController_Modules

	HController_Modules.stopModule()

def t_init():
	return True

def t_exit():
	return True

def t_startController():
	global init_ended

	return init_ended

def t_stopController():
	global cK

	return cK.getInput()['esc']

def t_beginSC():
	global cK

	return not cK.getInput()['esc']

def t_endSC():
	return True

#----------------------------------------------------------------------#def a_stopController():
	#TODO
	pass

