#include <iostream>
#include <vector>

using namespace std;

void selectSort(){
	int arr[] = {4, 6, 1, 3, 5, 2};
	int index_min = 0;
	int t = 0;

	for(int i=0; i<5; i++){
		index_min = i;
		for(int j=i+1; j<6; j++){
			if(arr[index_min] > arr[j]){
				t = arr[index_min];
				arr[index_min] = arr[j];
				arr[j] = t;
			}
		}
	}
	for(int i=0; i<6; i++)
			cout << arr[i];
}

int main(){
	selectSort();
	return 0;
}