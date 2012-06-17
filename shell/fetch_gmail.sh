#! /bin/bash
# filename: fetch_gmail.sh
# usage: get gmail message

username="wangyjob"
password="wy890304"

show_count=5

echo

curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom"|\
tr -d '\n' | sed 's:</entry>:\n:g'|\
sed 's/.*<title>\(.*\)<\/title.*<author><name>\([^<]*\)<\/name><email>\([^<]*\).*/Author: \2 [\3] \nSubject: \1\n/g' | \
head -n $(( $show_count * 3 ))
