import os
import sys
import re
import subprocess

java_home=r'%JAVA_HOME%\bin'

r1=subprocess.check_output(['C:/Program Files/Java/jdk1.8.0_192/bin/java.exe','-version'], stderr=subprocess.STDOUT)
print r1
pattern = '\"(\d+\.\d+).*\"'
r2= re.search(pattern, r1).groups()[0]
print r2
r3='C:\Program Files\Java\jdk1.8.0_192'
print r3.replace('\\','/')
r4='1.8'
r5=float(r4)
print(type(r5))