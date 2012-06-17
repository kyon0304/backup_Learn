/**
 * filename: gfeatures.cpp
 * Created on: 2012-2-23
 * Usage: Count the sum of gray(see the paper 'license plate location') of input image
 */
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;
int main(int argc, char* argv[])
{
	Mat readmat = imread(argv[1], 0);
	int graySum = 0;
	int area = readmat.rows * readmat.cols;
	for(int i = 0; i < area; i++){
		graySum += readmat.data[i];
	}
	cout << "the gray sum is: " << graySum << endl;
	return 0;
}
