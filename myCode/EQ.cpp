#include <iostream>
#include <cmath>
#include <opencv2/opencv.hpp>
using namespace std;
int main(int argc, char* argv[])
{
	IplImage* src = cvLoadImage(argv[1],0); 

	int pixel[256];
	for(int i = 0; i < 256; i++)
		pixel[i] = 0;
	int size =( src->width) * (src->height);
	for(int i = 0; i < size; i++){
		pixel[(int)(unsigned char)src->imageData[i]]++;
	}

	double cx[256];
	//for(int i = 0; i < 256; i++)
		//cx[i] = 0.0;
	for(int i = 0; i < 256; i++){
		cx[i] = pixel[i];
		for(int j = 0; j < i; j++)
			cx[i] += pixel[j];
	}
	for(int i = 0; i< 256; i++){
		cx[i] /= 1.0;
		cx[i] /= size; 
	}
	
	char pdst[256];
	for(int i = 0; i < 256; i++)
		pdst[i] = (char)(floor(cx[i] * 256+0.5));

	IplImage* dst = cvCreateImage(cvSize(src->width,src->height), 8 ,1);
	for(int i = 0; i < size; i++){
		int k = (int)(unsigned char)(src->imageData[i]);
		dst->imageData[i] = pdst[k];
	}
	cvNamedWindow("Origin",1);
	cvNamedWindow("EQ",1);

	cvShowImage("Origin",src);
	cvShowImage("EQ",dst);

	cvWaitKey(0);

	cvReleaseImage(&src);
	cvReleaseImage(&dst);

	cvDestroyWindow("Origin");
	cvDestroyWindow("EQ");


	return 0;
}
