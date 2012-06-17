
#include <stdio.h> 

typedef   union   
{ 
        long   l; 
        char   str[sizeof(long)]; 
}u; 

int   main() 
{ 
      u   endian; 
      endian.l   =   1; 

      if(   endian.str[0]   ==   1   ) 
      { 
                printf( "You   host   little   endian\n "); 
      } 
      else   if(   endian.str[sizeof(long)-1]   ==   1) 
      { 
              printf( "You   host   big   endian\n "); 
      } 
      else 
      { 
              printf( "You   host   unknow   endian,   are   you   made   it   by   yourself?\n "); 
      } 
	return 0;
}
