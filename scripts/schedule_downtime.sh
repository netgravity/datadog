#!/bin/bash



./schedule_downtime.py $1 $2 > /dev/null 2>&1
if [[ $? -ne 0 ]]; 
then
  echo "Schedule downtime failedi for "$1". Please run and check schedule_downtime.py for errors"
  exit 1
fi
echo "Schedule Downtime for "$1" completed"
exit 0
