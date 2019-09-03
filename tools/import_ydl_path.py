#-*- coding: utf-8 -*-
#

import sys

__youtube_dl_src__ = "/home/jovyan/ydl"

sys.path.append(__youtube_dl_src__)

try:
  import youtube_dl
except ImportError as err:
  print("Error: import %s: %s" % (__youtube_dl_src__, err))

youtube_dl.main()
