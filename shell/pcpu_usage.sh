#! /bin/bash
# pcpu_usage.sh: compute the top process that use CPU in last 1 hour.

SECS=60
UNIT_TIME=60

STEP=$(( $SECS / $UNIT_TIME ))

echo Watching CPU usage... ;

for((i=0;i<STEP;i++))
do
	ps -eo comm,pcpu|tail -n +2 >> ./cpu_usage.$$
	sleep $UNIT_TIME
done

echo
echo CPU eaters :

cat ./cpu_usage.$$|\
awk '
{ process[$1]+=$2; }
END{
	for(i in process)
	{
		printf("%-20s %s\n",i, process[i]);
	}
}'|sort -rnk 2 |head

rm ./cpu_usage.$$
