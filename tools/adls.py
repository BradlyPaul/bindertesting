#!/usr/bin/python
#-*- coding: utf-8 -*-
# 

import multiprocessing as mp
import subprocess
import os
import sys
import platform
import ctypes

processes_count = 2

def download_video(url):
  cmd ="python3 $HOME/tools/import_ydl_path.py --no-check-certificate --download-archive yarch.txt -i -x --audio-format mp3 --audio-quality 0 %s" % url 
  print("running cmd: %s" % cmd)
  os.system(cmd)

def tryInt(s, defaultValue=0):
  try:
    result = int(s)
  except:
    return (False, defauleValue)
  return (True, result)


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("[usage] downloading audio only:  vdlsmp3 FILELIST [PROCESSES_COUNT=2]")
    sys.exit(-1)

  print ("[DEBUG] processing %s" % sys.argv[1])

  f = open(sys.argv[1], "r")

  lines = []
  for line in f.readlines():
    line = line.rstrip('\n').strip()
    if  line != "" and  not line.startswith("#"):
      lines.append(line)

  if len(sys.argv)>=3:
    ok, processes_count = tryInt(sys.argv[2], 2)

  print("[DEBUG] processes_count = %d" % processes_count)

  pool = mp.Pool(processes=processes_count)
  pool_outputs = pool.map(download_video, lines)
  pool.close()
  pool.join()

