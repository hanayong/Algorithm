#include <iostream>
// #include <algorithm>

void bubbleSort(){
	int arr[] = {20, 10, 90, 29, 5};

// first way
// 	for(int i=0;i<sizeof(arr)/sizeof(arr[0])-1;i++)
// 		for(int j=0;j<sizeof(arr)/sizeof(arr[0])-1;j++){
// 			if(arr[j] > arr[j+1]){
// 				int tmp = arr[j];
// 				arr[j] = arr[j+1];
// 				arr[j+1] = tmp;
// 			}
// 		}
// }

// second way
	for(int i=0;i<sizeof(arr)/sizeof(arr[0])-1;i++)
		for(int j=0;j<sizeof(arr)/sizeof(arr[0])-1;j++){
			if(arr[j] > arr[j+1]){
				std::swap(arr[j], arr[j+1]);
			}
		}
}

int main(){
	bubbleSort();

	return 0;
}