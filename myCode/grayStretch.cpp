#include <iostream>
#include <math>

#include "opencv2/opencv.hpp"

using namespace std;

int main( int argc, char* argv[])
{
	IplImage* src;
	IplImage* dst;

	src = cvLoadImage(argv[1], 0);
	

	
	cvNamedWindow("Origin",1);
	cvNamedWindow("Destination",1);
	cvShowImage("Origin",src);
	cvShowImage("Destination",dst);
	cvWaitKey(0);
	cvReleaseImage(&src);
	cvReleaseImage(&dst);
	cvDestroyWindow("Origin");
	cvDestroyWindow("Destination");

	return 1;
}
