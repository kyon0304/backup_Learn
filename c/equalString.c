#include <stdio.h>

int main()
{
	char* c = "ss";
	int test = ("ss" == "ss");
	int test2 = (c == "ss");
	printf("%d, %d\n", test, test2);
	return 0;
}
