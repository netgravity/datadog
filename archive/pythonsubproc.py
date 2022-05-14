#!/usr/bin/env python3


def get_value():
  import subprocess

 # p1 = subprocess.run('cat sendata.py | grep datadog', capture_output=True, text=True, shell=True)
  p1 = subprocess.run('docker info | grep "Total Memory"  | cut -d " " -f4 | sed "s/GiB//g"', capture_output=True, text=True, shell=True)

  return (p1.stdout)

print (get_value())

d1 = float(get_value())
print (type(d1))
d2 = 15
if ( d1 < d2 ):
       print ("docker info value is less than what it should be")
