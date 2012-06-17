#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct node{
	char* num;
	struct node* left;
	struct node* right;
}node;
int Count = 0;
#include <stdio.h> 

typedef union  
{ 
	long   l; 
    char   str[sizeof(long)]; 
}u; 

int   endian() 
{ 
      u   endian; 
      endian.l   =   1; 

      if(   endian.str[0]   ==   1   ) //little   endian
      { 
      		return 1;         
      } 
      else   if(   endian.str[sizeof(long)-1]   ==   1) //big   endian
      { 
		  return 2;
      } 
      else 
      { 
              //printf( "You   host   unknow   endian,   are   you   made   it   by   yourself?\n "); 
				return 0;
      } 
}

node* Sort( void* src, int len, int width, int(*Compare)(void*, void*,int) )
{
	int count = 0;
	
	node* root = NULL;
	root = (node*)malloc(sizeof(node));
	node* p = NULL;
	while( count < (len) )
	{
		node* tempNode = NULL;
		tempNode = (node*)malloc(sizeof(node));
		tempNode->num = (char*)src+count*width;
		tempNode->right = NULL;
		tempNode->left = NULL;
		
		if(count == 0)
			root = tempNode;
		else
		{
			p = root;
			while(p->left!=NULL || p->right!=NULL){
				if( Compare(p->num,src+count*width,width) )
				{
					if(p->left != NULL)
						p = p->left;
					else
						break;
				}else{
					if(p->right != NULL)
						p = p->right;
					else
						break;
				}
			}
			if( Compare(p->num,src+count*width,width) )
				p->left = tempNode;
			else
				p->right =tempNode;
		}
		tempNode = NULL;
		count++;
	}
	return root;
}

int Compare(void* a, void* b, int width)
{
//	return *( (int*)a ) > *( (int*)b ) ? 1 : 0;
	if(endian() == 1)
	{
		int count = 0;
		while(count < width)//little endian
		{
			if(*((char*)a+count) == *((char*)b+count))
				count++;
			else
				break;
		}
		return *((char*)a+count) > *((char*)b+count) ? 1 : 0;
	}
	else if(endian() == 2)
	{
		int count = width;
		while(count > 0)
		{
			if( *((char*)a+count) == *((char*)b+count)  )
				count--;
			else
				break;
		}
		return *((char*)a+count) > *((char*)b+count) ? 1 : 0;
	}
}

int middle_order(node* p,int width)
{
	if( p != NULL )
	{
		middle_order(p->left,width);
		printf("%d\t",*((int*)(p->num)) );
		Count++;
		if(Count%10 == 0)
			printf("\n");
		middle_order(p->right,width);
	}
	return 0;
}

int main(int argc,char* argv[])
{
	int src[100];
	int i;
	//print the random list to the screen
	srand( (unsigned int)(time(0)) );
	printf("The random list is:\n");
	for( i = 0; i < 100; i++)
	{
		src[i] = rand()%100;
		printf("%d\t",src[i]);
		if(i%10 == 9)
			printf("\n");
	}
	//print the result to the screen
	printf("The sorted list is:\n");
	middle_order( Sort(src,100,sizeof(int),&Compare),sizeof(int) );

	return 0;
}
