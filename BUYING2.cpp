#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int n, x;
        int s=0, m = 100007;
        cin>>n>>x;
        for(int i=0; i<n; i++){
            int a;
            cin>>a;
            s += a;
            if(m>a) m = a;
        }
        //cout<<m<<" "<<s<<" "<<x;
        int d = (int)(s/x);
        if(s%x>=m)
            cout<<"-1\n";
        else
            cout<<d<<endl;
    }
	// your code goes here
	return 0;
}
