#!/usr/bin/python
#-*- coding: utf-8 -*-
#
#
#



import multiprocessing as mp
import subprocess
import os
import sys
import platform
import ctypes

processes_count = 2

osName = platform.system()


def download_video(url):
  cmd ="python3 $HOME/tools/import_ydl_path.py -f best -v --no-check-certificate --write-sub --write-auto-sub  --sub-lang en,zh-Hant  --sub-format srt --convert-subs srt --download-archive yarch.txt -i %s" % url
  print("running cmd: %s" % cmd)
  os.system(cmd)
  pass



def tryInt(s, defaultValue=0):
  try:
    result = int(s)
  except:
    return (False, defaultValue)
  return (True, result)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("[usage] vdls FILELIST [PROCESSES_COUNT]")
    sys.exit(-1)

  print ("[DEBUG] processing %s" % sys.argv[1])

  f = open(sys.argv[1], "r")

  if osName == "Windows":
    ctypes.windll.kernel32.SetConsoleTitleW(u"vdls downloading...")

  # skip all comment lines
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

