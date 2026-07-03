#!/bin/bash

sed -i 's/ \[.*//g' res_go.txt
sed -i 's/ (.*//g' res_python.txt

diff -y res_go.txt res_python.txt
