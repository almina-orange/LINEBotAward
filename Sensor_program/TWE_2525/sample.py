# coding: UTF-8
#! /usr/bin/env
import subprocess
import serial
from datetime import datetime

# COM3を開く
s = serial.Serial('COM5', 115200)
print 'Connection success!'

# PushMessage用のphpファイルを外部実行するコマンド
cmdLine1 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_3.php"
cmdList1 = cmdLine1.split()

cmdLine2 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_4.php"
cmdList2 = cmdLine2.split()

cmdLine3 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_5.php"
cmdList3 = cmdLine3.split()

# 無限ループ
while 1:
	data = s.readline()

	# 先頭の":"を取り除く
	data = data[2:]
	splitDataUm = data.split(":")

	dict = {}

	# key,value型にしてディクショナリに保存
	for splitData in splitDataUm:
		s_key = splitData.split("=")[0]
		s_val = splitData.split("=")[1]

		dict[s_key] = s_val

	# センサーから検知がないときは"ts"のkeyしか取れないので,
	# ここでは適当なkeyとして"id"で判断
	if ("id" in dict):
		if dict["id"] == "1":
			#subprocess.call(cmdList1, shell=True)
			print '<< call-1 >>'
		elif dict["id"] == "2":
			subprocess.call(cmdList3, shell=True)
			print '<< call-2 >>'
		elif dict["id"] == "3":
			#subprocess.call(cmdList3, shell=True)
			print '<< call-3 >>'

		print dict

s.close()