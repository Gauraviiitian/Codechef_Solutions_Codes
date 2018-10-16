#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int t;
    cin>>t;
    long long int val[2000001];
    //Counting values of each number.
    for(int i = 0; i<2000001; i++){
        if(i<10){
            if(i%2==0)
                val[i] = i;
            else
                val[i] = 0-i;
        }
        else{
            val[i] = val[i%10] + val[i/10];
        }
    }
    for(int i = 0; i<2000001; i++)
        val[i] = abs(val[i]);
    long long int ans[1000001];
    //Counting the answer for every possible value of n
    ans[0] = 0;
    ans[1] = 2;
    ans[2] = 12;
    long long int add = 10;
    for(int i = 3; i<=1000000; i++){
        add = add + val[2*i] + 2*val[2*i-1] + val[2*i-2] - 2*val[i];
        ans[i] = ans[i-1] + add;
    }
    while(t--){
        int n;
        cin>>n;
        cout<<ans[n]<<"\n";
    }
    return 0;
}
