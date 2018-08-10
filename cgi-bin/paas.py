#!/usr/bin/python36
print("Content-Type:text/html ")
print("\n")

import subprocess as sp
import cgi 

print("INITIUM | SOFTWARE DUMP")
print("<br><br>")
cg=cgi.FieldStorage()
uip=cg.getvalue('uip')

c1=sp.getstatusoutput("sudo systemctl restart docker")
print(c1)

c2=sp.getstatusoutput("sudo docker run -dit -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /usr/:/usr/  -e  DISPLAY={}:0.0  --privileged paas:v1  jupyter notebook --allow-root --ip=0.0.0.0".format(uip))
print(c2)

