#!/bin/bash

ip l set dev wlan0 up
ip r flush all
ip a add 83.172.38.66/28 dev eth0
ip r add default via 83.172.38.78
echo "nameserver 83.172.32.17" > /etc/resolv.conf
