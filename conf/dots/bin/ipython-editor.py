#!/bin/env python 
import os
import sys
cmd="C:\\cygwin\\opt\\local\\share\\PortableApps\\Notepad++Portable\\Notepad++Portable.exe "+" ".join(sys.argv[1:])
print(cmd)
os.system(cmd)


