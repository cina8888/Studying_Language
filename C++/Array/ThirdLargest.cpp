#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int _3Largest(vector<int> arr) {
	if (arr.size() < 3) {
		return -1;
	}
	sort(arr.begin(), arr.end());
	return arr[arr.size()-3];
}

int main() {
	vector<int> numbers = {1, 32 , 4, 5, 23, 56};
	cout << _3Largest(numbers) << "\n";
	
	return 0;
}
