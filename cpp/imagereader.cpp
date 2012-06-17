/*
 *imagereader.cpp
 * * Read pos&neg image from path in a txt file
 *
 * Created on: 2011-11-22 Author: Wang Ying
 * */

#include <fstream>
#include <iostream>
#include <string>
#include <opencv2/highgui/highgui.hpp>
#include <vector>

using namespace std;
using namespace cv;

int main( int argc, char* argv[] )
{
	char* filename;
	string path;
	filename = argv[1];
	ifstream in( filename );
	ofstream out( "pos" );
	Mat tmp;
	vector<Mat> picMat;

	while( getline( in, path ) )
	{
		tmp = imread( path.data(), 0 );
		picMat.push_back(tmp);
	//	out << tmp.cols << " " << tmp.rows << " " << endl;
	//	int area = tmp.rows * tmp.cols;
	//	for( int i = 0; i < area; i++ )
	//		out << (int)(uchar)*( (tmp.data + i ) ) << " ";
	//	out << endl;
	}

	return 0;
}
