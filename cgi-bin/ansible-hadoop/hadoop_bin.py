#!/usr/bin/python36

from subprocess import getoutput

package=getoutput("ansible-playbook package.yml")
print(package)

cloud=getoutput("ansible-playbook cloud.yml")
print(cloud)

namenode=getoutput("ansible-playbook namenode.yml")
print(namenode)

datanode=getoutput("ansible-playbook datanode.yml")
print(datanode)

bnamenode=getoutput("ansible-playbook bnamenode.yml")
print(bnamenode)
