#include <stdio.h>
typedef struct test
{
	int x;
	double y;
}test;
int main()
{
	int i,j;
	for( i =0; i < 10; i++ )
	{
		for( j = 0; j < 5; j++ )
		{
			if( j == 3)
				break;
			printf( "%d\t%d\n", i,j );
		}
	}
	printf("\n");
	return 0;
}
