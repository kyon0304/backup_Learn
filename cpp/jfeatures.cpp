/**
 * filename: jfeatures.cpp
 * Created on: 2012-2-23
 * Usage: Count the jump numbers(see the paper 'license plate location') of input image
 */
#include <iostream>
#include <opencv2/opencv.hpp>

#define TH 7
using namespace cv;
using namespace std;
int main(int argc, char* argv[])
{
	Mat readmat = imread(argv[1], 0);
	int rows = readmat.rows;
	int cols = readmat.cols;
	cout << rows << "\t" << cols << endl;
	int* xJump = new int[rows*sizeof(xJump)];
	int* yJump = new int[cols*sizeof(yJump)];
	int xTotalJump = 0,yTotalJump = 0;
	memset(xJump,0, sizeof(xJump)*rows);
	memset(yJump,0, cols*sizeof(yJump));
	int area = rows*cols;
	for(int i = 0; i < area; i++){
		if(readmat.data[i] < 128)
			readmat.data[i] = 0;
		else
			readmat.data[i] = 255;
	}
	for(int i = 0; i < rows-1; i++){
		for (int j = 0; j < cols-1; j++){
			xJump[i] += ((readmat.data[i*cols+j]==255 && readmat.data[i*cols+j+1]==0) ? 1 : 0);
			yJump[j] += ((readmat.data[i*cols+j]==255 && readmat.data[i*cols+cols+j]==0) ? 1 : 0);
		}
	}
	for(int i = 0; i < cols-1; i++){
		xJump[rows-1] += (readmat.data[rows*cols-cols+i]==255 && readmat.data[rows*cols-cols+i+1]==0) ? 1 : 0;
	}
	for(int i = 0; i < rows-1; i++){
		yJump[cols-1] += (readmat.data[i*cols+cols-1]==255 && readmat.data[i*cols+2*cols-1]==0) ? 1 : 0;
	}
	for(int i = 0; i < rows; i++){
		if(xJump[i] > TH)
			cout << "the " << i << "th line: " << xJump[i] << endl;
		xTotalJump += xJump[i];
	}
	for(int i = 0; i < cols; i++){
		if(yJump[i] > TH)
			cout << "the " << i << "th columns: " << yJump[i] << endl;
		yTotalJump += yJump[i];
	}
	cout << "total jumps x direction: " << xTotalJump <<", and the y: " << yTotalJump << endl;
	namedWindow("features", 0);
	imshow("features", readmat);
	cvWaitKey(0);
	delete xJump;
	delete yJump;
	return 0;
}
