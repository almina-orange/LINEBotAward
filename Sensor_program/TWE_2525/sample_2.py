# coding: UTF-8
#! /usr/bin/env
import subprocess
import serial
from datetime import datetime

def formatData(data):
	dict = {}

	dict["time"] = int(data[0])
	dict["MACID"] = data[4]
	dict["X"] = int(data[11])
	dict["Y"] = int(data[12])
	dict["Z"] = int(data[13])

	return dict

def modeSet(mode, d, cnt, log, power):
	x = d[0] + power
	y = d[1] + power
	z = d[2] + power

	if mode == 1:
		if z > 20:
			print "Door act!...",
			print 'count: ', cnt, 'dx: ', d[0], 'dy: ', d[1], 'dz: ', d[2]
			return cnt
			#subprocess.call(cmdList3, shell=True)
	elif mode == 2:
		if x > 450 or y > 450 or z > 450:
			print "Fall act!...",
			print 'count: ', cnt, 'dx: ', d[0], 'dy: ', d[1], 'dz: ', d[2]
			return cnt
			#subprocess.call(cmdList3, shell=True)
	elif mode == 3:
		if z > 200:
			print "Tap act!"
			#subprocess.call(cmdList3, shell=True)

	return log

# sensor mode
mode1 = 1
mode2 = 1
mode3 = 1

# set sensor mode
print "sensor1:", "(", str(mode1), ") /", "sensor2: ", "(", str(mode2), ") /", "sensor3: ", "(", str(mode3), ")"
while  1:
	print "change sensor mode? (y:1 / n:0):",
	flg = input()
	if flg == 0:
		break

	if flg == 1:
		print "******************"
		print "*mode1: [Door]"
		print "*mode2: [Tap]"
		print "*mode3: [Fall]"
		print "******************"

		print "No, Mode?:",
		c = input()
		if c[0] == 1:
			mode1 = c[1]
		elif c[0] == 2:
			mode2 = c[1]
		elif c[0] == 3:
			mode3 = c[1]

		print "sensor1:", "(", str(mode1), ") /", "sensor2: ", "(", str(mode2), ") /", "sensor3: ", "(", str(mode3), ")"

print "Delay?:",
delay = input()

print "Power?:",
power = input()

# COM3を開く
s = serial.Serial('COM5', 115200)
print 'Connection success!'

# PushMessage用のphpファイルを外部実行するコマンド
#cmdLine1 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_3.php"
cmdLine1 = "curl -s -v -k --tlsv1.2 https://developer-for-mimi.herokuapp.com/callback_3.php"
cmdList1 = cmdLine1.split()

#cmdLine2 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_4.php"
cmdLine2 = "curl -s -v -k --tlsv1.2 https://developer-for-mimi.herokuapp.com/callback_4.php"
cmdList2 = cmdLine2.split()

#cmdLine3 = "curl -s -v -k --tlsv1.2 https://hiroya-satake-161203.herokuapp.com/callback_5.php"
cmdLine3 = "curl -s -v -k --tlsv1.2 https://developer-for-mimi.herokuapp.com/callback_5.php"
cmdList3 = cmdLine3.split()

# センサIDリスト
sensorId = ["10f0409", "10f0690", "10f06a0"]

fx = open('test3_x.dat', 'w')
fy = open('test3_y.dat', 'w')
fz = open('test3_z.dat', 'w')
fdx = open('test3_dx.dat', 'w')
fdy = open('test3_dy.dat', 'w')
fdz = open('test3_dz.dat', 'w')
cnt = 0
lst_sec = 0
frq = 5

#power = 0		# センサ感度調整用オフセット
d = [power] * 3	# 加速度変化率リスト
#delay = 50		# 感知のディレイ
log = -delay	# 前回感知したタイミング

dict = {}	# センサ情報
dict2 = {}	# 1つ前のセンサ情報(退避用)

# 無限ループ
while 1:
	data = s.readline()

	# 先頭の";"を取り除く
	data = data[1:]
	splitDataUm = data.split(";")

	# 感知中のみ動作する
	if len(splitDataUm) > 2:
		lst_sec = 0

		# key,value型にしてディクショナリに保存
		dict = formatData(splitDataUm)

		# 初回のみ
		if len(dict2) == 0:
			dict2 = formatData(splitDataUm)

		# 加速度の変化率を取得
		d[0] = abs(dict["X"] - dict2["X"])
		d[1] = abs(dict["Y"] - dict2["Y"])
		d[2] = abs(dict["Z"] - dict2["Z"])

		# 1つ前のデータを退避
		dict2 = formatData(splitDataUm)

		# 各センサのIDで処理を分ける
		if dict["MACID"] == sensorId[0]:
			print "*************************************"
			print '<< call 1 >>'
		elif dict["MACID"] == sensorId[1]:
			print "*************************************"
			print '<< call 2 >>'
		elif dict["MACID"] == sensorId[2]:
			#print "*************************************"
			#print dict

			# delay[sec]後から再び判定開始
			if (cnt - log) > delay:
				log = modeSet(mode3, d, cnt, log, power)

			# ファイルに加速度を記録
			fx.write(str(cnt) + "\t" + str(dict["X"]) + "\n")
			fy.write(str(cnt) + "\t" + str(dict["Y"]) + "\n")
			fz.write(str(cnt) + "\t" + str(dict["Z"]) + "\n")
			fdx.write(str(cnt) + "\t" + str(d[0]) + "\n")
			fdy.write(str(cnt) + "\t" + str(d[1]) + "\n")
			fdz.write(str(cnt) + "\t" + str(d[2]) + "\n")
			cnt = cnt + 1

		# (0.1 * 200)[sec]で強制終了
		if cnt > 200:
			break
	else:
		lst_sec = lst_sec + 1
		if lst_sec == 5 * frq:
			print "sensor lost call!"

s.close()
fx.close()
fy.close()
fz.close()
fdx.close()
fdy.close()
fdz.close()