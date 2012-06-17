#! /bin/bash
#filename:equal.sh
if [ $UID -e 0 ]; then
	echo "Root user"
else
	echo None root user.
fi
