#!/bin/bash



./schedule_downtime.py $1 $2 > /dev/null 2>&1
if [[ $? -ne 0 ]]; 
then
  echo "Command failed"
  exit 1
fi
echo "command passed"
exit 0
