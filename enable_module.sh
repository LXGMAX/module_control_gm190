#!/bin/bash

gpio mode 7 output

echo "power off"
gpio write 7 1
gpio write 7 0
sleep 3.1
gpio write 7 1

echo "wait 4 second"
sleep 4

echo "power on"

gpio write 7 1
gpio write 7 0
sleep 0.3
gpio write 7 1

echo "waiting"

#stty -F /dev/ttyS1 ispeed 115200 ospeed 115200 cs8
#echo -e "at+zipcall=1\r\n" > /dev/ttyS1
python3 /root/check_call.py
echo "cat1 module enabled"
