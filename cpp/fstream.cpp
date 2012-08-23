#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("test.txt");
	int num;
	if(!ifs){
		ofs.open("test.txt");
		ofs << 1;
		ofs.flush();
	}else{
		ifs >> num;
		ifs.close();
		ofs.open("test.txt");
		ofs << num;
		ofs << 1;
		ofs.flush();
	}
	ofs.close();
}
