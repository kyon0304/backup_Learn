#! /bin/bash
# filename: recursive.sh
# It's in endless loop in line 9

function F()
{
	echo -n $1;
	sleep 1;
	tput rc
	tput ed
	F world;
}
tput sc
F hello
