#! /usr/bin/python

import os
import sys
import socket
import requests

host = "aa.bb.cc.dd"
port = 1234

remote_ip = requests.get('https://ip.beget.ru/').text[:-1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((remote_ip, port))
print(s.recv(1024))
