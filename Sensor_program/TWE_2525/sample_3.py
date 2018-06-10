# coding: UTF-8
#! /usr/bin/env
import subprocess
import serial
from datetime import datetime

def formatData(data):
	dict = {}

	dict["time"] = data[0]
	dict["num"] = data[3]
	dict["MACID"] = data[4]
	dict["mode"] = data[6]
	dict["X"] = data[11]
	dict["Y"] = data[12]
	dict["Z"] = data[13]

	return dict


# COM3を開く
s = serial.Serial('COM5', 115200)
print 'Connection success!'

# PushMessage用のphpファイルを外部実行するコマンド
cmdLine1 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_3.php"
#cmdLine1 = "curl -s -v -k --tlsv1.2 https://developer-for-mimi.herokuapp.com/callback_3.php"
cmdList1 = cmdLine1.split()

cmdLine2 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_4.php"
#cmdLine2 = "curl -s -v -k --tlsv1.2 https://developer-for-mimi.herokuapp.com/callback_4.php"
cmdList2 = cmdLine2.split()

cmdLine3 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_5.php"
#cmdLine3 = "curl -s -v -k --tlsv1.2 https://developer-for-mimi.herokuapp.com/callback_5.php"
cmdList3 = cmdLine3.split()

sensorId = ["10f0409", "10f0690", "10f06a0"]

# 無限ループ
while 1:
	data = s.readline()

	# 先頭の";"を取り除く
	data = data[1:]
	splitDataUm = data.split(";")

	if len(splitDataUm) > 2:
		# key,value型にしてディクショナリに保存
		dict = formatData(splitDataUm)

		# センサーから検知がないときは"ts"のkeyしか取れないので,
		# ここでは適当なkeyとして"id"で判断

		#if dict["MACID"] == sensorId[0] and dict["mode"] == "0008":
		if dict["MACID"] == sensorId[0] and dict["mode"] == "0008":
			print "*************************************"
			print dict
			print '<< call 1 >>'
			#subprocess.call(cmdList1, shell=True)
		elif dict["MACID"] == sensorId[1]:
			print "*************************************"
			print dict
			print '<< call 2 >>'
			#subprocess.call(cmdList2, shell=True)
		elif dict["MACID"] == sensorId[2]:
			print "*************************************"
			print dict
			print '<< call 3 >>'
			#subprocess.call(cmdList3, shell=True)

s.close()