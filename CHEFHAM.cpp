#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[n];
        for(int i=0; i<n; i++)
            cin>>a[i];
        int cnt=n;
        if(n==1){
            cout<<"0\n"<<a[0]<<"\n";
            continue;
        }
        else if(n==2){
            if(a[0]==a[1])
                cout<<"0\n";
            else
                cout<<"2\n";
            cout<<a[1]<<" "<<a[0]<<"\n";
            continue;
        }
        else if(n==3){
            if(a[0]==a[1] || a[0]==a[2]){
                cout<<"2\n"<<a[0]<<" "<<a[2]<<" "<<a[1]<<"\n";
            }
            else if(a[1]==a[2]){
                cout<<"2\n"<<a[1]<<" "<<a[0]<<" "<<a[2]<<"\n";
            }
            else{
                cout<<"3\n"<<a[1]<<" "<<a[2]<<" "<<a[0]<<"\n";
            }
            continue;
        }
        int j=0;
        int b[n], tbl[n];
        for(int i=0; i<n; i++)
            tbl[i] = 0;
        for(int i = 0; j<n; i++){
            if(tbl[i%n]==0 && a[i%n]!=a[j]){
                b[j] = a[i%n];
                tbl[i%n] = 1;
                j++;
            }
            if(j==n-1 && a[0]==a[n-1] && tbl[0]==0){
                int temp = b[1];
                b[1] = a[n-1];
                b[n-1] = temp;
                break;
            }
            if(j==n-2 && a[n-2]==a[n-1] && tbl[n-2]==0 && tbl[n-1]==0){
                int temp1 = b[0], temp2 = b[1];
                b[0] = a[n-2];
                b[1] = a[n-1];
                b[n-2] = temp1;
                b[n-1] = temp2;
                break;
            }
        }
        if(n<5){
            for(int i=0; i<n; i++){
                if(a[i]==b[i])
                    cnt--;
            }
            cout<<cnt<<"\n";
            for(int i=0; i<n; i++)
                cout<<b[i]<<" ";
        }
        else{
            cout<<n<<"\n";
            for(int i=0; i<n; i++){
                cout<<b[i]<<" ";
            }
        }
        cout<<"\n";
    }
}
