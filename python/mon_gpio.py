#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# Copyright (C) 2013, Elphel.inc.
# Monitor a range of GPIO bits (should be exported first)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
__author__ = "Andrey Filippov"
__copyright__ = "Copyright 2014, Elphel, Inc."
__license__ = "GPL"
__version__ = "3.0+"
__maintainer__ = "Andrey Filippov"
__email__ = "andrey@elphel.com"
__status__ = "Development"
import sys
if len(sys.argv) < 2 :
    print ("Usage: ", sys.argv[0]+" <gpio_number>[<gpio_max_number>]")
    exit (0)
gpio_low_n=int(sys.argv[1])
if len(sys.argv)>2:
    gpio_high_n=int(sys.argv[2])
else:
    gpio_high_n=gpio_low_n
print ("gpio %d.%d: "%(gpio_high_n,gpio_low_n), end=""),    
# bash> echo 240 > /sys/class/gpio/export
# bash> echo out > /sys/class/gpio/gpio240/direction
# bash> echo 1 > /sys/class/gpio/gpio240/value
       
for gpio_n in range (gpio_high_n, gpio_low_n-1,-1):
    if gpio_n != gpio_high_n and ((gpio_n-gpio_low_n+1) % 4) == 0:
        print (".",end="")
    try:
        with open ("/sys/class/gpio/gpio%d/value"%gpio_n,"r") as f:
            print (f.read(1),end="")
    except:
        print ("X",end="")
print()            
