#! /bin/bash
# Filename: IFS.sh

data="name,sex,rollno,location"
oldIFS=$IFS
IFS=,
for item in $data;
do
	echo Item: $item
done
IFS=$oldIFS
