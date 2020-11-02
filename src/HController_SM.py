'''
File: HController_SM.py
Created Date: Monday, November 1st 2020, 10:54:34 pm
Author: Zentetsu

----

Last Modified: Mon Nov 02 2020
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
'''

import IRONbark
from Controller.ControllerPS3 import ControllerPS3

global init_ended, cPS3, keyboard

init_ended = False
cPS3 = None
keyboard = None

def a_Main():
	#TODO
	pass

def a_SendControl():
	#TODO
	pass

def a_initController():
	global init_ended, cPS3

	HController_Modules = IRONbark.Module(file="./data/HController_Modules.json")

	cPS3 = ControllerPS3("/dev/input/js0")

	if cPS3 == -1:
		HController_Modules.delSender("PS3")
	else:
		HController_Modules.delListener("Keyboard")

	init_ended = True

def t_init():
	return True

def t_exit():
	#TODO
	pass

def t_startController():
	global init_ended

	return init_ended

def t_beginSC():
	#TODO
	pass

def t_endSC():
	#TODO
	pass

#----------------------------------------------------------------------#