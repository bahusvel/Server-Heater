#!/usr/bin/python
import serial
import os

LOW_LINE = 25
HIGH_LINE = 30
HEATER_IPS = ["192.168.100.6"]
HEATER_ON_COMMAND = "echo on > heaters.txt"
HEATER_OFF_COMMAND = "echo off > heaters.txt"

DEBUG = False
HEATERS_ON = False

def turn_heaters_on():
	print("heaters on")
	for heater_ip in HEATER_IPS:
		os.system("ssh root@{} '{}'".format(heater_ip, HEATER_ON_COMMAND))
	
def turn_heaters_off():
	print("heaters off")
	for heater_ip in HEATER_IPS:
		os.system("ssh root@{} '{}'".format(heater_ip, HEATER_OFF_COMMAND))

with serial.Serial('/dev/cu.usbmodem1421') as ser:
	while True:
		line = ser.readline().decode("ascii").strip()
		if DEBUG:
			print(line)
		temp = float(line)
		if temp < LOW_LINE and not HEATERS_ON:
			HEATERS_ON = True
			turn_heaters_on()
		elif temp > HIGH_LINE and HEATERS_ON:
			HEATERS_ON = False
			turn_heaters_off()