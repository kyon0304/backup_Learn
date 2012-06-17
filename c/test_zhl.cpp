#include<iostream>
#include<time.h>
#include<stdlib.h>
#include<string.h>
//#include<stdio.h>
using namespace std;
//inline int Max(int a,int b) {return a>b?a:b;}

int main()
{
 int n=100;
 int temp_a=0;
 int temp_b=0;
 int *a=(int *)malloc(sizeof(int)*n);
 int *b=(int *)malloc(sizeof(int)*n);
 srand((unsigned int )(time(0)));
int num=0;
for(int j=0;j<100;j++){
 temp_a=temp_b=0;
 for(int i=0;i<n-1;i++)
{
  a[i]=rand()%50;
  b[i]=rand()%50;
  temp_a+=a[i];
  temp_b+=b[i];
}
 cout<<"temp_a is "<<temp_a<<"   temp_b is "<<temp_b<<"  j is   "<<j<<endl;
if(temp_a>temp_b)
{
  a[n-1]=0;
  b[n-1]=temp_a-temp_b;
}
else{
  b[n-1]=0;
  a[n-1]=temp_b-temp_a;
}
temp_a=temp_b=0;
int k=0;
for(int i=0;i<n;i++){
 //cout<<"a is"<<a[i]<<"   b is"<<b[i]<<endl;
	temp_a=temp_b=0;
 while(temp_a>=temp_b){
  temp_a+=a[(k+i)%n];
  temp_b+=b[(k+i)%n];
  k++;
  if(k==n){
  //cout<<"success"<<endl;
  num++;
  break;
  //return 0;
}
break;
}
}
}
  cout<<"faint"<<num<<endl;
//    cout << "the max is "<<Max(++a, b) <<endl << "now a ="<<a << endl;
             //a is incremented twice
//    cout << "the max is "<<Max(++a, b + 10) <<endl << "now a ="<<a << endl;
        //a is incremented once
 return 0;
}
