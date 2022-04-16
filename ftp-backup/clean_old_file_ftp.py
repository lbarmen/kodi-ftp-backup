#! /usr/bin/python
import sys
sys.path.append('/storage/.kodi/addons/script.module.ftputil/lib')
import time
import ftputil

host = ftputil.FTPHost('192.168.1.1', 'login', 'pass')
path = '/backup/rpi4/'
now = time.time()
host.chdir(path)
names = host.listdir(host.curdir)
for name in names:
    if host.path.getmtime(name) < (now - (14 * 86400)):
      if host.path.isfile(name):
         host.remove(name)

host.close()