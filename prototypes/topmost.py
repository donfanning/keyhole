# Author: Nicolas VERDIER
# This file is part of memorpy.
#
# memorpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# memorpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with memorpy.  If not, see <http://www.gnu.org/licenses/>.

import win32gui
import win32con
import win32console
import time

def start_winforeground_daemon():
	import threading
	t=threading.Thread(target=window_foreground_loop)
	t.daemon=True
	t.start()
	
def window_foreground_loop(timeout=0.001):
	""" set the windows python console to the foreground (for example when you are working with a fullscreen program) """
	hwnd=int(win32console.GetConsoleWindow())
	while True:
		win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

start_winforeground_daemon()
while 1:
    time.sleep(0)