#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess as sp

status=sp.getstatusoutput("sudo ansible-playbook ansible-hadoop/bnamenode.yml")
#status= sp.getstatusoutput("sudo date")
if status[0] ==0:
	print("""
	<body bgcolor="black" text="white">
	<h1 align='center'>Hadoop Cluster setup</h1>
	<form>
	<table align='center' border='1' width='40%'>
	<th>Service</th>
	<th>link</th>
	<th>Status</th>
	<tr>
	<td>Click to install Hadoop</td>
	<td><a href='hadoop_setup2.py'>Click</td></td>
	<td><b>Installed</b></td>
	</tr>
	<tr>
	<td>Setup node storage over cloud</td>
	<td><a href='hadoop-cloud.py'>Click</a></td>
	<td><b>Setup done</b></td>
	</tr>
	<tr>
	<td>Click to Setup Namenode</td>
	<td><a href='hadoop-namenode.py'>Click</a></td>
	<td><b>Namenode active</b></td>
	</tr>
	<tr>
	<td>Click to setup datanodes</td>
	<td><a href='hadoop-datanode.py'>Click</a></td>
	<td><b>Datanode active</b></td>
	</tr>
	<tr>
	<td>Click to setup backup namenode</td>
	<td><a href='hadoop-backupnode.py'>Click</a></td>	
	<td><b>Backup node active</b></td>
	</tr>
	<tr>
	<td>Click submit for the cluster</td>
	<td colspan=2 align='center'><a href='http://192.168.43.167:50070'>submit</a></td>
	</tr>
	</table>
	</form>
	</body>
	""")
else:
	print("<h2 align='center'>Error</h2>")

