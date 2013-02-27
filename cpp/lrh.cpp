#include <iostream>

using namespace std;

int main(int argc, char** argv){
	float data;
	cin >> data;
	data *= 1000;
	data = (int)(data+0.5);
	data /= 1000;
	cout << data;
	return 0;
}
