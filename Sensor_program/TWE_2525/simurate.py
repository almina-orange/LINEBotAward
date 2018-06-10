# coding: UTF-8
#! /usr/bin/env
import subprocess
import serial
from datetime import datetime
import json
import requests

r = requests.get('https://developer-for-mimi.herokuapp.com/sample.json')
data = r.json()
s1 = int(data["sensor"][0]["No.1"])
s2 = int(data["sensor"][0]["No.2"])
s3 = int(data["sensor"][0]["No.3"])

def modeSet(mode, d, cnt, log):
	if mode == 1:
		if d[2] > s3:
			print "Door act!...",
			print 'count: ', xdata[0], 'dx: ', d[0], 'dy: ', d[1], 'dz: ', d[2]
			return cnt
		#subprocess.call(cmdList3, shell=True)
	elif mode == 2:
		if d[0] > 450 or d[1] > 450 or d[2] > 450:
			print "Fall act!...",
			print 'count: ', xdata[0], 'dx: ', d[0], 'dy: ', d[1], 'dz: ', d[2]
			return cnt
		#subprocess.call(cmdList3, shell=True)
	elif mode == 3:
		if d[2] > 200:
			print "Tap act!"
		#subprocess.call(cmdList3, shell=True)

	return log

# sensor mode
mode = 1

fdx = open('sample_dx.dat', 'r')
fdy = open('sample_dy.dat', 'r')
fdz = open('sample_dz.dat', 'r')

power = 0
d = [power] * 3
delay = 100
log = -delay

# 無限ループ
for xli in fdx.readlines():
	yli = fdy.readline()
	zli = fdz.readline()

	xdata = xli.split()
	ydata = yli.split()
	zdata = zli.split()

	# key,value型にしてディクショナリに保存
	d[0] = d[0] + int(xdata[1])
	d[1] = d[1] + int(ydata[1])
	d[2] = d[2] + int(zdata[1])
	cnt = int(xdata[0])

	# センサーから検知がないときは"ts"のkeyしか取れないので,
	# ここでは適当なkeyとして"id"で判断
	#print "*************************************"
	#print 'count: ', xdata[0], 'dx: ', dx, 'dy: ', dy, 'dz: ', dz
	if (cnt - log) > delay:
		print ".",
		log = modeSet(mode, d, cnt, log)

fdx.close()
fdy.close()
fdz.close()