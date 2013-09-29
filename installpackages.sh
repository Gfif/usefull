#!/bin/bash
sudo dpkg --get-selections | grep '[[:space:]]install$' | awk '{print $1}'
