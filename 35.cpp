#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
       int n = nums.size();
       int i=0;
	   for ( i=0;i<n;i++)
	   {
	   	if(target<=nums[i]) break;
		} 
		return i;
    }
};

int main()
{
	Solution s;
	int n[] = {1, 3, 5, 6, 7} ;
    vector<int> a(n, n+5) ;    
	cout<<s.searchInsert(a,5);
	int x;
	cin>>x;
 } 
