#! /usr/bin/python

import os
import sys
import socket

host = "aa.bb.cc.dd"
port = 1234

remote_ip = socket.gethostbyname(host)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((remote_ip, port))
print(s.recv(1024))
