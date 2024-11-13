#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import subprocess

def sendmessage(message="drink water"):
	subprocess.Popen(['notify-send', message])
	return

if __name__ == '__main__':
	sendmessage()
