#include <iostream>
#include <vector>
#include <climits>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    	int temp=0;int res=-2147483648;int h=-2147483648;
        int len = nums.size();
        for(int i=0;i<len;i++)
		{
			for(int j=i;j<len;j++)
			{
				temp+=nums[j];
				if(temp>res) res = temp;
			}
			if(res>h) h=res;
			temp=0;
		 } 
      return res;  
    }
};
int main()
{
	Solution s;
	int n[] = {-3,4,-1,2,1,-5} ;
    vector<int> a(n, n+6) ;    
	cout<<s.maxSubArray(a)<<endl;
	return 0;
}
