#include <fstream>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
int main( int argc, char* argv[] )
{
	ifstream in( argv[1] );
	IplImage* pic;
	IplImage* picNew = cvCreateImage( cvSize(24,24), 8, 3);
	
	string path;
	while( getline( in, path ) )
	{
		pic = cvLoadImage( path.data() );
		cvSetImageROI( pic, cvRect( 100, 100, 24, 24 ) );
		cvCopy( pic, picNew);
		cvSaveImage( path.data(), picNew);
	}
	return 0;
}
