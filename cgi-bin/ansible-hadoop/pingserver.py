#!/usr/bin/python36

from subprocess import getoutput
import os

ss = os.system("ping -c 1 {0}".format(ip))

while ss == 0:
	ss = os.system("ping -c 1 -W 2 {0}".format(ip))
	time.sleep(5)

getoutput("cat /root/staticip.txt > /etc/sysconfig/network-script/ifcfg-enp0s3")
getoutput("systemctl restart network")
getoutput("systemctl enable network")

getoutput("iptables -F")
getoutput("hadoop-daemon.sh start namenode")

