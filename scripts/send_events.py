#!/usr/bin/env python3

from datadog import initialize, api
import os

environment_vars = os.environ


# source the .env file to load the keys
options = {
           "api_key": environment_vars.get("api_key"),
           "app_key": environment_vars.get("app_key"),
           }

initialize(**options)

def send_to_datadog():
    print("inside send to datadog func")
    title = "docker info stuff"
    text = "docker storage needs to be checked , please check docker info command"
    tags = ["application:docker", "issue:dockerinfo"]
    
    api.Event.create(title=title, text=text, tags=tags)

def get_value():
  import subprocess

 # p1 = subprocess.run('cat sendata.py | grep datadog', capture_output=True, text=True, shell=True)
  p1 = subprocess.run('docker info | grep "Total Memory"  | cut -d " " -f4 | sed "s/GiB//g"', capture_output=True, text=True, shell=True)

  return (p1.stdout)

print (get_value())

d1 = float(get_value())
#print (type(d1))
d2 = 10
if ( d1 < d2 ):
       send_to_datadog()
       print ("docker info value is less than what it should be")
