#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<float> f1;
	vector<float> f2;
	vector<float> f3;
	for( int i = 0; i < 5; i++ )
	{	
		f1.push_back(2.3);
	}
		
	for( int i = 0; i < f1.size(); i++ )
	{
		cout << f1[i] << endl;
	}

	for( int i = 0; i < f1.size(); i++)
	{
		f1[i] *= f1[i];
	}

	for( int i = 0; i < f1.size(); i++ )
	{
		cout << f1[i] << endl;
	}
	return 0;
}
