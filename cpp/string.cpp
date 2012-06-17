#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

int main( int argc, char* argv[] )
{
//	fstream in(argv[1]);
//	string s;
//	while( getline( in, s ) )
//	{
//		cout << s.size() << endl;
//		cout << s << endl;
//		cout << s[6] << endl;
//	}
//	FILE* picInfo;
//	picInfo = fopen( argv[1], "r");
//	if( picInfo )
//		cout << "OK!" << endl;
//	int w,h,ws,v;
//	fscanf( picInfo, "%d %d %d", &w, &h, &ws );
//	cout << w << " " << h << endl;
//	int area = w*h;
//	for(int i = 0; i < area; i++)
//	{
//		fscanf( picInfo, "%d", &v );
//		printf( "%d\t", v);
//	}
//	printf("\n");
//	fclose( picInfo );
	char c[256];
	string s = "hello";
	int i = 10;
	sprintf( c, "%d", i );
	s += c;
	//stringstream ss;
	//string s3;
	//ss << i;
	//ss >> s3;
	//ss.clear();
	//cout << s << endl;
	ofstream ofs;
	ofs.open("0.txt");
	ofs << i << endl << 20 << endl;
	ofs.close();
	//ofstream ofs("0.txt");
	ofs.open("0.txt");
	ofs << 19 << endl;
	ofs.close();
	ifstream ifs("0.txt");
	string s2;
	int j;
	stringstream ss;
	while( true ){
		cout << getline( ifs, s2 ) << endl;
		cout << ifs << endl;
		ss << s2; ss >> j; ss.clear();
		cout << j << endl;
		if( ifs.eof() )
			break;
		//getline( ifs, s2 );
	}
	return 0;
}
