#!/bin/bash

while true
do
    echo "######################"
    echo "Menu ----"
    echo "######################"
    echo "Enter 1 to ugrade dev 1"
    echo "Enter 2 to ugrade uat 1"
    echo "Enter q o exit menu q: "
    echo -e "\n"
    echo -e "Enter your selection \c"
    read answer
    case "$answer" in
      1) scripts/dev_test.sh
	 exit ;;
   
      2) scripts/uat.sh
	 exit ;;

      q) exit ;;
    esac
done
	 
