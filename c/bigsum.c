// date: 2012-10-17
// author: kyon
// usage: add two big numbers 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* add(char* arr, char* brr)
{
	int lena = strlen(arr);
	int lenb = strlen(brr);
//	printf("%d\t%d\n",lena,lenb);
	int maxsize = (lena > lenb) ? lena : lenb;
	char* sum = (char*)malloc(maxsize+1);
	memset(sum, '0', maxsize+1);
	int i = 0;
	while(lena-- >0 && lenb-- >0)
	{
//		printf("%d\t%d\t%d\n", lena,lenb,maxsize);
		int c = arr[lena] + brr[lenb] + i - '0'*2;
		int r = c%10;
		sum[maxsize--] = r+'0';
		i = c/10;
	}
	while(lena > -1)
	{
//		printf("arr\n");
		int c = arr[lena--] + i - '0';
		int r = c%10;
		sum[maxsize--] = r+'0';
		i = c/10;
	}
	while(--lenb > -1)
	{
//		printf("brr\t%c\n", brr[lenb]);
		int c = brr[lenb] + i - '0';
		int r = c%10;
		sum[maxsize--] = r+'0';
		i = c/10;
	}
	sum[0] = i+'0';
	return sum;
}

int main(int argc, char** argv)
{
	char* a = "12345678";
	char* b = "87654321";
	char* sum = add(a,b);
	size_t pos = strspn(sum,"0");
	printf("%25s\n+%24s\n=%24s\n",a,b,sum+pos);
}
