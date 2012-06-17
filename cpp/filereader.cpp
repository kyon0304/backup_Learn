/*
 *filerreader.cpp
 *Read from file that stores pic detailed information 
 *
 *Created on: 2011-11-22 Author: Wang Ying
 *
 * */

#include <iostream>
#include <fstream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <cassert>
#include <string>
#include <sstream>
//#include <cstddef>
//#include <cstring>
using namespace std;

int main( int argc, char* argv[] )
{
	char* filename;
	ostringstream info;
	filename = argv[1];
	ifstream in( filename );
//	assure( in, filename );
	
	int width,height;
	CvMat** pic;
	int count = 0;

	while( getline( in, info ) )	
	{
		info >> width >> height;
		assert( width%1 == 0 && height%1 == 0 );
		pic[count] = cvCreateMat( width, height, CV_8UC1);
		int step = pic[count]->step/sizeof(float);
		float* data = pic[count]->data.fl;
		for( int i = 0; i < width; i++ )
		{
			for(int j = 0; j < height; j++ )
			{
				info >> ( data + i*step )[j];
			}
		}
		count++;
	}		
	return 0;
}
