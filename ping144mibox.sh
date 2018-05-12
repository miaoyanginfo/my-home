#! /bin/bash

ping -w 3 192.168.1.144 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "on"
else
    echo "off"
fi