#! /bin/sh

cat hightemp.txt | awk '{print $3}' | sort 
