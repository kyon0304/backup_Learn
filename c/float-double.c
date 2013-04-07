#include <stdio.h>
int main()
{
	float a = 12.5;
	printf("%d\n", a);
	printf("%d\n", (int)a);
	printf("%d\n", *(int*)&a);
	printf("%d\t%d\t%d\n", sizeof(float),sizeof(double),sizeof(int));
	return 0;
}
