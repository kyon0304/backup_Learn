#include <stdio.h>
#include <unistd.h>
int main()
{
	while(1){
		fprintf(stdout,"hello-std-out\n");
		fprintf(stderr,"hello-std-err");
		sleep(1);
	}
	return 0;
}
