/*
 * Filename: fileOpen.cpp
 * Usage: test what cpp do if it can not open a file to read.
 * Created on: 2011-12-16
 * */

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifs;
	ifs.open( "0.txt" );
	if( !ifs )
		cout << "No such file!" << endl;
	else
		cout << "fine." << endl;
	return 0;
}
