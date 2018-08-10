#!/usr/bin/python36

print("content-type: text/html")
print("")
import subprocess as sp
status=sp.getstatusoutput("sudo ansible-playbook ansible-hadoop/package.yml")
#status = sp.getstatusoutput("sudo date")
if status[0] == 0:
	print("""
	<body bgcolor="black" text="white">
	<h1 align='center'>Hadoop Cluster setup</h1>
	<form action=''>
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
	<td>No setup</td>
	</tr>
	</table>
	</form>
	</body>
	""")
else:
	print("<h2 align='center'>Error</h2>")
