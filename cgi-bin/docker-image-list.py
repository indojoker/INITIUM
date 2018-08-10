#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html \n")

dockerImageList=sp.getoutput("sudo docker images")
dockerimage=dockerImageList.split("\n")

print("""
<form action='caas-launch.py'>
<table align='center' width='80%' border=1>
<tr>
<td>enter container name: </td>
<input type='text' name='cname' /></td>
</tr>

<tr>
<td>Enter image name: </td>
</tr>
<select name='imgname'>
""")











