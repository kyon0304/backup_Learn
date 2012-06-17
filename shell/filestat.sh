#! /bin/bash
# filename: filestat.sh date: 2012-2-16
# Usage: generates files statistical information

if [ $# -ne 1 ];
then
	echo $0 $1;
	echo $2 "won't be processed"
	echo
fi
path=$1

declare -A statArray;

while read line
do
	ftype=`file -b "$line"|cut -d, -f1`
	let statArray["$ftype"]++;
	#echo $ftype
done< <(find $path -maxdepth 1 -type f -print)

echo ===============File types and counts===============
for ftype in "${!statArray[@]}";
do
	echo $ftype : ${statArray["$ftype"]}
done
