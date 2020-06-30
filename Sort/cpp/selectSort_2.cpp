#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
	int n = 0;
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	vector<pair<int, int>> v(n);

	for (int i=0; i<n; i++){
		cin >> v[i].first;
		v[i].second = i;
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++)
		cout << v[i].first;

	return 0;

}