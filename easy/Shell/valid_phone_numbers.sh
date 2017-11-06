#!/bin/bash

while read -r line ; do [[ $line =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]] && echo $line; [[ $line =~ ^\([0-9]{3}\)[[:space:]][0-9]{3}-[0-9]{4}$ ]] && echo $line;done < file.txt
