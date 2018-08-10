#!/usr/bin/python36
print("Content-Type:text/html ")
print("\n")

import subprocess as sp
import cgi 

print("hello")
print("<br><br>")
sp.getoutput("systemctl restart docker")
sip="192.168.100.242"
cmd=cgi.FieldStorage()
opt=cmd.getvalue('sel')
uname=cmd.getvalue('uname')
uip=cmd.getvalue('uip')
passwd="thanos"
print(opt)
print("<br><br>")


rd=sp.getstatusoutput("sudo systemctl restart docker")
print("docker restart: ",rd)
print("<br><br>")

ed=sp.getstatusoutput("export DISPLAY=:0")
print("export display: ",ed)
print("<br><br>")

uadd=sp.getstatusoutput("sudo useradd -m -p {}  {}".format(passwd,uname))
print("useradd:  ",uadd)
print("<br><br>")
sudoer=sp.getstatusoutput("sudo sed -i '1 a {} ALL=(ALL) NOPASSWD: ALL' /etc/sudoers".format(uname))
print("sudoer:  ",sudoer)
print("<br><br>")
cmd="""#!/usr/bin/python36

print("THANOS|SAAS")

import subprocess as sp

sp.getoutput("sudo systemctl restart docker")

x=sp.getstatusoutput("sudo docker run -dit -e DISPLAY={}:0.0  -v  /tmp/.X11-unix:/tmp/.X11-unix  -v /usr/:/usr/   firefox:v1  firefox")

print(x)
""".format(uip)

#bp=sp.getstatusoutput("cat {} >> /bin/{}.py".format(cmd,uname))
sp.getoutput("sudo cp /bin/demosaas.py  /bin/{}.py".format(uname))
sudoer=sp.getstatusoutput("sudo sed -i 's/xxx/{0}/' /bin/{0}.py".format(uip,uname))
#x="/bin/{}.py".format(uname)
#fh=open(x,'w')
#fh.write(cmd)
#fh.close()
#rint("bin py:  ",bp)
#rint("<br><br>")

ch=sp.getstatusoutput("sudo chmod +rwx /bin/{}.py".format(uname))
print("chmod:   ",ch)
print("<br><br>")

sed=sp.getstatusoutput("sudo sed -i 's/{0}:\/bin\/bash/{0}:\/bin\/{0}.py/' /etc/passwd".format(uname))
print("sed:  ",sed)
print("<br><br>")

print("Login IP: {} <br>Login Account Name: {} <br>Login Password: {}".format(sip,uname,passwd))
print("<br><br>")


