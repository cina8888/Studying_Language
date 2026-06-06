#include <iostream>
#include <vector>
using namespace std;

void reverse(vector<int> &arr){
	int n = arr.size();
	vector<int> temp(n);
	//append reverse into temp array
	for (int i = 0; i < n; i++) {
		temp[i] = arr[n-1-i];
	}
	//make temp arr into real array
	for (int i = 0; i < n; i++) {
		arr[i] = temp[i];
	}

}

int main() {
	vector<int> arr = {1, 4, 5, 7, 8, 13};
	reverse(arr);

	for (int num:arr){
		cout << num << " ";
	}
	cout << "\n";
	return 0;
}	
