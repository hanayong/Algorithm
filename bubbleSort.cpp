#include <iostream>

void bubbleSort(){
	int arr[] = {20, 10, 90, 29, 5};

	for(int i=0;i<sizeof(arr)/sizeof(arr[0])-1;i++)
		for(int j=0;j<sizeof(arr)/sizeof(arr[0])-1;j++){
			if(arr[j] > arr[j+1]){
				int tmp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = tmp;
			}
		}
}

int main(){
	bubbleSort();

	return 0;
}