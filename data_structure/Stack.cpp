#include <iostream>
#define SIZE 100

using namespace std;

int Stack[SIZE];
int Top = -1;

void push(int data){

	if (Top == 99){
		cout << "This stack is full." << endl;
	}

	Top++;
	Stack[Top] = data;

	return;
}

int pop(){
	if (Top == -1){
		cout << "This stack is empty." << endl;
		return 0;
	}

	return Stack[Top];
}

int isempty(){
	if(Top == -1){
		return 1;
	}
	return 0;
}


int main(){

	push(10);
	push(5);
	cout << isempty() << endl;
	cout << pop();

	return 0;	
}