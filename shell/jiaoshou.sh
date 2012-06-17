#! /bin/bash
while [ $? -eq 0 ]
do nc -vlp 8888 -C
	`r=read;e=echo;$r a b c;z=$r;
	while [ ${#z} -gt 2 ];do $r z;done;
	f=`$e $b|sed "s/[^a-z0-9_.-]//gi"`;
	h="HTTP/1.1";
	o="$h 200 OK";
	c="Content";
	hd="$c-Type: text/html";
    charset="utf-8";
	if [ -z $f ];then
		($e "$o";$e $hd;$e;ls|(while $r n;do if [ -f "$n" ]; then $e "<a href=\"/$n\">`ls -gh $n`</a><br>";fi;done););
	elif [[ $f =~ eggs ]];then
		($e "$o";$e $hd;$e;curl http://labs.douban.com/doublo/eggs?k=`$e $f|sed "s/eggs//gi"` 2>/dev/null;);
	elif [ -f $f ];then 
		$e "$o";$e "$c-Type: `file -ib $f`";$e "$c-Length: `stat -c%s $f`";$e;cat $f;
	else $e -e "$h 404 Not Found\n\n404\n";fi`;
done
