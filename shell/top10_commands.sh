#! /bin/bash
# top10_commands.sh:list top 10 commands that be used

printf "COMMAND\tCOUNT\n"

cat ~/.bash_history|awk '{ list[$1]++; } \
END{
	for(i in list)
		{
			printf("%s\t%d\n",i,list[i]); 
		}
}'|sort -nrk 2|head
