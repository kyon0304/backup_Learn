#include <stdio.h>

void plus(int i)
{
	i++;
}
int main()
{
	int i = 10;
	printf("%d\n", i);
	plus(i);
	printf("%d\n", i);
	return 0;
}

