#!/usr/bin/python

import subprocess
import os
import time

cmd1 = 'echo 1 | nmapper.sh'
cmd2 = 'echo 2 | nmapper.sh'

current = os.getcwd()

# Run Discovery scan
ps = subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print(output)

# This assumes you made called output directory nmap
os.chdir(current + '/nmap')

#print(os.getcwd())
time.sleep(5)

subprocess.call(["ultimate-nmap-parser.sh","*.gnmap","--up"])
time.sleep(3)

# Run Full scan on hosts_up.txt
ps = subprocess.Popen(cmd2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
ps.wait()
output = ps.communicate()[0]
print(output)
time.sleep(190)

# This assumes you made called output directory full
os.chdir(current + '/nmap/full')

subprocess.call(["ultimate-nmap-parser.sh","*.gnmap","--all"])
