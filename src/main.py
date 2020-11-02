'''
File: main.py
Created Date: Wednesday, October 3rd 2020, 11:06:09 pm
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


from CorState import StateMachine
import curses


if __name__ == "__main__":
    state_machine = StateMachine("HController")
    state_machine.loadJSON("./data/HController_SM.json")

    state_machine.start()