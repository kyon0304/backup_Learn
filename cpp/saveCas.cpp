/* Filename: saveCas.cpp
 * Usage: for the adaboost code, save data to files.
 * Created on: 2011-12-13
 * */

#include <iostream>
#include <fstream>

using namespace std;
int main()
{
	int sc,wc,rc;
	double th;
	int dir;

	ofstream cas( "cascade.txt" );
	sc = 3;
	cas << sc << endl;
	for( sc = 1; sc < 4; sc++ ){
		wc = 2; cas << wc << endl;
		for( wc = 1; wc < 3; wc++ ){
			rc = 2; cas << rc << endl;
			for( rc = 1; rc < 3; rc++ ){
				th = 0.34; dir = 0;
				cas << th << "\t" << dir << endl; 
				cas << "---------------" << endl;
			}
			cas << "+++++++++++++++" << endl;
		}
	}
}
