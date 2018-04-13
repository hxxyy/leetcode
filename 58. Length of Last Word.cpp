 using namespace std;
#include <iostream>
#include <string> 
 
class Solution {
public:
	int lengthOfLastWord(string s) {
		int len = s.size();
		int n = len;
		int res = 0;
		while (1)
		{
			if (s[n - 1] == ' ') n--;
			else break;
		}

		if (len == 0) return 0;

		while(n)
		{

			if (s[n - 1] != ' ') {
				res++;
				n--;

			}
			else break;
		}
		//	cout<<s[len-1];
		return res;
	}
};
int main()
{
	Solution s;
	std::cout << s.lengthOfLastWord("daxy");
	return 0;
}
