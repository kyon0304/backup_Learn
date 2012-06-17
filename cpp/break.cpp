/**
 * @file break.cpp
 * @date 2012-2-9
 * break只能跳出一层循环
 */
#include <iostream> 
#include <string>
using namespace std;

int main(int argc, char* argv[])
{
	int i = 0;
	int j = 0;
	int k = 0;
	while(i < 3){
		i++;
		while(j < 2){
			j++;
			while(k < 2){
				k++;
				if(i == 2)
					break;
				cout << "k = " << k << "\t";
			}
			cout << "j = "<< j << endl;
		}
		cout << "i = " << i << endl;
		j = 0; k = 0;
	}
	return 0;
}
