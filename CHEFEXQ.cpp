#include<iostream>
using namespace std;

int main(){
    int n, q;
    cin>>n>>q;
    int a[n+1];
    a[0] = 0;
    for(int i = 1; i<=n; i++)
        cin>>a[i];
    while(q--){
        int t, i, k;
        cin>>t>>i>>k;
        if(t==1){
            a[i]=k;
            continue;
        }
        int c = 0;
        if(a[1]==k)
            c++;
        int x = a[1];
        for(int j = 2; j<=i; j++){
            x = x^a[j];
            if(x==k)
                c++;
        }
        cout<<c<<"\n";
    }
    return 0;
}
