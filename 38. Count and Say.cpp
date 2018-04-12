 
#include <iostream> 
#include <sstream>
#include<string> 
using namespace std;

class Solution {
public:
	string countAndSay(int n) {
		string str = "", t, init = "1";
		char c = '1';

		int num = 0;
		for (int i = 0; i<n-1; i++)
		{
			int len = init.size();
			for (int j = 0; j <=len; j++)
			{
				if (init[j] == c) num++;
				else
				{
					stringstream ss;
					ss << num;
					t = ss.str();
					str += t;
					str += c;
					num = 1;
					c = init[j];
				}

			}	 init = str;c = init[0]; str = "";num=0;
		}
		return init;
	}
};

int  main()
{
	Solution s;
	
	cout << s.countAndSay(4) << endl;
	return 0;
}
