#!/bin/sh

cat hightemp.txt | awk '{print $1}' > col1.txt
cat hightemp.txt | awk '{print $2}' > col2.txt
