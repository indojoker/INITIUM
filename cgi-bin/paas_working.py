#!/usr/bin/python36
print("Content-Type:text/html ")
print("\n")

import subprocess as sp
import cgi 

print("INITIUM | SOFTWARE DUMP")
print("<br><br>")
cg=cgi.FieldStorage()
uip=cg.getvalue('uip')
uname=cg.getvalue('uname')
passwd="thanos"
print("<br><br>")
print(uip)
print("<br>")
print(uname)
print("<br>")
#uname="r1"
#passwd="r1"
#uip="192.168.43.162"

c1=sp.getstatusoutput("touch /bin/{}.sh".format(uname))
print(c1)
shellfile="""#!/bin/bash
sudo systemctl restart docker

sudo docker run -it -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /usr/:/usr/  -e  DISPLAY={}:0.0  --privileged paas:v1  jupyter notebook --allow-root --ip=0.0.0.0
""".format(uip)

file2 = "/bin/{}.sh".format(uname)
sp.getoutput("chmod +rwx {}".format(file2))
sp.getoutput("chown apache {}".format(file2))
f1=open(file2,'w')
f1.write(shellfile)
f1.close()

c2=sp.getstatusoutput("sudo chmod +x {}".format(file2))
print("c2")
print(c2)

c3=sp.getstatusoutput("sudo useradd -s {}  {}".format(file2,uname))
print(c3)

c4=sp.getstatusoutput('echo "{}" | sudo passwd "{}" --stdin'.format(passwd,uname))
print("c4")
print(c4)

rootpower="{}  ALL=(ALL)  NOPASSWD: ALL".format(uname)
f2=open('/etc/sudoers','a')
f2.write(rootpower)
f2.close()

c5=sp.getstatusoutput("sudo systemctl restart docker")
print(c5)

print("LOGIN WITH MOBAxTERM ON <br>IP: 192.168.43.20<br>UNAME: {} <br>PASSWD: thanos".format(uname))


