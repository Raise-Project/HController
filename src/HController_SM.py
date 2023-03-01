'''
File: HController_SM.py
Created Date: Monday, November 1st 2020, 10:54:34 pm
Author: Zentetsu

----

Last Modified: Tue Dec 07 2021
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
2020-11-18	Zen	Adding gestion for arm and PS3 Controller
2020-11-07	Zen	Refactoring KB name
2020-11-06	Zen	Adding state to clean before exit
2020-11-04	Zen	First step in implementation of SM HController
'''


import platform

from Controller.ControllerPS3 import ControllerPS3

if "Linux" not in platform.system():
	from Controller.ControllerKB import ControllerKB

import IRONbark

import threading
import time

global init_ended, cPS3, HController_Modules, thread

HController_Modules = None
init_ended = False
cPS3 = None
cKB = None
thread = None

#----------------------------------------------------------------------#
# ------------------------------ States ------------------------------ #
#----------------------------------------------------------------------#
def a_initController():
	global init_ended, cPS3, cKB, HController_Modules, thread
	# print("INIT State")

	HController_Modules = IRONbark.Module(file="./data/HController_Modules.json")

	cPS3 = ControllerPS3("/dev/input/js0")

	if cPS3 != -1:
		del HController_Modules["HController"]["Keyboard"]
		thread = threading.Thread(target=cPS3.pairing, args=())
	else:
		cKB = ControllerKB()
		del HController_Modules["HController"]["PS3"]
		thread = threading.Thread(target=cKB.readInput, args=())

	thread.start()

	init_ended = True

def a_Main():
	global cKB
	# print("MAIN State")

	time.sleep(0.1)

def a_SendControl():
	global cKB, cPS3, HController_Modules
	# print("SENDC State")

	if cPS3 != -1:
		HController_Modules["HController"]["PS3"] = cPS3.getInput()
		# print(HController_Modules["HController"]["PS3"], end="\r", flush=True)
	else:
		HController_Modules["HController"]["Keyboard"] = cKB.getInput()
		# print(HController_Modules["HController"]["Keyboard"], end="\r", flush=True)

	HController_Modules["HController"]["time"] = HController_Modules["HCore"]["time"]

def a_stopController():
	global HController_Modules
	# print("STOPC State")

	HController_Modules.stopModule()

#----------------------------------------------------------------------#
# ---------------------------- Transitions --------------------------- #
#----------------------------------------------------------------------#
def t_init():
	return True

def t_startController():
	global init_ended

	return init_ended

def t_beginSC():
	global cKB, cPS3

	if cPS3 != -1:
		return HController_Modules["HCore"]["Active"]
	else:
		return HController_Modules["HCore"]["Active"]

def t_endSC():
	return True

def t_stopController():
	global cKB, cPS3

	if cPS3 != -1:
		return not HController_Modules["HCore"]["Active"]
	else:
		return not HController_Modules["HCore"]["Active"]

def t_exit():
	return True

#----------------------------------------------------------------------#
# --------------------------- Sub functions -------------------------- #
#----------------------------------------------------------------------#
