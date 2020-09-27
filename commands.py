#!/usr/bin/python3
import cgi
print("content-type:text/html")
print()
mydata=cgi.FieldStorage()
myx=mydata.getvalue("x")
import subprocess
output=subprocess.getoutput(myx)
print(output)