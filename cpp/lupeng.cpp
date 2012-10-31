#include <iostream>
using namespace std;

int main(int argc, char** argv){
	typedef int intarray[4];
	int ia[2][4] = {1,2,3,4,5,6,7,8};
	for(intarray *p = ia; p != ia+2; ++p){
		for(int* q = *p; q != *p+4; ++q)
			cout << *q << "\t";
		cout << endl;
	}
	intarray *p;
	cout << sizeof(*p) << "\t " << sizeof(ia) << "\t" << sizeof(int) << "\t" << sizeof(char) << endl;
}
