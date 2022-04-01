#!/usr/bin/env python
# coding: utf-8
'''
Project 9 03/2022
@Witch_Sec
https://github.com/miss-anthrope
-
Class: https://www.udemy.com/course/python-for-pentesters (Credit to Cristi Zot https://www.udemy.com/user/cristivlad2/)
'''
#Spoofing your MAC with Python
print("Have fun, ya skiddie!")
print("WARNING: THIS WILL CHANGE THE MAC UNTIL REBOOT.")
print("Requires elevated privs")

import random
import os
import subprocess

def get_rand():
	return random.choice("abcdef0123456789")

def new_mac():
	new_=""
	for i in range(0,5):
			new_+=get_rand()+get_rand()+":" 

	new_+=get_rand()+get_rand()
	return new_

print("Abracadabra! Your current MAC is:")
print(os.system("\nifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

subprocess.call(["sudo","ifconfig","eth0","down"])

new_m=new_mac()

subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m])
subprocess.call(["sudo","ifconfig","eth0","up"])

print("\nHocus pocus! Your new MAC is now:")
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

print("\nOk, haha. Now change me back.")

