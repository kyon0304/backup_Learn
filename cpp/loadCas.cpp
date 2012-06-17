/*
 * Filename: loadCas.cpp
 * Usage: load data from file to construct a cascade using in adaboost.
 * Created on: 2011-12-13
 * */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

template <class T>
void convertFromString( T &, const string & );

int main()
{
	int sc,wc,rc,dir;
	double th;
	sc = 0;

	ifstream cas("cascade.txt");
	//ostringstream info;
	string s;
	getline( cas, s );
//	info >> sc;
	cout << s << endl;
	stringstream ss;
	ss << s; ss >> sc; ss.clear();
//	convertFromString( sc, s );
	cout << sc << endl;
	getline( cas, s );
	getline( cas, s );
	getline( cas, s );
	string s1,s2;
	istringstream is(s);
	is >> s1 >> s2;
	is >> th >> dir;
	cout << s1 << " " << s2 << endl;
	//convertFromString( th, s1 );
	cout << th << "\t" << dir << endl;
//	convertFromString( th, s );
	return 0;
	//while()
}

template <class T>
void convertFromString( T &value, const string &s ){
	stringstream ss(s);
	ss >> value;
}
