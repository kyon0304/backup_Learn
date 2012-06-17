/*
 *Created on 2011-11-23
 *resize.cpp unify the size of pic
 *
 * Author: Wang Ying
 * */

#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv2/core/core.hpp>
//#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

int main( int argc, char* argv[] )
{
	ifstream in( argv[1] );
	string filename;
//	string path = "../unified/";
	string fullPath;

	Mat pic;
	Mat picNew( 24, 24, CV_8UC3);
	Mat temp( 72, 72, CV_8UC3 );
	Rect roi( 100, 50, 72, 72 );
	while( getline( in, filename))
	{
		pic = imread( filename );
		temp = pic( Range(122,194), Range(172,244) );
		resize( temp, picNew, picNew.size() );
		fullPath =  filename;
		imwrite( fullPath, picNew);
	}
//	Mat pic = imread( argv[1] );
////	cout << pic.flags << endl;
//	Mat picNew( 24, 24, CV_8UC1);
//	resize( pic, picNew, picNew.size(), 0, 0 );
//	namedWindow( "orig", 1 );
//	namedWindow( "new", 1 );
//	imshow( "orig", pic );
//	imshow( "new", picNew );
//	waitKey(0);
	return 0;
}
