#!/bin/bash
airmon-ng stop wlanmon
sleep 2
ifconfig wlan down
ip link set wlan name $1