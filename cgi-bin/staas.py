#!/usr/bin/python36
print("Content-Type: text/html ")
print("\n")

import subprocess as sp
import cgi 

#print("hello")

sip="192.168.43.162"
cmd=cgi.FieldStorage()
uname=cmd.getvalue('uname')
cip=cmd.getvalue('ip')
passwd=cmd.getvalue("passwd")
acname=cmd.getvalue("acname")
size=cmd.getvalue("size")
#uname="ss11"
#cip="192.168.43.73"
#passwd="redhat"
#acname="root"
#size=1

#print(cip,"<br>")
#print(passwd,"<br>")
#print(size,"<br>")
#print(uname,"<br>")


#subprocess.getoutput("echo '{}	ansinble_ssh_user={}	ansible_ssh_pass={}'>>/etc/ansible/hosts".format(cip, acname, passwd))
'''
yum install nsf-utils----------package
mkdir /mydata------------------files
chmod o+w /mydata-----------------"
echo "/cloud *(rw,no_root_squash)">>/etc/exports---------copy
systemctl restart nfs----------------------------------service
------------------------------------------------
yum install nfs-utils
mkdir /media/mystore
mount cloupip:/mydata  /media/mystore
echo "cloudip:/mydata  /media/mystore  nfs  _netdev,defaults  0 0"
'''


'''
lvcreate --name mylv --size xG  vg
mkfs.ext4 /dev/vg/mylv
mkdir /username
mount /dev/vg/mylv  /username
echo "/dev/vg/mylv  /username  ext4  defaults  0 0" >> /etc/fstab
chmod o+w /mydata-----------------"
echo "/cloud *(rw,no_root_squash)">>/etc/exports---------copy
systemctl restart nfs----------------------------------service
'''

h="""{}	ansible_ssh_user={}	ansible_ssh_pass={}
192.168.43.162	ansible_ssh_user=root	ansible_ssh_pass=redhat
""".format(cip,acname,passwd)
c1=sp.getoutput("chmod +x /etc/ansible/hosts")
c2=sp.getoutput("chown apache /etc/ansible/hosts")
f=open('/etc/ansible/hosts','w')
f.write(h)
f.close()


ans="""
- hosts: {2}
  tasks:
  - name: create lv
    lvol:
        vg: /dev/mycloud
        lv: {0}
        size: {1}

  - name: Create a ext4 filesystem on lv
    command: "mkfs.ext4 /dev/mycloud/{0}"

  - name: create cloud folder
    file:
        path: /{0}
        state: directory
        mode: 0777

  - name: fix folder size by mounting
    command: mount /dev/mycloud/{0}  /{0}

  - lineinfile:
        line: "/{0}  {3}(rw,no_root_squash)"
        path: /etc/exports
  - lineinfile:
        line: "/dev/mycloud/{0}  /{0}  ext4  defaults  0 0"
        path: /etc/fstab

  - name: install nfs
    package:
        name: nfs-utils
        state: present

  - name: start nfs service
    service:
        name: nfs
        state: restarted
        enabled: true

- hosts: {3}
  tasks:
  - name: install nfs
    package:
        name: nfs-utils
        state: present

  - name: create drive folder
    file:
        path: /media/{0}
        state: directory
        mode: 0777

  - name: mount drive
    command: "mount {2}:/{0}  /media/{0}"

  - name: fstab entry
    lineinfile:
        line: "{2}:/{0}  /media/{0}  nfs  _netdev,defaults  0 0"
        path: /etc/fstab

""".format(uname, size, sip, cip)

sp.getoutput("touch staas.yml")

sp.getstatusoutput("chmod +x staas.yml")
sp.getstatusoutput("chown apache staas.yml")

f=open('./staas.yml','w')
f.write(ans)
f.close()
sp.getstatusoutput("chmod +x staas.yml")
sp.getstatusoutput("chown apache staas.yml")
final=sp.getstatusoutput("sudo ansible-playbook staas.yml")
#print(final)
if final[0]==0:
	print("location: ../menu.html")
	print("")
else:
	print("<a href='menu.html'>TRY AGAIN</a>")
