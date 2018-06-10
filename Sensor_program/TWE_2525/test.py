# coding: UTF-8
#! /usr/bin/env
import subprocess
import serial
from datetime import datetime

fr = open('test_dz.dat', 'r')
fw = open('sample_dz.dat', 'w')

# 無限ループ
for li in fr.readlines():
	data = li.split()

	fw.write(str(data[0]) + "\t" + str(abs(int(data[1]))) + "\n")

fr.close()
fw.close()