#include <iostream>

void merge(int arr[], int tmp[], int start, int mid, int end){
	for(int i = start; i <= end; i++)
		tmp[i] = arr[i];
		int p1 = start;
		int p2 = mid + 1;
		int index = start;
		while(p1 <= mid && p2 <= end){
			if(tmp[p1] <= tmp[p2]){
				arr[index] = tmp[p1];
				p1++;
			}else{
				arr[index] = tmp[p2];
				p2++;
			}
			index++;
		}
		for (int i = 0; i<= mid - p1; i++)
			arr[index + i] = tmp[p1 +i];
}

void printArray(int arr[], int N){
	for(int i = 0; i<N; i++)
		printf("%d ",arr[i]);
}

void mergeSort(int arr[], int tmp[], int start, int end){
	if(start < end){
		int mid = (start+end) / 2;
		mergeSort(arr, tmp, start, mid);
		mergeSort(arr, tmp, mid+1, end);
		merge(arr, tmp, start, mid, end);	
	}
}

int main(){
	int N = 0;
	scanf("%d", &N);

	int stored[N];
	int tmp[N];

	for(int i = 0; i<N; i++)
		scanf("%d", &stored[i]);

	mergeSort(stored, tmp, 0, N-1);
	printArray(stored, N);
	return 0;
}