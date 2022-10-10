#!/bin/bash
#Author: Iulian Bancau

IP=$(ip a show tun0 | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}')

if expr "$IP" : '[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$' >/dev/null; then
  echo "VPN: $IP"
else
  IP=$(dig +short myip.opendns.com @resolver1.opendns.com)
  echo "[VPN OFF] - INET: $IP"
fi
