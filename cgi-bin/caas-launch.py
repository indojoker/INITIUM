#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type:text/html")
print("")
print("hi")
form = cgi.FieldStorage()
cname= form.getvalue('cname')
imgname= form.getvalue('imgname')
sp.getoutput("systemctl restart docker")
docker_launch_output=sp.getstatusoutput("sudo docker run -dit --name {c} {i}".format(c=cname,i=imgname))
if docker_launch_output[0]==0:
	print("container launched")
	print("<a href='docker-manage.py'> Click to Manage</a>")
else:
	print("container launch failed")



